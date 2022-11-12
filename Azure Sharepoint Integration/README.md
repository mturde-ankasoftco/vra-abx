# How to create new list item in azure sharepoint

You can create a new list item in azure sharepoint by your vRealize Automation Cloud Assembly extensibility action.

# Inputs
## Action Inputs:
    name				      name of virtual machine
    cpu               resource amount of vCPU
    memory            resource amount of memory
    cluster           name of cluster
    datacenter        name of datacenter 
    sharepoint_token_url
    sharepoint_graph_url
## Action Secrets:
    sharepoint_tenant_id				vRealize Automation password for connection   
    sharepoint_client_id
    sharepoint_client_secret
    sharepoint_list_id
    sharepoint_side_id

* Please note that the runtime of action-based extensibility in vRealize Automation Cloud Assembly is Linux-based.
Therefore, any Python dependencies compiled in a Windows environment might make the generated ZIP package unusable for the creation of extensibility actions. Therefore, you must use a Linux shell.

## Necessary Python Modules
    json                                    JSON is a simple data format developed to enable communication between different languages
    requests				The requests module allows you to send HTTP requests using Python
    urllib3
