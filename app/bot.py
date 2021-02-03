#!/bin/python3
from sys import path

from requests import get

from config import bot_token
from sdk_bot.client import Client
from get_book_name import get_book_name


bot = Client(bot_token)
try:
    messages = bot.get_messages()
    for message in messages:
        print("New Message Received: " + str(message))

        send_text = get_book_name(message["body"])

        if send_text == "این کتاب ها را یافتیم!\n\n":
            send_text = "چیزی نیافتیم! لطفا در نوشتار کلمه دقت کنید! "

        bot.send_text(message["from"], send_text)
except Exception as e:
    print(e.args[0])
