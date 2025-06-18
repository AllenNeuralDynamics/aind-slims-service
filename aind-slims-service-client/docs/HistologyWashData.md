# HistologyWashData

Expected wash information from SLIMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wash_name** | **str** |  | [optional] 
**wash_type** | **str** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**modified_by** | **str** |  | [optional] 
**reagents** | [**List[HistologyReagentData]**](HistologyReagentData.md) |  | [optional] [default to []]
**mass** | **str** |  | [optional] 

## Example

```python
from aind_slims_service_client.models.histology_wash_data import HistologyWashData

# TODO update the JSON string below
json = "{}"
# create an instance of HistologyWashData from a JSON string
histology_wash_data_instance = HistologyWashData.from_json(json)
# print the JSON string representation of the object
print(HistologyWashData.to_json())

# convert the object into a dict
histology_wash_data_dict = histology_wash_data_instance.to_dict()
# create an instance of HistologyWashData from a dict
histology_wash_data_from_dict = HistologyWashData.from_dict(histology_wash_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


