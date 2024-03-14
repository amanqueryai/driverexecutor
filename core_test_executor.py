from qailib.search import S
from masala.results import SubQuery, SubQueryId
from typing import Any
from abc import ABC, abstractmethod
from masala.drivers import BaseDriver



class TestExecutor(ABC):

    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def run_test(self) -> None:
        pass

class TestExecutorAnnotated(TestExecutor):
    
    def __init__(self) -> None:
        super().__init__()

    def generate_search_response(self, result: str, generated_query: str = "") -> dict[str, str]:
        return {
            "result": result,
            "generated_query": generated_query,
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
            generated_query = ""

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
            
            if query_generator_callback: 
                generated_query = query_generator_callback(**callback_params)

            query_results = resultset.search_results
            
            if show_results:
                print(query_results)
        
        except Exception as err:
            print(f"Exception occurred while searching. {test_case_id} FAILED.")
            return self.generate_search_response(result=f"Failed. Reason: {err}")

        expected_passed = results_expected and len(query_results) > 0
        notexpected_passed = not results_expected and len(query_results) == 0

        return self.generate_search_response(result='Passed' if (expected_passed or notexpected_passed) else 'Failed', generated_query=generated_query)
        

class TestAggregator:

    def __init__(self) -> None:
        self.annotated_executor = TestExecutorAnnotated()

    def get_failed_test_cases_from_results(self, results: dict[str, dict[str, str]]) -> list[str]:

        failed_cases = []
        for id, result in results.items():
            if 'failed' in result['result'].lower():
                failed_cases.append(id)
            
        return failed_cases

    def aggregate_test_cases(self, test_cases: dict[str, Any], driver: BaseDriver) -> dict[str, list[str] | dict[str, str]]:
        results = {}
        for test_case_id, details in test_cases.items():
            curr_result = self.annotated_executor.run_test(test_case_id=test_case_id, test_case_details=details, driver=driver)
            results.update({test_case_id: curr_result})
        
        return {
            'results': results,
            'failed_cases': self.get_failed_test_cases_from_results(results=results)
        } 
    


# Intune
 
# failed_cases = [k for k, v in test_results.items() if 'failed' in v]
# if failed_cases:
#     print(f"FAILED CASES: {failed_cases}")
# else: print("All test cases PASSED.")


# print("##### THE END ######")

