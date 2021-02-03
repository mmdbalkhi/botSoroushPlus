#!/bin/python3
from sys import path

from requests import get

from config import bot_token
from sdk_bot.client import Client
from get_book_name import get_book_name


text = get_book_name()
bot = Client(bot_token)
try:
    messages = bot.get_messages()
    for message in messages:
        print("New Message Received: " + str(message))
        to = message["from"]
        bot.send_text(to, text)
except Exception as e:
    print(e.args[0])
