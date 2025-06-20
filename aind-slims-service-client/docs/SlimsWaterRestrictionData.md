# SlimsWaterRestrictionData

Expected Model that needs to be extracted from SLIMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_event_created_on** | **datetime** |  | [optional] 
**subject_id** | **str** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**assigned_by** | **str** |  | [optional] 
**target_weight_fraction** | **str** |  | [optional] 
**baseline_weight** | **str** |  | [optional] 
**weight_unit** | **str** |  | [optional] 

## Example

```python
from aind_slims_service_client.models.slims_water_restriction_data import SlimsWaterRestrictionData

# TODO update the JSON string below
json = "{}"
# create an instance of SlimsWaterRestrictionData from a JSON string
slims_water_restriction_data_instance = SlimsWaterRestrictionData.from_json(json)
# print the JSON string representation of the object
print(SlimsWaterRestrictionData.to_json())

# convert the object into a dict
slims_water_restriction_data_dict = slims_water_restriction_data_instance.to_dict()
# create an instance of SlimsWaterRestrictionData from a dict
slims_water_restriction_data_from_dict = SlimsWaterRestrictionData.from_dict(slims_water_restriction_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


