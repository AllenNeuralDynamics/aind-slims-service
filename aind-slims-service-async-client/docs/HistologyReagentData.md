# HistologyReagentData

Expected reagent information from SLIMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**lot_number** | **str** |  | [optional] 

## Example

```python
from aind_slims_service_async_client.models.histology_reagent_data import HistologyReagentData

# TODO update the JSON string below
json = "{}"
# create an instance of HistologyReagentData from a JSON string
histology_reagent_data_instance = HistologyReagentData.from_json(json)
# print the JSON string representation of the object
print(HistologyReagentData.to_json())

# convert the object into a dict
histology_reagent_data_dict = histology_reagent_data_instance.to_dict()
# create an instance of HistologyReagentData from a dict
histology_reagent_data_from_dict = HistologyReagentData.from_dict(histology_reagent_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


