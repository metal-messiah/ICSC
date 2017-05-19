import requests
import json

url = "https://content.dropboxapi.com/2/files/get_preview"

headers = {
    "Authorization": "Bearer 71OAfy_GtIAAAAAAAAAA0BtEItMGOdr6zX-1ZHVyUCUscL32VEw1wZI4lHVAVnnO",
    "Dropbox-API-Arg": "{\"path\":\"/ICSC 2017 - On-market listings/ICSC Available Investments.xlsx\"}"
}

r = requests.post(url, headers=headers)
