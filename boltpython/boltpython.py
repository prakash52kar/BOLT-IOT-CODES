import requests
import time as t
def ledon():
 url = "https://cloud.boltiot.com/remote/ca6XXXXXXX8b0f2/digitalWrite"
 querystring = {"pin":"0","state":"HIGH","deviceName":"BOLTXXXXX"}
 headers = {
    'Cache-Control': "no-cache"
    }
 response = requests.request("GET", url, headers=headers, params=querystring)
 print(response.text)

def ledoff():
 url = "https://cloud.boltiot.com/remote/ca60XXXXXXX0f2/digitalWrite"
 querystring = {"pin":"0","state":"LOW","deviceName":"BOLTXXXXX"}
 headers = {
    'Cache-Control': "no-cache"
    }
 response = requests.request("GET", url, headers=headers, params=querystring)
 print(response.text)


ledon()
t.sleep(0.5)     
ledoff()

