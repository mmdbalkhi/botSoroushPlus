#!/bin/python3
from sys import path

from requests import get

from config import bot_token
from get_book_name import get_book_name
from sdk_bot.client import Client


start_text = """سلام به ربات کتاب خوب خوش آمدید\n نزدیکترین نام به کتاب مدنظرتون رو بنویسید تا ربات پیدا بکنه! """
bot = Client(bot_token)
try:
    messages = bot.get_messages()
    for message in messages:
        print("New Message Received: " + str(message))
        if message["type"] == "START":
            bot.send_text(message["from"], start_text)

        elif message["type"] == "TEXT":
            send_text = get_book_name(message["body"])

            if send_text == "این کتاب ها را یافتیم!\n\n":
                send_text = "چیزی نیافتیم! لطفا در نوشتار کلمه دقت کنید! "

            bot.send_text(message["from"], send_text)
        else:
            bot.send_text(message["from"], "من فعلا بلد نیستم اینو چیکار کنم ! اصلا این چی هستش؟ لطفا اسم کتاب خود را وارد کنید.")
except Exception as e:
    print(e.args[0])
