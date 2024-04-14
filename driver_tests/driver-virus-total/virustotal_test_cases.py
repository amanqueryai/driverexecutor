
from qailib.search import S
from typing import Any
from qai_ocsf_schema.objects import Fingerprint, Url, DomainInfo, File, ThreatIntelligence 
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

    # DomainInfo searches with reputation followups  
    "000": {
        "filter": S(domain__exact="google.com"),
        "time_range_filter": S(),
        "expected": True,
        "entity": DomainInfo,
        "followups": {},
        "show_results": False,
    },
    "001": {
        "filter": S(domain__iexact="GOOGLE.cOm"),
        "time_range_filter": S(),
        "expected": True,
        "entity": DomainInfo,
        "followups": {},
        "show_results": False,
    },
    "002": {
        "filter": S(registrar__exact='MarkMonitor Inc.'),
        "time_range_filter": S(),
        "expected": True,
        "entity": DomainInfo,
        "followups": {},
        "show_results": False,
    },
    "003": {
        "filter": S(domain__in={"google.com", "microsoft.com"}),
        "time_range_filter": S(),
        "expected": True,
        "entity": DomainInfo,
        "followups": {},
        "show_results": False,
    },
    "004": {
        "filter": S(domain__in={"google.com", "zzzdjjjdjdjdjdjd.com"}),
        "time_range_filter": S(),
        "expected": True,
        "entity": DomainInfo,
        "followups": {},
        "show_results": False,
    },
    "005": {
        "filter": S(domain__in={"zzzdjjjdjdjdjdjd123.com"}),
        "time_range_filter": S(),
        "expected": False,
        "entity": DomainInfo,
        "followups": {},
        "show_results": False,
    },
    "006": {
        "filter": S(domain__iin={"google.Com", "MicRosoft.com"}),
        "time_range_filter": S(),
        "expected": True,
        "entity": DomainInfo,
        "followups": {},
        "show_results": False,
    },
    "007": {
        "filter": S(domain__exact="google.com") | S(domain__exact="microsoft.com"),
        "time_range_filter": S(),
        "expected": True,
        "entity": DomainInfo,
        "followups": {},
        "show_results": False,
    },
    "008": {
        "filter": S(domain__exact="google.com") & S(domain__exact="microsoft.com"),
        "time_range_filter": S(),
        "expected": False,
        "entity": DomainInfo,
        "followups": {},
        "show_results": False,
    },

    # Url Searches
    "009": {
        "filter": S(text__exact="https://google.com"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Url,
        "followups": {},
        "show_results": False,
    },
    "010": {
        "filter": S(text__iexact="https://GOOGLE.com"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Url,
        "followups": {},
        "show_results": False,
    },
    "011": {
        "filter": S(text__in={"https://GOOGLE.com", "https://microsoft.com"}),
        "time_range_filter": S(),
        "expected": True,
        "entity": Url,
        "followups": {},
        "show_results": False,
    },
    "012": {
        "filter": S(text__iin={"https://GOOGLE.com", "https://MICROSOFT.com"}),
        "time_range_filter": S(),
        "expected": True,
        "entity": Url,
        "followups": {},
        "show_results": False,
    },
    "013": {
        "filter": S(text__exact="https://google.com") | S(text__exact="https://microsoft.com"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Url,
        "followups": {},
        "show_results": False,
    },
    "014": {
        "filter": S(text__exact="https://google.com") & S(text__exact="https://microsoft.com"),
        "time_range_filter": S(),
        "expected": False,
        "entity": Url,
        "followups": {},
        "show_results": False,
    },

    # File searches
    "015": {
        "filter": S(),
        "time_range_filter": S(),
        "expected": True,
        "entity": File,
        "followups": {
            "followup_filter": S(value__exact="fb55414848281f804858ce188c3dc659d129e283bd62d58d34f6e6f568feab37"),
            "type": Fingerprint, 
            "relationship": "fingerprints", 
        },
        "show_results": False,
    },
    "016": {
        "filter": S(),
        "time_range_filter": S(),
        "expected": True,
        "entity": File,
        "followups": {
            "followup_filter": S(value__exact="61104e2ae6c12556124680a067a454628e71a9e33e2958088c4e392541099e9f"),
            "type": Fingerprint, 
            "relationship": "fingerprints", 
        },
        "show_results": False,
    },
    "017": {
        "filter": S(),
        "time_range_filter": S(),
        "expected": False,
        "entity": File,
        "followups": {
            "followup_filter": S(value__exact="xxxx"),
            "type": Fingerprint, 
            "relationship": "fingerprints", 
        },
        "show_results": False,
    },
    "018": {
        "filter": S(),
        "time_range_filter": S(),
        "expected": True,
        "entity": File,
        "followups": {
            "followup_filter": S(value__iexact="61104E2ae6c12556124680a067a454628e71a9e33e2958088c4e392541099e9F"),
            "type": Fingerprint, 
            "relationship": "fingerprints", 
        },
        "show_results": False,
    },
    "019": {
        "filter": S(),
        "time_range_filter": S(),
        "expected": True,
        "entity": File,
        "followups": {
            "followup_filter": S(value__exact="61104E2ae6c12556124680a067a454628e71a9e33e2958088c4e392541099e9F") | S(value__exact="fb55414848281f804858ce188c3dc659d129e283bd62d58d34f6e6f568feab37"),
            "type": Fingerprint, 
            "relationship": "fingerprints", 
        },
        "show_results": False,
    },
    "020": {
        "filter": S(),
        "time_range_filter": S(),
        "expected": False,
        "entity": File,
        "followups": {
            "followup_filter": S(value__exact="61104E2ae6c12556124680a067a454628e71a9e33e2958088c4e392541099e9F") & S(value__exact="fb55414848281f804858ce188c3dc659d129e283bd62d58d34f6e6f568feab37"),
            "type": Fingerprint, 
            "relationship": "fingerprints", 
        },
        "show_results": False,
    },
    "021": {
        "filter": S(type_id__exact=ThreatIntelligence.TypeId.HASH) & S(value__exact="fb55414848281f804858ce188c3dc659d129e283bd62d58d34f6e6f568feab37"),
        "time_range_filter": S(),
        "expected": True,
        "entity": ThreatIntelligence,
        "followups": {},
        "show_results": False,
    },
    "022": {
        "filter": S(type_id__exact=ThreatIntelligence.TypeId.DOMAIN) & S(value__in={"amazon.com", "google.com"}),
        "time_range_filter": S(),
        "expected": True,
        "entity": ThreatIntelligence,
        "followups": {},
        "show_results": False,
    },
    "023": {
        "filter": S(type_id__exact=ThreatIntelligence.TypeId.IP) & S(value__exact="8.8.8.8"),
        "time_range_filter": S(),
        "expected": True,
        "entity": ThreatIntelligence,
        "followups": {},
        "show_results": False,
    },
    "024": {
        "filter": S(type_id__exact=ThreatIntelligence.TypeId.URL) & S(value__exact="https://microsoft.com"),
        "time_range_filter": S(),
        "expected": True,
        "entity": ThreatIntelligence,
        "followups": {},
        "show_results": True,
    },
    "025": {
        "filter": S(domain__startswith="google"),
        "time_range_filter": S(),
        "expected": False,
        "entity": DomainInfo,
        "followups": {},
        "show_results": False,
    },
    "026": {
        "filter": S(domain__isnull=True),
        "time_range_filter": S(),
        "expected": False,
        "entity": DomainInfo,
        "followups": {},
        "show_results": False,
    },
    "027": {
        "filter": S(text__gte="A"),
        "time_range_filter": S(),
        "expected": False,
        "entity": Url,
        "followups": {},
        "show_results": False,
    },
    "028": {
        "filter": ~S(text__exact="https://google.com"),
        "time_range_filter": S(),
        "expected": False,
        "entity": Url,
        "followups": {},
        "show_results": False,
    },
    "029": {
        "filter": S(type_id__exact=ThreatIntelligence.TypeId.DOMAIN) & S(value__iexact="amazon.com") | S(type_id__exact=ThreatIntelligence.TypeId.DOMAIN) & S(value__iexact="microsoft.com"),
        "time_range_filter": S(),
        "expected": True,
        "entity": ThreatIntelligence,
        "followups": {},
        "show_results": True,
    },

} 
