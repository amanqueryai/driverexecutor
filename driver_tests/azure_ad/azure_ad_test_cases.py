
from qailib.search import S
from typing import Type, Any
from qai_ocsf_schema.objects import User, Device, Observable, Email
from qai_ocsf_schema.classes import Authentication 
from qai_ocsf_schema.classes.dev import EmailDeliveryActivity 
from masala.entity import Entity 
from qai_msgraph import translate_graph_search, translate_kql_search
import datetime

time_range_filter = S(time__gte=datetime.datetime(2024, 3, 6, 7, 55, 21, 260000, tzinfo=datetime.timezone.utc)) & S(
    time__lte=datetime.datetime(
        2024, 3, 7, 7, 55, 21, 260000, tzinfo=datetime.timezone.utc)
)


TEST_CASES: dict[str, dict[str, Any]] = {

    # User searches 

    # NAME BASED PREDICATES
    "000": {
        "filter": S(),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "001": {
        "filter": S(name__contains="Emily"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "002": {
        "filter": S(name__contains="emily"),
        "time_range_filter": S(),
        "expected": False,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "003": {
        "filter": S(name__icontains="emily"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },


    "004": {
        "filter": S(name__exact="Emily@queryengineering.onmicrosoft.com"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "005": {
        "filter": S(name__exact="emily@queryengineering.onmicrosoft.com"),
        "time_range_filter": S(),
        "expected": False,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "006": {
        "filter": S(name__iexact="emily@queryengineering.onmicrosoft.com"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },

    "007": {
        "filter": S(name__startswith="emily"),
        "time_range_filter": S(),
        "expected": False,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "008": {
        "filter": S(name__startswith="Emily"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "009": {
        "filter": S(name__istartswith="EMILY"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },

    "010": {
        "filter": S(name__endswith="onmicrosoft.com"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "011": {
        "filter": S(name__endswith="onmicrosoft.COM"),
        "time_range_filter": S(),
        "expected": False,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "012": {
        "filter": S(name__iendswith="onmicrosoft.COM"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },

    "013": {
        "filter": S(name__in=frozenset(['Emily@queryengineering.onmicrosoft.com', 'Barbara@queryengineering.onmicrosoft.com'])),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "014": {
        "filter": S(name__in=frozenset(['emily@queryengineering.onmicrosoft.com', 'barbara@queryengineering.onmicrosoft.com'])),
        "time_range_filter": S(),
        "expected": False,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "015": {
        # "filter": S(name__iin=frozenset(['emily@queryengineering.onmicrosoft.com', 'barbara@queryengineering.onmicrosoft.com'])),
        "filter": S(name__iin=frozenset(['emily@queryengineering.onmicrosoft.com', 'barbara@queryengineering.onmicrosoft.com'])),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    
    "016": {
        "filter": S(name__gt="A"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "017": {
        "filter": S(name__gte="d"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "018": {
        "filter": S(name__lte="B"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "019": {
        "filter": S(name__lt="E"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },

    "020": {
        "filter": S(name__isnull=False),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "021": {
        "filter": S(name__isnull=True),
        "time_range_filter": S(),
        "expected": False,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    
    "022": {
        "filter": ~S(name__icontains="onmicrosoft"),
        "time_range_filter": S(),
        "expected": False,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "023": {
        "filter": ~S(name__icontains="barbara"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },

    "024": {
        "filter": S(name__startswith="Barbara") & S(name__endswith="com"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "025": {
        "filter": S(name__startswith="Barbara") & S(name__endswith="COM"),
        "time_range_filter": S(),
        "expected": False,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "026": {
        "filter": S(email_addr__istartswith="Barbara") & S(name__iendswith="COM"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    
    "027": {
        "filter": S(email_addr__startswith="barbara") | S(name__startswith="Emily"), 
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "028": {
        "filter": S(email_addr__gte="Emily"), 
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },


    # Device related searches
    "029": {
        "filter": S(), 
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "030": {
        "filter": S(hostname__exact="nbalakrishna-pc"), 
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "031": {
        "filter": S(hostname__iexact="nbalaKRishna-PC"), 
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "032": {
        "filter": S(name__exact="b441d933-2ce2-4b88-94c0-1ff585506cd1"), 
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "033": {
        "filter": S(uid__exact="24c12ad8-96c5-4c7b-b6f5-7107c2051abf"), 
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "034": {
        "filter": S(name__exact="b05b1337-90b2-4517-bbf3-1952c2d4c185"), 
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "035": {
        "filter": S(name__iexact="b441d933-2ce2-4B88-94C0-1ff585506cd1"), 
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    
    "036": {
        "filter": S(is_compliant__exact=False), 
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "037": {
        "filter": S(is_compliant__isnull=True), 
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": True, 
        "query_generator_callback": translate_graph_search, 
    },
    "038": {
        "filter": S(is_managed__exact=True), 
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "039": {
        "filter": ~S(is_compliant__exact=False), 
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "040": {
        "filter": ~S(hostname__exact="VM2-Windows10"), 
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },

    # Authentication Events 
    "041": {
        "filter": S(), 
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": Authentication,
        "followups": {
            "followup_filter": S(),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "042": {
        "filter": S(), 
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": Authentication,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.USER_NAME) & S(value__exact="mike@queryengineering.onmicrosoft.com"),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "043": {
        "filter": S(), 
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": Authentication,
        "followups": {
            "followup_filter": S(type_id__exact=Observable.TypeId.USER_NAME) & S(value__exact="dummyboy@queryengineering.onmicrosoft.com"),
            "type": Observable,
            "relationship": "observables",
        },
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },

    "044": {
        "filter": S(is_compliant__exact=False), 
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "045": {
        "filter": S(name__isnull=False), 
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },
    "046": {
        # "filter": S(name__iin=frozenset(['emily@queryengineering.onmicrosoft.com', 'barbara@queryengineering.onmicrosoft.com'])),
        "filter": S(name__iin={'emily@queryengineering.onmicrosoft.com', 'barbara@queryengineering.onmicrosoft.com'}),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False, 
        "query_generator_callback": translate_graph_search, 
    },

} 