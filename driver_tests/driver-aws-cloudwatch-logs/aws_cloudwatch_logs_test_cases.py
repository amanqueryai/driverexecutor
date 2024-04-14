
from qailib.search import S
from typing import Any
from qai_ocsf_schema.classes import HttpActivity 
from qai_ocsf_schema.objects import Observable
import datetime
import os
import sys

parent = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
parent_parent = os.path.dirname(parent)
sys.path.append(parent_parent)

time_range_filter = S(time__gte=datetime.datetime(2024, 3, 1, 7, 55, 21, 260000, tzinfo=datetime.timezone.utc)) & S(
    time__lte=datetime.datetime(
        2024, 3, 31, 7, 55, 21, 260000, tzinfo=datetime.timezone.utc)
)

TEST_CASES: dict[str, dict[str, Any]] = {

    # User based searches 
    # "000": {
    #     "filter": S(), 
    #     "time_range_filter": time_range_filter,
    #     "expected": True,
    #     "entity": HttpActivity,
    #     "followups": {},
    #     "show_results": False,
    # },
    # "001": {
    #     "filter": S(), 
    #     "time_range_filter": time_range_filter,
    #     "expected": True,
    #     "entity": HttpActivity,
    #     "followups": {
    #         "followup_filter": S(type_id__exact=Observable.TypeId.IP_ADDRESS) & S(value__exact="50.18.128.253"),
    #         "type": Observable,
    #         "relationship": "observables",
    #     },
    #     "show_results": False,
    # },
    # "002": {
    #     "filter": S(), 
    #     "time_range_filter": time_range_filter,
    #     "expected": True,
    #     "entity": HttpActivity,
    #     "followups": {
    #         "followup_filter": S(type_id__exact=Observable.TypeId.IP_ADDRESS) & S(value__exact="185.254.196.186"),
    #         "type": Observable,
    #         "relationship": "observables",
    #     },
    #     "show_results": False,
    # },
    # "003": {
    #     "filter": S(), 
    #     "time_range_filter": time_range_filter,
    #     "expected": True,
    #     "entity": HttpActivity,
    #     "followups": {
    #         "followup_filter": S(type_id__exact=Observable.TypeId.IP_ADDRESS) & S(value__exact="185.254.196.186") | S(type_id__exact=Observable.TypeId.IP_ADDRESS) & S(value__exact="50.18.128.253"),
    #         "type": Observable,
    #         "relationship": "observables",
    #     },
    #     "show_results": False,
    # },
    # "004": {
    #     "filter": S(), 
    #     "time_range_filter": time_range_filter,
    #     "expected": True,
    #     "entity": HttpActivity,
    #     "followups": {
    #         "followup_filter":  S(type_id__exact=Observable.TypeId.RESOURCE_UID) & S(value__exact="125343585094-app/mock-lambda-external-alb/72b69973b95c6ccf"),  
    #         "type": Observable,
    #         "relationship": "observables",
    #     },
    #     "show_results": False,
    # },
    # "005": {
    #     "filter": S(), 
    #     "time_range_filter": time_range_filter,
    #     "expected": True,
    #     "entity": HttpActivity,
    #     "followups": {
    #         "followup_filter":  S(type_id__exact=Observable.TypeId.RESOURCE_UID) & S(value__exact="125343585094-app/mock-lambda-external-alb/72b69973b95c6ccf"),  
    #         "type": Observable,
    #         "relationship": "observables",
    #     },
    #     "show_results": False,
    # },

    # # Random attributes searches
    # "006": {
    #     "filter": S(activity_id__exact=HttpActivity.ActivityId.HEAD), 
    #     "time_range_filter": time_range_filter,
    #     "expected": True,
    #     "entity": HttpActivity,
    #     "followups": {},
    #     "show_results": False,
    # },
    # "007": {
    #     "filter": S(severity_id__exact=HttpActivity.SeverityId.INFORMATIONAL), 
    #     "time_range_filter": time_range_filter,
    #     "expected": True,
    #     "entity": HttpActivity,
    #     "followups": {},
    #     "show_results": False,
    # },
    # "008": {
    #     "filter": S(status_id__exact=HttpActivity.StatusId.SUCCESS), 
    #     "time_range_filter": time_range_filter,
    #     "expected": True,
    #     "entity": HttpActivity,
    #     "followups": {},
    #     "show_results": False,
    # },
    # "009": {
    #     "filter": S(status_id__exact=HttpActivity.StatusId.FAILURE), 
    #     "time_range_filter": time_range_filter,
    #     "expected": True,
    #     "entity": HttpActivity,
    #     "followups": {},
    #     "show_results": False,
    # },

    # "010": {
    #     "filter": S(), 
    #     "time_range_filter": time_range_filter,
    #     "expected": True,
    #     "entity": HttpActivity,
    #     "followups": {
    #         "followup_filter": S(type_id__exact=Observable.TypeId.IP_ADDRESS) & S(value__in={"185.254.196.186", "50.18.128.253"}),
    #         "type": Observable,
    #         "relationship": "observables",
    #     },
    #     "show_results": True,
    # },


    # # Negative test cases
    # "011": {
    #     "filter": S(), 
    #     "time_range_filter": time_range_filter,
    #     "expected": False,
    #     "entity": HttpActivity,
    #     "followups": {
    #         "followup_filter": S(type_id__exact=Observable.TypeId.IP_ADDRESS) & S(value__exact="185.186"),
    #         "type": Observable,
    #         "relationship": "observables",
    #     },
    #     "show_results": True,
    # },

    # "012": {
    #     "filter": S(), 
    #     "time_range_filter": time_range_filter,
    #     "expected": True,
    #     "entity": HttpActivity,
    #     "followups": {
    #         "followup_filter":  S(type_id__exact=Observable.TypeId.RESOURCE_UID) & S(value__startswith="125343585094-app"),  
    #         "type": Observable,
    #         "relationship": "observables",
    #     },
    #     "show_results": False,
    # },
    # "013": {
    #     "filter": S(), 
    #     "time_range_filter": time_range_filter,
    #     "expected": True,
    #     "entity": HttpActivity,
    #     "followups": {
    #         "followup_filter":  S(type_id__exact=Observable.TypeId.RESOURCE_UID) & S(value__istartswith="125343585094-APP"),  
    #         "type": Observable,
    #         "relationship": "observables",
    #     },
    #     "show_results": False,
    # },
    # "014": {
    #     "filter": S(),
    #     "time_range_filter": time_range_filter,
    #     "expected": True,
    #     "entity": HttpActivity,
    #     "followups": {
    #         "followup_filter":  S(type_id__exact=Observable.TypeId.RESOURCE_UID) & S(value__endswith='mock-lambda-external-alb/72b69973b95c6ccf'),
    #         # "followup_filter":  S(type_id__exact=Observable.TypeId.RESOURCE_UID) & S(value__endswith='c6ccf'),
    #         "type": Observable,
    #         "relationship": "observables",
    #     },
    #     "show_results": True,
    # },
    # "015": {
    #     "filter": S(),
    #     "time_range_filter": time_range_filter,
    #     "expected": True,
    #     "entity": HttpActivity,
    #     "followups": {
    #         "followup_filter":  S(type_id__exact=Observable.TypeId.RESOURCE_UID) & S(value__iendswith='MOCK-LAMBDA-EXTERNAL-ALB/72B69973B95C6CCF'),
    #         "type": Observable,
    #         "relationship": "observables",
    #     },
    #     "show_results": False,
    # },
    # "016": {
    #     "filter": S(),
    #     "time_range_filter": time_range_filter,
    #     "expected": True,
    #     "entity": HttpActivity,
    #     "followups": {
    #         "followup_filter":  S(type_id__exact=Observable.TypeId.RESOURCE_UID) & S(value__contains='mock-lambda-external-alb'),
    #         "type": Observable,
    #         "relationship": "observables",
    #     },
    #     "show_results": True,
    # },
    # "017": {
    #     "filter": S(),
    #     "time_range_filter": time_range_filter,
    #     "expected": True,
    #     "entity": HttpActivity,
    #     "followups": {
    #         "followup_filter":  S(type_id__exact=Observable.TypeId.RESOURCE_UID) & S(value__icontains='MOCK-LAMBDA-EXTERNAL-ALB'),
    #         "type": Observable,
    #         "relationship": "observables",
    #     },
    #     "show_results": True,
    # },
    # "018": {
    #     "filter": S(),
    #     "time_range_filter": time_range_filter,
    #     "expected": True,
    #     "entity": HttpActivity,
    #     "followups": {
    #         "followup_filter":  S(type_id__exact=Observable.TypeId.RESOURCE_UID) & S(value__gte='0'),
    #         "type": Observable,
    #         "relationship": "observables",
    #     },
    #     "show_results": False,
    # },
    # "019": {
    #     "filter": S(),
    #     "time_range_filter": time_range_filter,
    #     "expected": True,
    #     "entity": HttpActivity,
    #     "followups": {
    #         "followup_filter":  S(type_id__exact=Observable.TypeId.RESOURCE_UID) & S(value__lte='2'),
    #         "type": Observable,
    #         "relationship": "observables",
    #     },
    #     "show_results": False,
    # },
    "020": {
        "filter": S(), 
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": HttpActivity,
        "followups": {
            "followup_filter":  S(type_id__exact=Observable.TypeId.RESOURCE_UID) & ~S(value__exact="125343585094-app/mock-lambda-external-alb/72b69973b95c6ccf"),  
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": True,
    },
} 