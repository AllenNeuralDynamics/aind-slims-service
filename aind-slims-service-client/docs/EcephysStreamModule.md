# EcephysStreamModule

Expected Stream module information from SLIMS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**implant_hole** | **int** |  | [optional] 
**assembly_name** | **str** |  | [optional] 
**probe_name** | **str** |  | [optional] 
**primary_target_structure** | **str** |  | [optional] 
**secondary_target_structures** | **List[object]** |  | [optional] 
**arc_angle** | **str** |  | [optional] 
**module_angle** | **str** |  | [optional] 
**rotation_angle** | **str** |  | [optional] 
**coordinate_transform** | **str** |  | [optional] 
**ccf_coordinate_ap** | **str** |  | [optional] 
**ccf_coordinate_ml** | **str** |  | [optional] 
**ccf_coordinate_dv** | **str** |  | [optional] 
**ccf_coordinate_unit** | **str** |  | [optional] 
**ccf_version** | **str** |  | [optional] 
**bregma_target_ap** | **str** |  | [optional] 
**bregma_target_ml** | **str** |  | [optional] 
**bregma_target_dv** | **str** |  | [optional] 
**bregma_target_unit** | **str** |  | [optional] 
**surface_z** | **str** |  | [optional] 
**surface_z_unit** | **str** |  | [optional] 
**manipulator_x** | **str** |  | [optional] 
**manipulator_y** | **str** |  | [optional] 
**manipulator_z** | **str** |  | [optional] 
**manipulator_unit** | **str** |  | [optional] 
**dye** | **str** |  | [optional] 

## Example

```python
from aind_slims_service_client.models.ecephys_stream_module import EcephysStreamModule

# TODO update the JSON string below
json = "{}"
# create an instance of EcephysStreamModule from a JSON string
ecephys_stream_module_instance = EcephysStreamModule.from_json(json)
# print the JSON string representation of the object
print(EcephysStreamModule.to_json())

# convert the object into a dict
ecephys_stream_module_dict = ecephys_stream_module_instance.to_dict()
# create an instance of EcephysStreamModule from a dict
ecephys_stream_module_from_dict = EcephysStreamModule.from_dict(ecephys_stream_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


