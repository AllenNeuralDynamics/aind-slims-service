# SlimsHistologyData

Expected Model that needs to be extracted from SLIMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**procedure_name** | **str** |  | [optional] 
**experiment_run_created_on** | **datetime** |  | [optional] 
**specimen_id** | **str** |  | [optional] 
**subject_id** | **str** |  | [optional] 
**protocol_id** | **str** |  | [optional] 
**protocol_name** | **str** |  | [optional] 
**washes** | [**List[HistologyWashData]**](HistologyWashData.md) |  | [optional] [default to []]

## Example

```python
from aind_slims_service_client.models.slims_histology_data import SlimsHistologyData

# TODO update the JSON string below
json = "{}"
# create an instance of SlimsHistologyData from a JSON string
slims_histology_data_instance = SlimsHistologyData.from_json(json)
# print the JSON string representation of the object
print(SlimsHistologyData.to_json())

# convert the object into a dict
slims_histology_data_dict = slims_histology_data_instance.to_dict()
# create an instance of SlimsHistologyData from a dict
slims_histology_data_from_dict = SlimsHistologyData.from_dict(slims_histology_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


