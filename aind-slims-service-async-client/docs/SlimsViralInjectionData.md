# SlimsViralInjectionData

\"Model for viral injection data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_category** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**content_created_on** | **datetime** |  | [optional] 
**content_modified_on** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**viral_injection_buffer** | **str** |  | [optional] 
**volume** | **str** |  | [optional] 
**volume_unit** | **str** |  | [optional] 
**labeling_protein** | **str** |  | [optional] 
**date_made** | **datetime** |  | [optional] 
**intake_date** | **datetime** |  | [optional] 
**storage_temperature** | **str** |  | [optional] 
**special_storage_guidelines** | **List[str]** |  | [optional] 
**special_handling_guidelines** | **List[str]** |  | [optional] 
**mix_count** | **int** |  | [optional] 
**derivation_count** | **int** |  | [optional] 
**ingredient_count** | **int** |  | [optional] 
**assigned_mice** | **List[str]** |  | [optional] 
**requested_for_date** | **int** |  | [optional] 
**planned_injection_date** | **datetime** |  | [optional] 
**planned_injection_time** | **datetime** |  | [optional] 
**order_created_on** | **datetime** |  | [optional] 
**viral_materials** | [**List[SlimsViralMaterialData]**](SlimsViralMaterialData.md) |  | [optional] 

## Example

```python
from aind_slims_service_async_client.models.slims_viral_injection_data import SlimsViralInjectionData

# TODO update the JSON string below
json = "{}"
# create an instance of SlimsViralInjectionData from a JSON string
slims_viral_injection_data_instance = SlimsViralInjectionData.from_json(json)
# print the JSON string representation of the object
print(SlimsViralInjectionData.to_json())

# convert the object into a dict
slims_viral_injection_data_dict = slims_viral_injection_data_instance.to_dict()
# create an instance of SlimsViralInjectionData from a dict
slims_viral_injection_data_from_dict = SlimsViralInjectionData.from_dict(slims_viral_injection_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


