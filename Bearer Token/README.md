# How to get a bearer token for vRealize Automation with Python

You can create a bearer token by your vRealize Automation Cloud Assembly extensibility action.

# Inputs
## Action Inputs:
    username				vRealize Automation username for connection
    baseUrl                                 vRealize Automation base url or FQDN
## Action Secrets:
    password				vRealize Automation password for connection   

* Please note that the runtime of action-based extensibility in vRealize Automation Cloud Assembly is Linux-based.
Therefore, any Python dependencies compiled in a Windows environment might make the generated ZIP package unusable for the creation of extensibility actions. Therefore, you must use a Linux shell.

## Necessary Python Modules
    json                                    JSON is a simple data format developed to enable communication between different languages
    requests				The requests module allows you to send HTTP requests using Python

This's a image of some defined variable
![inputAction](https://github.com/mturde-ankasoftco/vra-abx/blob/main/Refresh%20Token/media/inputAction.png)
This's output of bearer token action
![inputAction](https://github.com/mturde-ankasoftco/vra-abx/blob/main/Refresh%20Token/media/detailsAction.png)
