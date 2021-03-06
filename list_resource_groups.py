from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.resource import ResourceManagementClient
import os


os.environ['AZURE_AUTH_LOCATION'] = os.path.expanduser('~/.azure/sp_keys/readonly.json')
client = get_client_from_auth_file(ResourceManagementClient)

for rg in client.resource_groups.list():
    # print(rg)
    print('Name: ', rg.name)
    print('Type: ', rg.type)
    print('Location: ', rg.location)
    print('Managed By: ', rg.managed_by)
    print('ID: ', rg.id)
    print('Tags: ', rg.tags)
    print('Properties: ', rg.properties)
    print('Additional Properties: ', rg.additional_properties)
    print('\n')
