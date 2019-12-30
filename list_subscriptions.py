from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.resource.subscriptions import SubscriptionClient
import os


os.environ['AZURE_AUTH_LOCATION'] = os.path.expanduser('~/.azure/sp_keys/readonly.json')
client = get_client_from_auth_file(SubscriptionClient)

for subscription in client.subscriptions.list():
    # print(subscription)
    print('Name: ', subscription.display_name)
    print('Subscription ID: ', subscription.subscription_id)
    print('Tenant ID: ', subscription.tenant_id)
    print('State: ', subscription.state)
    print('Policies: ', subscription.subscription_policies)
    print('Authorization Source: ', subscription.authorization_source)
    print('Managed By: ', subscription.managed_by_tenants)
