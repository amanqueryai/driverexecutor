### Overview
This is a rudimentary tool that helps you execute your test cases against a driver of your choice. All you need is to procure a test case and driver credentials. 
The tool supports you declare your test case with:
- Top-level filter with time filter
- Followup on the relationships
- Verify the platform query generated(if the platform supports it and the driver has it implemented) for your test case.

The tool has certain gaps which will be implemented eventually and soon.
- Support scaffolding to generate basic test files for the new drivers. Currently, you might have to copy `driver_name_test.py` and `driver_name_test_cases.py` file from other drivers and replace your credentials.
- The tool has missing environment configuration. In order to run the tool, you might have to keep the virtual environment active for the driver that is being tested from `masala` repository.
- Though boolean flags help in knowing if the results were received, it is often required to check the returned what was returned as the. Hence, a robust mechanism for verification of the results is not in place currently. 

### Test case parameters: 

- **filter**: This is the filter on the parent entity.
- **time_range_filter**: Time range filter that can be applied on events.
- **expected**: A boolean flag that indicates expected results. True meaning results are expected, False meaning the results are expected to be an empty list.
- **entity**: Name of the top-level OCSF type (Event or object).
- **followups** (Optional):
  - **followup_filter**: This is the filter on the followup entity's attribute, for example, a filter on Observable while fetching events.
  - **type**: Followup type, Ex Observable, Device etc.
  - **relationship**: Relationship name of the follow-up entity from top-level OCSF entity. For example observables in most of the cases for Observable in Events.
- **show_results**: For debugging purpose. Irrelevant/Ignore.
- **query_generator_callback** (Optional): The function callback object that is used to generate intermediate query before invoking API request. This helps in capturing respective generated query in the results.
- **callback_params** (Optional): Parameters that the query generator callback accepts. These paramters will be unpacked by the core test case executor.

### Example test case
    time_range_filter = S(time__gte=datetime.datetime(2024, 3, 6, 7, 55, 21, 260000, tzinfo=datetime.timezone.utc)) & S(
        time__lte=datetime.datetime(
            2024, 3, 7, 7, 55, 21, 260000, tzinfo=datetime.timezone.utc)
    )
    "test_case_id": {
        "filter": ~S(hostname__exact="VM2-Windows10"), 
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
        "callback_params": {},
    },
