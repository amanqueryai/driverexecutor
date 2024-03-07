
from qailib.search import S
from typing import Type, Any
from qai_ocsf_schema.objects import User, Device 
from masala.entity import Entity 
import datetime

time_range_filter = S(time__gte=datetime.datetime(2024, 2, 24, 7, 55, 21, 260000, tzinfo=datetime.timezone.utc)) & S(
    time__lte=datetime.datetime(
        2024, 2, 25, 7, 55, 21, 260000, tzinfo=datetime.timezone.utc)
)

TEST_CASES: dict[str, dict[str, Any]] = {

    # User searches 
    "000": {
        "filter": S(name__contains="mahesh"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {} 
    },
    "001": {
        "filter": S(name__contains="MAhesh"),
        "time_range_filter": S(),
        "expected": False,
        "entity": User,
        "followups": {} 
    },
    "002": {
        "filter": S(name__icontains="MAhesh"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {} 
    },
    
    "003": {
        "filter": S(email_addr__contains="mahesh"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {} 
    },
    "004": {
        "filter": S(email_addr__contains="MAhesh"),
        "time_range_filter": S(),
        "expected": False,
        "entity": User,
        "followups": {} 
    },
    "005": {
        "filter": S(email_addr__icontains="MAhesh"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {} 
    },
    
    "006": {
        "filter": S(email_addr__exact="mahesh@query.ai"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {} 
    },
    "007": {
        "filter": S(email_addr__exact="MAhesh@query.ai"),
        "time_range_filter": S(),
        "expected": False,
        "entity": User,
        "followups": {} 
    },
    "008": {
        "filter": S(email_addr__iexact="MAhesh@query.ai"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {} 
    },

    "009": {
        "filter": S(email_addr__startswith="mahesh"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {} 
    },
    "010": {
        "filter": S(email_addr__startswith="MAhesh"),
        "time_range_filter": S(),
        "expected": False,
        "entity": User,
        "followups": {} 
    },
    "011": {
        "filter": S(email_addr__istartswith="MAhesh"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {} 
    },
    
    "012": {
        "filter": S(email_addr__endswith="query.ai"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {} 
    },
    "013": {
        "filter": S(email_addr__endswith="query.aI"),
        "time_range_filter": S(),
        "expected": False,
        "entity": User,
        "followups": {} 
    },
    "014": {
        "filter": S(email_addr__iendswith="QUERY.AI"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {} 
    },
    
    "015": {
        "filter": S(email_addr__exact="mahesh@query.ai") & S(email_addr__endswith="query.ai"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {} 
    },
    "016": {
        "filter": S(email_addr__startswith="mahesh") | S(email_addr__endswith="query.ai"),
        "time_range_filter": S(),
        "expected": True,
        "entity": User,
        "followups": {} 
    },
    "017": {
        "filter": S(email_addr__exact="query.ai") & S(email_addr__endswith="query.ai"),
        "time_range_filter": S(),
        "expected": False,
        "entity": User,
        "followups": {} 
    },
    "018": {
        "filter": S(email_addr__startswith="MAhesh") | S(email_addr__endswith="Query.ai"),
        "time_range_filter": S(),
        "expected": False,
        "entity": User,
        "followups": {} 
    },

    # # Device searches 
    "019": {
        "filter": S(name__contains="mahesh"),
        "time_range_filter": S(),
        "expected": False,
        "entity": Device,
        "followups": {} 
    },
    "020": {
        "filter": S(name__contains="Mahesh"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {} 
    },
    "021": {
        "filter": S(name__icontains="MAhesH"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {} 
    },

    "022": {
        "filter": S(hostname__contains="mahesh"),
        "time_range_filter": S(),
        "expected": False,
        "entity": Device,
        "followups": {} 
    },
    "023": {
        "filter": S(hostname__contains="Mahesh"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {} 
    },
    "024": {
        "filter": S(hostname__icontains="MAhesH"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {} 
    },
    
    "025": {
        "filter": S(hostname__exact="Mahesh-MPB"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {} 
    },
    "026": {
        "filter": S(hostname__exact="mahesh-MPB"),
        "time_range_filter": S(),
        "expected": False,
        "entity": Device,
        "followups": {} 
    },
    "027": {
        "filter": S(hostname__iexact="MAhesH-MPB"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {} 
    },
    
    "028": {
        "filter": S(hostname__startswith="Mahesh"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {} 
    },
    "029": {
        "filter": S(hostname__startswith="mahesh"),
        "time_range_filter": S(),
        "expected": False,
        "entity": Device,
        "followups": {} 
    },
    "030": {
        "filter": S(hostname__istartswith="MAhesH"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {} 
    },

    "031": {
        "filter": S(hostname__endswith="MPB"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {} 
    },
    "032": {
        "filter": S(hostname__endswith="mpb"),
        "time_range_filter": S(),
        "expected": False,
        "entity": Device,
        "followups": {} 
    },
    "033": {
        "filter": S(hostname__iendswith="MPb"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {} 
    },

    "034": {
        "filter": S(hostname__endswith="MPB") & S(hostname__startswith="Mahesh"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {} 
    },
    "035": {
        "filter": S(hostname__endswith="mpb") & S(hostname__istartswith="Mahesh"),
        "time_range_filter": S(),
        "expected": False,
        "entity": Device,
        "followups": {} 
    },
    "036": {
        "filter": S(hostname__endswith="mpb") | S(hostname__istartswith="Mahesh"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {} 
    },
    "037": {
        "filter": S(hostname__endswith="mpb") | S(hostname__istartswith="ahesh"),
        "time_range_filter": S(),
        "expected": False,
        "entity": Device,
        "followups": {} 
    },
    "038": {
        "filter": S(S(hostname__endswith="mpb") | S(hostname__istartswith="ahesh")) | S(hostname__endswith="MPB"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {} 
    },
    "039": {
        "filter": S(S(hostname__endswith="mpb") | S(hostname__istartswith="ahesh")) | S(hostname__endswith="MPb"),
        "time_range_filter": S(),
        "expected": False,
        "entity": Device,
        "followups": {} 
    },
    "040": {
        "filter": S(S(hostname__endswith="mpb") | S(hostname__istartswith="ahesh")) | S(hostname__iendswith="MPb"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {} 
    },
    "041": {
        "filter": S(S(hostname__endswith="mpb") | S(hostname__istartswith="ahesh")) | ~S(hostname__endswith="MPb"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {} 
    },

    "042": {
        "filter": ~S(hostname__iendswith="MPB"),
        "time_range_filter": S(),
        "expected": False,
        "entity": Device,
        "followups": {} 
    },
    "043": {
        "filter": ~S(hostname__exact="Mahesh-MB"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {} 
    },
    
    "044": {
        "filter": S(hostname__gte="A"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {} 
    },
    "045": {
        "filter": S(hostname__lte="z"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {} 
    },
    
    "046": {
        "filter": S(ip__exact="192.168.1.10"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {} 
    },
    "047": {
        "filter": S(ip__exact="192.168.1.10") | S(hostname__startswith="Mahesh"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {} 
    },
    "048": {
        "filter": S(ip__exact="192.168.1.10") & S(hostname__startswith="mahesh"),
        "time_range_filter": S(),
        "expected": False,
        "entity": Device,
        "followups": {} 
    },
    "049": {
        "filter": S(ip__exact="192.168.1.10") & S(hostname__startswith="Mahesh"),
        "time_range_filter": S(),
        "expected": True,
        "entity": Device,
        "followups": {} 
    },
    "050": {
        "filter": S(ip__exact="192.168.1.1") | S(hostname__istartswith="ahesh"),
        "time_range_filter": S(),
        "expected": False,
        "entity": Device,
        "followups": {} 
    },
} 