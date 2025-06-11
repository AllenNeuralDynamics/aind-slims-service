# EcephysRewardSpouts

Expected Reward Spouts information from SLIMS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spout_side** | **str** |  | [optional] 
**starting_position** | **str** |  | [optional] 
**variable_position** | **bool** |  | [optional] 

## Example

```python
from aind_slims_service_client.models.ecephys_reward_spouts import EcephysRewardSpouts

# TODO update the JSON string below
json = "{}"
# create an instance of EcephysRewardSpouts from a JSON string
ecephys_reward_spouts_instance = EcephysRewardSpouts.from_json(json)
# print the JSON string representation of the object
print(EcephysRewardSpouts.to_json())

# convert the object into a dict
ecephys_reward_spouts_dict = ecephys_reward_spouts_instance.to_dict()
# create an instance of EcephysRewardSpouts from a dict
ecephys_reward_spouts_from_dict = EcephysRewardSpouts.from_dict(ecephys_reward_spouts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


