import json
import requests
import urllib3
urllib3.disable_warnings()
    
def handler(context, inputs):
    virtualMachineName = inputs["name"]
    cpu = inputs["cpu"]
    memory = inputs["memory"]
    cluster = inputs["cluster"]
    datacenter = inputs["datacenter"]
    tokenUrl = inputs["sharepoint_token_url"]
    graphUrl = inputs["sharepoint_graph_url"]
    tenantId = context.getSecret(inputs["sharepoint_tenant_id"])
    clientId = context.getSecret(inputs["sharepoint_client_id"])
    clientSecret = context.getSecret(inputs["sharepoint_client_secret"])
    listId = context.getSecret(inputs["sharepoint_list_id"])
    sideId = context.getSecret(inputs["sharepoint_side_id"])
    sessiontoken = create_new_session(tokenUrl,tenantId,clientId,clientSecret);
    createNewItem = create_new_item(vmName,cpu,memory,graphUrl,listId,sideId,sessiontoken)

# Creating new session ###################################################################################
def create_new_session(baseUrl,tenantId,clientId,clientSecret):

    url = baseUrl + tenantId + "/oauth2/v2.0/token"
    proxies = {
        "http": None,
        "https": None
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    print('Generating Access Token...')
    payload = { 
            "grant_type": "client_credentials", 
            "scope": "https://graph.microsoft.com/.default", 
            "client_id": "{}".format(clientId), 
            "client_secret": "{}".format(clientSecret)
    }
    response = requests.post(url, headers=headers, data=payload, proxies=proxies, verify=False, timeout=10)
    if response.status_code == 200:
        data = response.json()
        token = data['access_token']
        output = "New token created successfully"
        responseout = f"Got a response: {response.reason}, with status code: {response.status_code}"
        outputs = {
            "output":output,
            "responseout":responseout
            }   
        print(json.dumps(outputs, indent=4))
        return token
    else:
        return ("Error code : ",response.status_code)

# Creating a new Item ###################################################################################
def create_new_item(vmName,cpu,memory,baseUrl,listId,sideId,accessToken):

    url = baseUrl + sideId + "/lists/" + listId + "/items"
    proxies = {
        "http": None,
        "https": None
    }
    headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(accessToken)
    }
    
    print('Creating a new item...')
    payload =  {
           "fields": {
            "name": "{}".format(name),
            "cpu": "{}".format(cpu),
            "memory": "{}".format(memory)
            "cluster": "{}".format(cluster),
            "datacenter": "{}".format(datacenter)
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload), proxies=proxies, verify=False, timeout=10)
    if 200 <= int(response.status_code) < 300:
        #data = response.json()
        output = "New item created successfully"
        responseout = f"Got a response: {response.reason}, with status code: {response.status_code}"
    if not 200 <= int(response.status_code) < 300:
        output = 'Creating new Item failed'
        output += f"Got a response: {response.reason}, with status code: {response.status_code}"
        output += f"Response: {response.json()}"
        raise Exception(output);
    
    outputs = {
        "output":output,
        "responseout":responseout
    }
    print(json.dumps(outputs, indent=4))
    return outputs
