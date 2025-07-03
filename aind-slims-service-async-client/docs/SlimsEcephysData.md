# SlimsEcephysData

Expected Model that needs to be extracted from SLIMS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment_run_created_on** | **datetime** |  | [optional] 
**subject_id** | **str** |  | [optional] 
**operator** | **str** |  | [optional] 
**instrument** | **str** |  | [optional] 
**session_type** | **str** |  | [optional] 
**device_calibrations** | **int** |  | [optional] 
**mouse_platform_name** | **str** |  | [optional] 
**active_mouse_platform** | **bool** |  | [optional] 
**session_name** | **str** |  | [optional] 
**animal_weight_prior** | **str** |  | [optional] 
**animal_weight_after** | **str** |  | [optional] 
**animal_weight_unit** | **str** |  | [optional] 
**reward_consumed** | **str** |  | [optional] 
**reward_consumed_unit** | **str** |  | [optional] 
**stimulus_epochs** | **int** |  | [optional] 
**link_to_stimulus_epoch_code** | **str** |  | [optional] 
**reward_solution** | **str** |  | [optional] 
**other_reward_solution** | **str** |  | [optional] 
**reward_spouts** | [**List[EcephysRewardSpouts]**](EcephysRewardSpouts.md) |  | [optional] 
**stream_modalities** | **List[str]** |  | [optional] 
**stream_modules** | [**List[EcephysStreamModule]**](EcephysStreamModule.md) |  | [optional] 
**daq_names** | **List[str]** |  | [optional] 
**camera_names** | **List[str]** |  | [optional] 

## Example

```python
from aind_slims_service_async_client.models.slims_ecephys_data import SlimsEcephysData

# TODO update the JSON string below
json = "{}"
# create an instance of SlimsEcephysData from a JSON string
slims_ecephys_data_instance = SlimsEcephysData.from_json(json)
# print the JSON string representation of the object
print(SlimsEcephysData.to_json())

# convert the object into a dict
slims_ecephys_data_dict = slims_ecephys_data_instance.to_dict()
# create an instance of SlimsEcephysData from a dict
slims_ecephys_data_from_dict = SlimsEcephysData.from_dict(slims_ecephys_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


