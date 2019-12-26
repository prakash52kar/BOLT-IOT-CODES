from boltiot import Bolt
import http.client
import json
api_key = "caXXXXXf2"
device_id  = "BOLTXXXX"
mybolt = Bolt(api_key, device_id)

def sms(temp):   
 conn = http.client.HTTPConnection("api.msg91.com")
 payload ='''{
  "sender": "hellos",
  "route": "4",
  "country": "91",
  "sms": [
    {
      "message":"hello how r u?",
      "to": [
        "9XXXXXX"
      ]
    }   
  ]
 }'''   
 x=eval(payload)
 x['sms'][0]['message']="hello temp has exceeded to "+str(temp)
 y=json.dumps(x)
 print(y)
 headers = {
    'authkey': "2XXXXXXa9",
    'content-type': "application/json"}
 print(payload)
 conn.request("POST", "/api/v2/sendsms?country=91&sender=&route=&mobiles=&authkey=&encrypt=&message=&flash=&unicode=&schtime=&afterminutes=&response=&campaign=",y, headers)
 res = conn.getresponse()
 data = res.read()
 print(data.decode("utf-8"))

for i in range(10):

    response = mybolt.analogRead('A0')
    r=eval(response)
    temp=0.097*int(r['value'])
    print (temp)
    if temp>26:
        sms(temp)
        break






 
 
 

