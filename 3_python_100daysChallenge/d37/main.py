import requests
TOKEN = "thisissecret"
USERNAME = 'raphafang'
GRAPHID = 'firstgraph'
# https://pixe.la/v1/users/raphafang/graphs/firstgraph.html



# set up user info ------------------------------------------------------------------
pixela_endpoint = 'https://pixe.la/v1/users'
user_para = {"token":TOKEN, 
             "username":USERNAME, 
             "agreeTermsOfService":"yes", 
             "notMinor":"yes"}
# the set up for the pixela
# resp = requests.post(url = pixela_endpoint, json=user_para)
# print(resp.text)


# set up first graph ------------------------------------------------------------------
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_config = {
    'id' : GRAPHID,
    'name': "study graph",
    'unit': 'hr',
    'type':'float',
    'color': 'shibafu'
}
headers = {
    "X-USER-TOKEN":TOKEN
}
# response_set_graph = requests.post(url = graph_endpoint, json = graph_config, headers = headers)
# print(response_set_graph.text)


# post------------------------------------------------------------------
from datetime import datetime

today = datetime.now()
# today = datetime(year=2000,month=12,day=1)

post_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}'
pixel_data = {
    'date':today.strftime('%Y%m%d'),
    "quantity": '2.5'
}
# response_post = requests.post(url = post_endpoint, json=pixel_data, headers = headers)
# print(response_post.text)


# put ------------------------------------------------------------------
today = datetime(year=2000,month=12,day=1)
put_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime("%Y%m%d")}'
new_pixel_data = {
    "quantity": '4.5'
}

# response_put = requests.put(url = put_endpoint, json=new_pixel_data, headers = headers)
# print(response_put.text)


# delete ------------------------------------------------------------------
delete_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime("%Y%m%d")}'
# response_delete = requests.delete(url = delete_endpoint, headers = headers)
# print(response_delete.text)