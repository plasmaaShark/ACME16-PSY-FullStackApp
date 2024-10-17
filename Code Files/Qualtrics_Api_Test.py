import requests

survey_id = 'SV_3wvBtxhaQcsl06G'
data_center = "wsu.iad1"
token = '4DGKlfv4CPqlSfXQGODa1Yv4lr5V3wZdW19vie7A'

baseUrl = "https://{0}.qualtrics.com/API/v3/surveys/".format(data_center)
headers = {
    "x-api-token": token,
}

response = requests.get(baseUrl, headers=headers)

print(response.text)