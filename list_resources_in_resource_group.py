from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.resource import ResourceManagementClient
import os


os.environ['AZURE_AUTH_LOCATION'] = os.path.expanduser('~/.azure/sp_keys/readonly.json')
client = get_client_from_auth_file(ResourceManagementClient)

for rg in client.resource_groups.list():
    for item in client.resources.list_by_resource_group(rg.name):
        print(rg.name, ':', item)
