To create a Service Principal key, run the following command: 

az ad sp create-for-rbac --role reader --name [name] --sdk-auth > ~/.azure/sp_keys/readonly.json
