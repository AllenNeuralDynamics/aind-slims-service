# SlimsViralMaterialData

Model for viral material data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_category** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**content_created_on** | **datetime** |  | [optional] 
**content_modified_on** | **datetime** |  | [optional] 
**viral_solution_type** | **str** |  | [optional] 
**virus_name** | **str** |  | [optional] 
**lot_number** | **str** |  | [optional] 
**lab_team** | **str** |  | [optional] 
**virus_type** | **str** |  | [optional] 
**virus_serotype** | **str** |  | [optional] 
**virus_plasmid_number** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**dose** | **str** |  | [optional] 
**dose_unit** | **str** |  | [optional] 
**titer** | **str** |  | [optional] 
**titer_unit** | **str** |  | [optional] 
**volume** | **str** |  | [optional] 
**volume_unit** | **str** |  | [optional] 
**date_made** | **datetime** |  | [optional] 
**intake_date** | **datetime** |  | [optional] 
**storage_temperature** | **str** |  | [optional] 
**special_storage_guidelines** | **List[str]** |  | [optional] 
**special_handling_guidelines** | **List[str]** |  | [optional] 
**parent_name** | **str** |  | [optional] 
**mix_count** | **int** |  | [optional] 
**derivation_count** | **int** |  | [optional] 
**ingredient_count** | **int** |  | [optional] 

## Example

```python
from aind_slims_service_async_client.models.slims_viral_material_data import SlimsViralMaterialData

# TODO update the JSON string below
json = "{}"
# create an instance of SlimsViralMaterialData from a JSON string
slims_viral_material_data_instance = SlimsViralMaterialData.from_json(json)
# print the JSON string representation of the object
print(SlimsViralMaterialData.to_json())

# convert the object into a dict
slims_viral_material_data_dict = slims_viral_material_data_instance.to_dict()
# create an instance of SlimsViralMaterialData from a dict
slims_viral_material_data_from_dict = SlimsViralMaterialData.from_dict(slims_viral_material_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


