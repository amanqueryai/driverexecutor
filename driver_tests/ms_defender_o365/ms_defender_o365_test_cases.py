
from qailib.search import S
from typing import Type, Any
from qai_ocsf_schema.objects import email, Device, Observable, Email
from qai_ocsf_schema.classes import Authentication 
from qai_ocsf_schema.classes.dev import EmailDeliveryActivity 
from qai_ocsf_schema.objects.dev import EmailAuth 
from masala.entity import Entity 
from qai_msgraph import translate_graph_search, translate_kql_search
import datetime

time_range_filter = S(time__gte=datetime.datetime(2024, 3, 1, 7, 55, 21, 260000, tzinfo=datetime.timezone.utc)) & S(
    time__lte=datetime.datetime(
        2024, 3, 7, 7, 55, 21, 260000, tzinfo=datetime.timezone.utc)
)


TEST_CASES: dict[str, dict[str, Any]] = {

    
} 