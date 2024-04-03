from qai_datadog.connector import DatadogConnector  
from qai_datadog.driver import DatadogDriver, translate_search, translate_observable_search 
from qai_ocsf_schema.objects import Device, Email, File, Observable, Os, User 
from qai_ocsf_schema.classes import ProcessActivity, Authentication, SecurityFinding 
from qailib.search import S
from typing import List, cast, Type, Optional
from masala.entity import Entity 
import datetime
from masala.hints import EntityType

from masala.results import SubQuery, SubQueryId


configuration = {
}

connector = DatadogConnector(**configuration)
driver = DatadogDriver(connector)

def get_queries(test_cases: dict[str, list[S | bool | Type[Entity]]]) -> list[dict[str, str]]:

    queries_observables = {}
    for k, v in test_cases.items():
        search = cast(S, v[0])
        ocsf_type = cast(Entity, v[2])
        q = translate_observable_search(search=search, top_level_entity=ocsf_type) # type: ignore
        queries_observables.update({k: q})
    
    queries_top_level = {}
    for k, v in test_cases.items():
        search = cast(S, v[0])
        ocsf_type = cast(Entity, v[2])
        field_map = driver.get_platform_data(entity_type=ocsf_type).mapping # type: ignore
        q = translate_search(search=search, field_map=field_map) 
        queries_top_level.update({k: q})

    return [queries_observables, queries_top_level] 



sub_query_id_2 = SubQueryId(label="os", relationship="os")
sub_query_2 = SubQuery(entity_type=Os, search=S(), annotations=[], id=sub_query_id_2)


class TestExecutor:
    ...

def test_executor(test_cases: dict[str, list[S | bool | Type[Entity]]] , check_results_for: list[str] = []) -> dict[str, str]:

    sub_query_id_1 = SubQueryId(label="observables", relationship="observables")
    
    time_range_filter = S(time__gte=datetime.datetime(2024, 2, 24, 7, 55, 21, 260000, tzinfo=datetime.timezone.utc)) & S(
        time__lte=datetime.datetime(
            2024, 2, 25, 7, 55, 21, 260000, tzinfo=datetime.timezone.utc)
    )
    
    test_case_results = {} 
    for test_case,v in test_cases.items():
        expected_passed = False
        notexpected_passed = False
        resultset = None

        expected = v[1]
        ocsf_type = cast(Entity, v[2])
        search_filter = cast(S, v[0])
        observable_annotation = SubQuery(entity_type=Observable, search=search_filter, annotations=[], id=sub_query_id_1)

        top_level_query = False 
        if len(v) >= 4:
            top_level_query = v[3]
        
        if top_level_query: 
            resultset = ocsf_type.filter(search=search_filter & time_range_filter, driver=driver)
        else:
            resultset = ocsf_type.filter(search=time_range_filter, driver=driver).annotate(observable_annotation)

        error = ''
        try:
            results = resultset.search_results
        except Exception as e:
            error = e
        
        expected_passed = expected and len(results) > 0
        notexpected_passed = not expected and len(results) == 0

        if check_results_for:
            for tc in check_results_for:
                if tc == test_case:
                    print(f"CHECK RESULTS FOR: {check_results_for}") 
        test_case_results.update({test_case: 'passed' if (expected_passed or notexpected_passed) and not error else f'failed: {error}'})
    
    return test_case_results
# Intune
test_cases: dict[str, list[S | bool | Type[Entity] ]] = {
    
    # SecurityFinding related test cases
    "000": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__contains="query"), True, SecurityFinding],
    "001": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__contains="QUERY"), False, SecurityFinding],
    "002": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__icontains="QUERY"), True, SecurityFinding],
    
    "003": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__exact="iris.query.ai"), False, SecurityFinding],
    "004": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__exact="splunk2.sesandbox.query.ai"), True, SecurityFinding],
    "005": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__iexact="Splunk2.sesandbox.query.ai"), True, SecurityFinding], 
    
    "006": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__startswith="splunk"), True, SecurityFinding],
    "007": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__startswith="Splunk"), False, SecurityFinding],
    "008": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__istartswith="splunk"), True, SecurityFinding],
    "009": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__istartswith="Splunk"), True, SecurityFinding],
    
    "010": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__endswith="ai"), True, SecurityFinding],
    "011": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__endswith="Ai"), False, SecurityFinding],
    "012": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__iendswith="ai"), True, SecurityFinding],
    "013": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__iendswith="Ai"), True, SecurityFinding],
    
    "014": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__in={"iris.query.ai", "splunk2.sesandbox.query.ai"}), True, SecurityFinding],
    "015": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__in={"iris.query.ai"}), False, SecurityFinding],
    "015.1": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__in={"splunk2.sesandbox.query.ai"}), True, SecurityFinding],
    "015.2": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__in={"Splunk2.sesandbox.query.ai"}), False, SecurityFinding],
    "015.3": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__iin={"Splunk2.sesandbox.query.ai"}), True, SecurityFinding],
    "016": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__iin={"Iris.query.ai", "Splunk2.sesandbox.query.ai"}), True, SecurityFinding],
    
    "017": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__gte="A"), True, SecurityFinding],
    "018": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__lte="z"), True, SecurityFinding],
    
    "019": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__isnull=False), True, SecurityFinding],
    "020": [S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__isnull=True), True, SecurityFinding],
    
    "021": [(S(value__startswith="splunk") & S(type_id__exact=Observable.TypeId.HOSTNAME)) | (S(value__contains="query") & S(type_id__exact=Observable.TypeId.HOSTNAME)), True, SecurityFinding],
    "022": [(S(value__startswith="splunk") & S(type_id__exact=Observable.TypeId.HOSTNAME)) & (S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__contains="query")), True, SecurityFinding],
    "023": [(S(value__startswith="abc") & S(type_id__exact=Observable.TypeId.HOSTNAME)) | (S(value__contains="lll") & S(type_id__exact=Observable.TypeId.HOSTNAME)), False, SecurityFinding],
    
    "024": [S(type_id__exact=Observable.TypeId.HOSTNAME) & ~S(value__contains="query"), False, SecurityFinding, True],
    
    "025": [S(message__contains="CPU"), True, SecurityFinding, True],
    "026": [S(severity_id__exact=SecurityFinding.SeverityId.INFORMATIONAL), True, SecurityFinding, True],
    "027": [S(status_id__exact=SecurityFinding.StatusId.UNKNOWN), True, SecurityFinding, True],
    "028": [S(status_id__exact=SecurityFinding.StatusId.SUCCESS) | S(message__contains='CPU'), True, SecurityFinding, True],
    "029": [S(status_id__exact=SecurityFinding.StatusId.UNKNOWN) & S(message__contains='CPU'), True, SecurityFinding, True],
    "030": [S(status_id__exact=SecurityFinding.StatusId.SUCCESS) & S(message__contains='YOLO'), False, SecurityFinding, True],
    
    # ProcessActivity related test cases
    "031": [(S(value__exact="iris.query.ai") & S(type_id__exact=Observable.TypeId.HOSTNAME)), True, ProcessActivity],
    "032": [(S(value__exact="irs.query.ai") & S(type_id__exact=Observable.TypeId.HOSTNAME)), False, ProcessActivity],
    
} 

generated_queries = get_queries(test_cases=test_cases)
check_results_for = [
    '019',
    '020',
]
test_results = test_executor(test_cases=test_cases, check_results_for=check_results_for)
 
failed_cases = [k for k, v in test_results.items() if 'failed' in v]
if failed_cases:
    print(f"FAILED CASES: {failed_cases}")
else: print("All test cases PASSED.")
print(f"Total {len(test_cases)} testcases run.")


print("##### THE END ######")



