
from qailib.search import S
from typing import Type, Any
from qai_ocsf_schema.objects import Observable
from qai_ocsf_schema.classes import SecurityFinding, ProcessActivity
from masala.entity import Entity
from qai_datadog.driver import translate_search, translate_observable_search 
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

    # SecurityFinding searches 
    "000": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__contains="query"),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "001": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": False,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__contains="QUERY"),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "002": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__icontains="QUERY"),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "003": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": False,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__exact="iris.query.ai"),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "004": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__exact="splunk2.sesandbox.query.ai"),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "005": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__iexact="Splunk2.sesandbox.query.ai"),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "006": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__startswith="splunk"),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "007": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": False,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__startswith="Splunk"),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "008": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__istartswith="splunk"),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "009": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__istartswith="Splunk"),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "010": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__endswith="ai"),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "011": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": False,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__endswith="Ai"),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "012": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__iendswith="ai"),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "013": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__iendswith="Ai"),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "014": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__in={"iris.query.ai", "splunk2.sesandbox.query.ai"}),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "015": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": False,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__in={"iris.query.ai"}),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "016": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__in={"splunk2.sesandbox.query.ai"}),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "017": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": False,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__in={"Splunk2.sesandbox.query.ai"}),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "018": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__iin={"Splunk2.sesandbox.query.ai"}),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "019": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__iin={"Iris.query.ai", "Splunk2.sesandbox.query.ai"}),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "020": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__gte="A"),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "021": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": False,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__gte="t"),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "022": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": False,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__lte="p"),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "023": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__isnull=False),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "024": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": False,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__isnull=True),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "025": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": (S(value__startswith="splunk") & S(type_id__exact=Observable.TypeId.HOSTNAME)) | (S(value__contains="query") & S(type_id__exact=Observable.TypeId.HOSTNAME)),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "026": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": (S(value__startswith="splunk") & S(type_id__exact=Observable.TypeId.HOSTNAME)) & (S(type_id__exact=Observable.TypeId.HOSTNAME) & S(value__contains="query")),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "027": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": False,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": (S(value__startswith="abc") & S(type_id__exact=Observable.TypeId.HOSTNAME)) | (S(value__contains="lll") & S(type_id__exact=Observable.TypeId.HOSTNAME)),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "028": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": (S(value__startswith="splunk") & S(type_id__exact=Observable.TypeId.HOSTNAME)) | (S(value__contains="lll") & S(type_id__exact=Observable.TypeId.HOSTNAME)),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "029": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.HOSTNAME) & ~S(value__contains="query"), 
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
    "030": {
        "filter": S(message__contains="CPU"),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {},
        "show_results": False,
        "query_generator_callback": translate_search,
        "callback_params":  {},
    },
    "031": {
        "filter": S(message__contains="XYZ"),
        "time_range_filter": time_range_filter,
        "expected": False,
        "entity": SecurityFinding,
        "followups": {},
        "show_results": False,
        "query_generator_callback": translate_search,
        "callback_params":  {},
    },
    "032": {
        "filter": S(severity_id__exact=SecurityFinding.SeverityId.INFORMATIONAL),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {},
        "show_results": False,
        "query_generator_callback": translate_search,
        "callback_params":  {},
    },
    "033": {
        "filter": S(severity_id__exact=SecurityFinding.SeverityId.CRITICAL),
        "time_range_filter": time_range_filter,
        "expected": False,
        "entity": SecurityFinding,
        "followups": {},
        "show_results": False,
        "query_generator_callback": translate_search,
        "callback_params":  {},
    },
    "034": {
        "filter": S(severity_id__in={SecurityFinding.SeverityId.CRITICAL}),
        "time_range_filter": time_range_filter,
        "expected": False,
        "entity": SecurityFinding,
        "followups": {},
        "show_results": False,
        "query_generator_callback": translate_search,
        "callback_params":  {},
    },
    "035": {
        "filter": S(severity_id__in={SecurityFinding.SeverityId.CRITICAL, SecurityFinding.SeverityId.INFORMATIONAL}),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {},
        "show_results": False,
        "query_generator_callback": translate_search,
        "callback_params":  {},
    },
    "036": {
        "filter": S(status_id__exact=SecurityFinding.StatusId.UNKNOWN),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {},
        "show_results": False,
        "query_generator_callback": translate_search,
        "callback_params":  {},
    },
    "037": {
        "filter": S(status_id__exact=SecurityFinding.StatusId.SUCCESS) | S(message__contains='CPU'),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {},
        "show_results": False,
        "query_generator_callback": translate_search,
        "callback_params":  {},
    },
    "038": {
        "filter": S(status_id__exact=SecurityFinding.StatusId.SUCCESS) | S(message__contains='SOMETHING RANDOM'),
        "time_range_filter": time_range_filter,
        "expected": False,
        "entity": SecurityFinding,
        "followups": {},
        "show_results": False,
        "query_generator_callback": translate_search,
        "callback_params":  {},
    },
    "039": {
        "filter": S(status_id__exact=SecurityFinding.StatusId.UNKNOWN) & S(message__contains='CPU'),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": SecurityFinding,
        "followups": {},
        "show_results": False,
        "query_generator_callback": translate_search,
        "callback_params":  {},
    },
    "040": {
        "filter": S(status_id__exact=SecurityFinding.StatusId.UNKNOWN) & S(message__contains='SOMETHING RANDOM'),
        "time_range_filter": time_range_filter,
        "expected": False,
        "entity": SecurityFinding,
        "followups": {},
        "show_results": False,
        "query_generator_callback": translate_search,
        "callback_params":  {},
    },

    # ProcessActivity
    "041": {
        "filter": S(),
        "time_range_filter": time_range_filter_process_activity,
        "expected": True,
        "entity": ProcessActivity,
        "followups": {
            "followup_filter": S(value__contains="query") & S(type_id__exact=Observable.TypeId.HOSTNAME), 
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": True,
        "query_generator_callback": translate_observable_search,
        "callback_params":  {},
    },
} 