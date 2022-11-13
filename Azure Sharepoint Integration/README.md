# How to create new list item in azure sharepoint
You can create a new list item in azure sharepoint by your vRealize Automation Cloud Assembly extensibility action.
## Action Inputs:
    name				        The name of virtual machine
    cpu                                     resource amount of vCPU
    memory                                  resource amount of memory
    cluster                                 The name of cluster
    datacenter                              The name of datacenter 
    sharepoint_token_url                    The url where you will receive token
    sharepoint_graph_url                    The Microsoft Graph API url
## Action Secrets:
    sharepoint_tenant_id                    Azure tenant id   
    sharepoint_client_id                    Azure client id 
    sharepoint_client_secret                Azure client secret
    sharepoint_list_id                      Sharepoint list id
    sharepoint_side_id                      Sharepoint side id

* Please note that the runtime of action-based extensibility in vRealize Automation Cloud Assembly is Linux-based.
Therefore, any Python dependencies compiled in a Windows environment might make the generated ZIP package unusable for the creation of extensibility actions. Therefore, you must use a Linux shell.

## Python Modules
    json                                    JSON is a simple data format developed to enable communication between different languages
    requests				The requests module allows you to send HTTP requests using Python
    urllib3                                 Urllib3 is a powerful, user-friendly HTTP client for Python

## You need the necessary resources to check if you don't know how to find the tenant id, client id and client secret

[How to find azure tenant id](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-to-find-tenant)

[How to find azure client id and secret](https://docs.lacework.com/onboarding/gather-the-required-azure-client-id-tenant-id-and-client-secret)

[How to grant access using SharePoint](https://learn.microsoft.com/en-us/sharepoint/dev/solution-guidance/security-apponly-azureacs)
          
