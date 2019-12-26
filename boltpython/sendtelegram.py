import requests                 # for making HTTP requests
import json                     # library for handling JSON data
import time                     # module for sleep operation

from boltiot import Bolt   
bolt_api_key = "cxxxxxxf2"                 # This is your Bolt Cloud API Key
device_id = "BOLTXXXXX"                    # This is the device ID and will be similar to BOLTXXXX where XXXX is some numbers
telegram_chat_id = "@bot"            # This is the channel ID of the created Telegram channel. Paste after @ symbol.
telegram_bot_id = "bot1055783589:AAXXXHqBM"           # This is the bot ID of the created Telegram Bot. Paste after bot text.

mybolt = Bolt(bolt_api_key,device_id)
# this is to send the message to telgram channel
def send_telegram_message(message):
    """Sends message via Telegram"""
    url = "https://api.telegram.org/" + telegram_bot_id + "/sendMessage"
    data = {
        "chat_id": telegram_chat_id,
        "text": message
    }
    try:
        response = requests.request(
            "POST",
            url,
            params=data
        )
        print("This is the Telegram response")
        print(response.text)
        telegram_data = json.loads(response.text)
        return telegram_data["ok"]
    except Exception as e:
        print("An error occurred in sending the alert message via Telegram")
        print(e)
        return False
message='sat shri akal'
send_telegram_message(message)
