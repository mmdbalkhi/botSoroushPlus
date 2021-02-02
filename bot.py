#!/bin/python3
from sdk_bot.client import Client
from sys import path
from config import bot_token

bot = Client(bot_token)
try:
    messages = bot.get_messages()
    for message in messages:
        print("New Message Received: " + str(message))
except Exception as e:
          print(e.args[0])
