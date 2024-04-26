# Roles

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the role. | [optional] 
**name** | **str** | Name of the role. | [optional] 
**icon** | **str** | The role&#x27;s icon. | [optional] 
**description** | **str** | Description of the role. | [optional] 
**ip_access** | **list[str]** | Array of IP addresses that are allowed to connect to the API as a user of this role. | [optional] 
**enforce_tfa** | **bool** | Whether or not this role enforces the use of 2FA. | [optional] 
**admin_access** | **bool** | Admin role. If true, skips all permission checks. | [optional] 
**app_access** | **bool** | The users in the role are allowed to use the app. | [optional] 
**users** | **list[OneOfRolesUsersItems]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

