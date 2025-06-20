# aind_slims_service_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aind_instrument**](DefaultApi.md#get_aind_instrument) | **GET** /aind_instruments/{input_id} | Get Aind Instrument
[**get_ecephys_sessions**](DefaultApi.md#get_ecephys_sessions) | **GET** /ecephys_sessions | Get Ecephys Sessions
[**get_histology_data**](DefaultApi.md#get_histology_data) | **GET** /histology | Get Histology Data
[**get_smartspim_imaging**](DefaultApi.md#get_smartspim_imaging) | **GET** /smartspim_imaging | Get Smartspim Imaging
[**get_water_restriction_data**](DefaultApi.md#get_water_restriction_data) | **GET** /water_restriction | Get Water Restriction Data


# **get_aind_instrument**
> List[Dict[str, object]] get_aind_instrument(input_id, partial_match=partial_match)

Get Aind Instrument

## AIND instrument metadata
Retrieves AIND Instrument information from SLIMS.

### Example


```python
import aind_slims_service_client
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
    input_id = 'input_id_example' # str | Instrument ID
    partial_match = False # bool | If true, will search for a partial match that contains the input_id string (optional) (default to False)

    try:
        # Get Aind Instrument
        api_response = api_instance.get_aind_instrument(input_id, partial_match=partial_match)
        print("The response of DefaultApi->get_aind_instrument:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_aind_instrument: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_id** | **str**| Instrument ID | 
 **partial_match** | **bool**| If true, will search for a partial match that contains the input_id string | [optional] [default to False]

### Return type

**List[Dict[str, object]]**

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

# **get_histology_data**
> List[SlimsHistologyData] get_histology_data(subject_id=subject_id, start_date_gte=start_date_gte, end_date_lte=end_date_lte)

Get Histology Data

## Histology metadata
Retrieves histology information from SLIMS.

### Example


```python
import aind_slims_service_client
from aind_slims_service_client.models.slims_histology_data import SlimsHistologyData
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
    subject_id = 'subject_id_example' # str | Subject ID (optional)
    start_date_gte = 'start_date_gte_example' # str | Date performed on or after. (ISO format) (optional)
    end_date_lte = 'end_date_lte_example' # str | Date performed on or before. (ISO format) (optional)

    try:
        # Get Histology Data
        api_response = api_instance.get_histology_data(subject_id=subject_id, start_date_gte=start_date_gte, end_date_lte=end_date_lte)
        print("The response of DefaultApi->get_histology_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_histology_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id** | **str**| Subject ID | [optional] 
 **start_date_gte** | **str**| Date performed on or after. (ISO format) | [optional] 
 **end_date_lte** | **str**| Date performed on or before. (ISO format) | [optional] 

### Return type

[**List[SlimsHistologyData]**](SlimsHistologyData.md)

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

# **get_smartspim_imaging**
> List[SlimsSpimData] get_smartspim_imaging(subject_id=subject_id, start_date_gte=start_date_gte, end_date_lte=end_date_lte)

Get Smartspim Imaging

## SmartSPIM imaging metadata
Retrieves SmartSPIM imaging information from SLIMS.

### Example


```python
import aind_slims_service_client
from aind_slims_service_client.models.slims_spim_data import SlimsSpimData
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
    subject_id = 'subject_id_example' # str | Subject ID (optional)
    start_date_gte = 'start_date_gte_example' # str | Date performed on or after. (ISO format) (optional)
    end_date_lte = 'end_date_lte_example' # str | Date performed on or before. (ISO format) (optional)

    try:
        # Get Smartspim Imaging
        api_response = api_instance.get_smartspim_imaging(subject_id=subject_id, start_date_gte=start_date_gte, end_date_lte=end_date_lte)
        print("The response of DefaultApi->get_smartspim_imaging:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_smartspim_imaging: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id** | **str**| Subject ID | [optional] 
 **start_date_gte** | **str**| Date performed on or after. (ISO format) | [optional] 
 **end_date_lte** | **str**| Date performed on or before. (ISO format) | [optional] 

### Return type

[**List[SlimsSpimData]**](SlimsSpimData.md)

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

# **get_water_restriction_data**
> List[SlimsWaterRestrictionData] get_water_restriction_data(subject_id=subject_id, start_date_gte=start_date_gte, end_date_lte=end_date_lte)

Get Water Restriction Data

## Water Restriction data
Retrieves water restriction information from SLIMS.

### Example


```python
import aind_slims_service_client
from aind_slims_service_client.models.slims_water_restriction_data import SlimsWaterRestrictionData
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
    subject_id = 'subject_id_example' # str | Subject ID (optional)
    start_date_gte = 'start_date_gte_example' # str | Date performed on or after. (ISO format) (optional)
    end_date_lte = 'end_date_lte_example' # str | Date performed on or before. (ISO format) (optional)

    try:
        # Get Water Restriction Data
        api_response = api_instance.get_water_restriction_data(subject_id=subject_id, start_date_gte=start_date_gte, end_date_lte=end_date_lte)
        print("The response of DefaultApi->get_water_restriction_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_water_restriction_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id** | **str**| Subject ID | [optional] 
 **start_date_gte** | **str**| Date performed on or after. (ISO format) | [optional] 
 **end_date_lte** | **str**| Date performed on or before. (ISO format) | [optional] 

### Return type

[**List[SlimsWaterRestrictionData]**](SlimsWaterRestrictionData.md)

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

