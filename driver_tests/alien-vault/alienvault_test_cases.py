
from qailib.search import S
from typing import Any
from qai_ocsf_schema.objects import Reputation 
from qai_ocsf_schema.objects.query import ThreatIntelligence
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

    # ThreatIntelligence searches with reputation followups  
    "000": {
        "filter": S(value="c0202cf6aeab8437c638533d14563d35") & S(type_id=ThreatIntelligence.TypeId.HASH),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": ThreatIntelligence,
        "followups": {
            "followup_filter": S(),
            "type": Reputation,
            "relationship": "reputation",
        },
        "show_results": True,
    },

    # Reputation based searches 
    "001": {
        "filter": S(raw_data__indicator="c0202cf6aeab8437c638533d14563d35") & S(provider="AlienVault"),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": Reputation,
        "followups": {},
        "show_results": True,
    },
} 