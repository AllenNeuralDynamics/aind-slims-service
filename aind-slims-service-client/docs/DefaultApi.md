# aind_slims_service_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ecephys_sessions**](DefaultApi.md#get_ecephys_sessions) | **GET** /ecephys_sessions | Get Ecephys Sessions


# **get_ecephys_sessions**
> List[SlimsEcephysData] get_ecephys_sessions(subject_id=subject_id, session_name=session_name, start_date_gte=start_date_gte, end_date_lte=end_date_lte)

Get Ecephys Sessions

## Ecephys session metadata
Retrieves Ecephys session information from SLIMS.

### Example


```python
import aind_slims_service_client
from aind_slims_service_client.models.slims_ecephys_data import SlimsEcephysData
from aind_slims_service_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aind_slims_service_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with aind_slims_service_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aind_slims_service_client.DefaultApi(api_client)
    subject_id = 'subject_id_example' # str |  (optional)
    session_name = 'session_name_example' # str | Name of the session (optional)
    start_date_gte = 'start_date_gte_example' # str | Experiment run created on or after. (ISO format) (optional)
    end_date_lte = 'end_date_lte_example' # str | Experiment run created on or before. (ISO format) (optional)

    try:
        # Get Ecephys Sessions
        api_response = api_instance.get_ecephys_sessions(subject_id=subject_id, session_name=session_name, start_date_gte=start_date_gte, end_date_lte=end_date_lte)
        print("The response of DefaultApi->get_ecephys_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_ecephys_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id** | **str**|  | [optional] 
 **session_name** | **str**| Name of the session | [optional] 
 **start_date_gte** | **str**| Experiment run created on or after. (ISO format) | [optional] 
 **end_date_lte** | **str**| Experiment run created on or before. (ISO format) | [optional] 

### Return type

[**List[SlimsEcephysData]**](SlimsEcephysData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

