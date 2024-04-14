
from qailib.search import S
from typing import Any
from qai_ocsf_schema.classes import Authentication 
from qai_ocsf_schema.objects import User, Device, Observable
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
    "000": {
        "filter": S(email_addr__contains="query"), 
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False,
    },
    "001": {
        "filter": S(email_addr__exact='aman@query.ai'),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False,
    },
    "002": {
        "filter": S(email_addr__contains='aman'),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False,
    },
    "003": {
        "filter": S(email_addr__startswith='aman'),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False,
    },
    "004": {
        "filter": S(email_addr__endswith='query.ai'),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False,
    },
    "005": {
        "filter": S(email_addr__gte='a'),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False,
    },
    "006": {
        "filter": S(email_addr__lte='z'),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False,
    },
    "007": {
        "filter": ~S(email_addr__exact='aman@query.ai'),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False,
    },
    
    "008": {
        "filter": S(uid__exact='112435548293798255772'),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False,
    },
    "009": {
        "filter": S(email_addr__in={'aman@query.ai', 'aman77707@gmail.com'}),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False,
    },
    "010": {
        "filter": S(email_addr__in={'aman@query.ai', 'aman77707@gmail.com'}) | S(email_addr__exact="avnish@query.ai"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False,
    },
    "011": {
        "filter": S(uid__exact='112435548293798255772') | S(email_addr__exact="avnish@query.ai"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False,
    },
    "012": {
        "filter": S(name__exact='google-apps|avnish@query.ai') & S(email_addr__exact="avnish@query.ai"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {},
        "show_results": False,
    },

    # Device based searches
    "013": {
        "filter": S(hostname__exact="auth.test.query.ai"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False,
    },
    "014": {
        "filter": S(hostname__contains='.query.ai'),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False,
    },
    "015": {
        "filter": S(hostname__startswith='auth'),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False,
    },
    "016": {
        "filter": S(hostname__endswith='query.ai'),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False,
    },
    "017": {
        "filter": S(hostname__gte='A'),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False,
    },
    "018": {
        "filter": S(hostname__lte='z'),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False,
    },
    "019": {
        "filter": S(ip__exact='65.28.81.133'),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False,
    },
    "020": {
        "filter": ~S(hostname__exact='auth.test.query.ai'),
        "time_range_filter": S(),
        "expected": False,
        "entity": Device,
        "followups": {},
        "show_results": False,
    },
    "021": {
        "filter": S(type_id__exact=Device.TypeId.UNKNOWN),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False,
    },
    "022": {
        "filter": S(type_id__exact=Device.TypeId.UNKNOWN) | S(hostname__exact='auth.test.query.ai'),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False,
    },
    "023": {
        "filter": S(hostname__in={'auth.test.query.ai', "iris.query.ai"}),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False,
    },
    "024": {
        "filter": S(hostname__exact="auth.test.query.ai") & S(ip__exact='65.28.81.133'),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False,
    },
    "025": {
        "filter": S(hostname__exact="auth.query.ai") & S(ip__exact='65.28.81.133'),
        "time_range_filter": S(),
        "expected": False,
        "entity": Device,
        "followups": {},
        "show_results": False,
    },
    "026": {
        "filter": S(hostname__exact="auth.test.query") | S(ip__exact='65.28.81.133'),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {},
        "show_results": False,
    },

    # Authentication based searches 
    "027": {
        "filter": S(),
        "time_range_filter": time_range_filter,
        "expected": True,
        "entity": Authentication,
        "followups": {

        },
        "show_results": True,
    },
} 