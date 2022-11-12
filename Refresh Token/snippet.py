import json
import requests

def handler(context, inputs):
    username = inputs["vra_usr"]
    password = context.getSecret(inputs["vra_pwd"])
    baseUrl = inputs["base_url"]
    url = baseUrl + "/csp/gateway/am/api/login?access_token"
    headers = {"Content-Type": "application/json"}
    body = {
            "username": "{}".format(username),
            "password": "{}".format(password)
    }
    print('Generating Refresh Token...')
    response = requests.post(url, headers=headers, data=json.dumps(body))
    if response.status_code == 200:
        data = response.json()
        token = (data['refresh_token'])
        print("token : ",token)
        return token
    else:
        return ("Error code : ",response.status_code)