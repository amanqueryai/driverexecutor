from qai_jamf.connector import JAMFConnector 
from qai_jamf.driver import JAMFDriver 
from jamf_test_cases import TEST_CASES as test_cases 
from typing import Any
from masala.drivers import BaseConnector, BaseDriver
import os
import sys

parent = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
parent_parent = os.path.dirname(parent)
sys.path.append(parent_parent)

from core_test_executor import TestAggregator


class TestReports:
    def __init__(self, configuration: dict[str, Any], connector_type: BaseConnector, driver_type: BaseDriver) -> None:
        connector = connector_type(**configuration) # type: ignore 
        self.driver = driver_type(connector) # type: ignore 

    def get_reports(self):
        aggregator = TestAggregator()
        results = aggregator.aggregate_test_cases(test_cases=test_cases , driver=self.driver)
        print("HELLO")

if __name__ == '__main__':
    configuration = {
    }


    tr = TestReports(configuration=configuration, connector_type=JAMFConnector, driver_type=JAMFDriver) # type: ignore
    tr.get_reports()

print("##### THE END ######")

