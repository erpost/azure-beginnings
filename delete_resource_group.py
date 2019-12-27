from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.resource.resources import ResourceManagementClient
import os


os.environ['AZURE_AUTH_LOCATION'] = os.path.expanduser('~/.azure/sp_keys/contributor.json')
client = get_client_from_auth_file(ResourceManagementClient)

delete_async_operation = client.resource_groups.delete('delete-me')
delete_async_operation.wait()
