from qailib.search import S
from masala.results import SubQuery, SubQueryId
from typing import Any
from abc import ABC, abstractmethod
from masala.drivers import BaseDriver, BaseConnector

TOP_LVL_QUERY_STRING_KEY = "top_level_query_string"
FOLLOWUP_QUERY_STRING_KEY = "followup_query_string"

class TestExecutor(ABC):

    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def run_test(self) -> None:
        pass

class TestExecutorAnnotated(TestExecutor):
    
    def __init__(self) -> None:
        super().__init__()

    def generate_search_response(self, result: str, query_strings: dict[str, Any] = {}) -> dict[str, str]:
        return {
            "result": result,
            "top_level_query_string": query_strings.pop(TOP_LVL_QUERY_STRING_KEY),
            "followup_query_string": query_strings.pop(FOLLOWUP_QUERY_STRING_KEY),
        }

    def run_test(self, test_case_id: str, test_case_details: dict[str, Any], driver: BaseDriver) -> dict[str, str]:
        
        try:
            # Extract test case details
            top_level_filter = test_case_details["filter"]
            time_range_filter = test_case_details["time_range_filter"]
            results_expected = test_case_details["expected"]
            entity = test_case_details["entity"]
            followup_filter = None 
            followup_type, followup_relationship = None, ""
            
            show_results = test_case_details.get("show_results") 
            query_generator_callback = test_case_details.get("query_generator_callback")
            callback_params = test_case_details.get("callback_params", {}) 
            query_strings = {
                TOP_LVL_QUERY_STRING_KEY: "",
                FOLLOWUP_QUERY_STRING_KEY: "",
            }

            callback_params.update({"search": top_level_filter})

            followups = test_case_details.get("followups")
            
            if query_generator_callback:
                try:
                    platform_data = driver.get_platform_data(entity)
                except ValueError as err:
                    print(f"Exception occurred while generating outbound query syntax. {test_case_id} FAILED.")
                    return self.generate_search_response(result=f"Failed. Reason: {err}")

                field_map = platform_data.mapping
                callback_params.update({"field_map": field_map})
            
            if followups:
                followup_filter = followups.get("followup_filter") 
                followup_type = followups.get("type")
                followup_relationship = followups.get("relationship")

        except Exception as err:
            print(f"Exception occurred while fetching the test_case details. {test_case_id} FAILED.")
            return self.generate_search_response(result=f"Failed. Reason:{err}")

        sub_query_id = SubQueryId(label=followup_relationship, relationship=followup_relationship)
        observable_annotation = SubQuery(entity_type=followup_type, search=followup_filter, annotations=[], id=sub_query_id) # type: ignore
        
        expected_passed = False
        notexpected_passed = False
        resultset = None 

        try: 
            if followups:
                resultset = entity.filter(search=top_level_filter & time_range_filter, driver=driver).annotate(observable_annotation)
            else:
                resultset = entity.filter(search=top_level_filter & time_range_filter, driver=driver)
                
            # if query_generator_callback: 
            #     query_strings.update({TOP_LVL_QUERY_STRING_KEY: query_generator_callback(**callback_params)})

            #     if followups and followup_filter:
            #         callback_params.update({"search": followup_filter})
            #         query_strings.update({FOLLOWUP_QUERY_STRING_KEY: query_generator_callback(**callback_params)})

            if show_results:
                # Stop here and check if any break points are requierd in the main code
                print(f"About to run the testcase {test_case_id}")
            
            query_results = resultset.search_results
            
            if show_results:
                print(query_results)
        
        except Exception as err:
            print(f"Exception occurred while searching. {test_case_id} FAILED.")
            return self.generate_search_response(result=f"Failed. Reason: {err}", query_strings=query_strings)

        expected_passed = results_expected and len(query_results) > 0
        notexpected_passed = not results_expected and len(query_results) == 0

        return self.generate_search_response(result='Passed' if (expected_passed or notexpected_passed) else 'Failed', query_strings=query_strings)
        

class TestAggregator:

    def __init__(self) -> None:
        self.annotated_executor = TestExecutorAnnotated()

    def get_failed_test_cases_from_results(self, results: dict[str, dict[str, str]]) -> list[str]:

        failed_cases = []
        for id, result in results.items():
            if 'failed' in result['result'].lower():
                failed_cases.append(id)
            
        return failed_cases

    def aggregate_test_cases(
            self, 
            test_cases: dict[str, Any], 
            driver_type: BaseDriver,
            connector_type: BaseConnector,
            credentials: dict[str, Any],
        ) -> dict[str, list[str] | dict[str, str]]:
        results = {}
        for test_case_id, details in test_cases.items():
            driver = driver_type(connector_type(**credentials)) # type: ignore
            curr_result = self.annotated_executor.run_test(test_case_id=test_case_id, test_case_details=details, driver=driver)
            results.update({test_case_id: curr_result})
        
        return {
            'results': results,
            'failed_cases': self.get_failed_test_cases_from_results(results=results)
        } 
    