
from qailib.search import S
from typing import Any
from qai_ocsf_schema.objects import IpIntelligence
import datetime
import os
import sys

parent = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
parent_parent = os.path.dirname(parent)
sys.path.append(parent_parent)
from core_test_executor import TestAggregator

time_range_filter = S(time__gte=datetime.datetime(2024, 2, 24, 7, 55, 21, 260000, tzinfo=datetime.timezone.utc)) & S(
    time__lte=datetime.datetime(
        2024, 2, 25, 7, 55, 21, 260000, tzinfo=datetime.timezone.utc)
)
time_range_filter_process_activity = S(time__gte=datetime.datetime(2023, 9, 1, 7, 55, 21, 260000, tzinfo=datetime.timezone.utc)) & S(
    time__lte=datetime.datetime(
        2024, 3, 20, 7, 55, 21, 260000, tzinfo=datetime.timezone.utc)
)

TEST_CASES: dict[str, dict[str, Any]] = {

    # IpIntelligence based searches 
    "000": {
        "filter": S(ip__exact="8.8.8.8"), 
        "time_range_filter": S(),
        "expected": True,
        "entity": IpIntelligence,
        "followups": {},
        "show_results": False,
    },
    "001": {
        "filter": S(ip__exact="1.1.1.1"), 
        "time_range_filter": S(),
        "expected": True,
        "entity": IpIntelligence,
        "followups": {},
        "show_results": False,
    },
    "002": {
        "filter": S(ip__in={"8.8.8.8", "1.1.1.1"}), 
        "time_range_filter": S(),
        "expected": True,
        "entity": IpIntelligence,
        "followups": {},
        "show_results": False,
    },
    "003": {
        "filter": S(ip__iin={"8.8.8.8", "1.1.1.1"}), 
        "time_range_filter": S(),
        "expected": True,
        "entity": IpIntelligence,
        "followups": {},
        "show_results": False,
    },
    "004": {
        "filter": S(ip__exact="8.8.8.8") | S(ip__exact="1.1.1.1"), 
        "time_range_filter": S(),
        "expected": True,
        "entity": IpIntelligence,
        "followups": {},
        "show_results": False,
    },
    "005": {
        "filter": S(ip__exact="8.8.8.8") & S(ip__exact="1.1.1.1"), 
        "time_range_filter": S(),
        "expected": False,
        "entity": IpIntelligence,
        "followups": {},
        "show_results": False,
    },
    "006": {
        "filter": ~S(ip__exact="8.8.8.8"), 
        "time_range_filter": S(),
        "expected": False,
        "entity": IpIntelligence,
        "followups": {},
        "show_results": False,
    },
    "007": {
        "filter": S(ip__exact="2607:f8b0:4001:c17::65"), 
        "time_range_filter": S(),
        "expected": True,
        "entity": IpIntelligence,
        "followups": {},
        "show_results": True,
    },
    "008": {
        "filter": S(ip__iexact="2607:f8b0:4001:c17::65"), 
        "time_range_filter": S(),
        "expected": True,
        "entity": IpIntelligence,
        "followups": {},
        "show_results": True,
    },
} 