#!env/bin/ python3
"""main file in soroush plus Bot
"""

from client import Client, get_book_name

from config import BOT_TOKEN
START_TEXT = """سلام به ربات کتاب خوب خوش آمدید شما میتوانید نام نویسنده یا کتاب مورد نظرتون رو جست و جو کنید تا بهترین نتایج به دست شما برسه:) """

bot = Client(BOT_TOKEN)
try:
    messages = bot.get_messages()
    for message in messages:
        print("New Message Received: " + str(message))
        if message["type"] == "START":
            bot.send_text(message["from"], START_TEXT)

        elif message["type"] == "TEXT":
            SEND_TEXT = get_book_name(message["body"])

            if SEND_TEXT == "این کتاب ها را یافتیم!\n\n":
                SEND_TEXT = "چیزی نیافتیم! لطفا در نوشتار کلمه دقت کنید! "

            bot.send_text(message["from"], SEND_TEXT)
        else:
            bot.send_text(
                message["from"], "من فعلا بلد نیستم اینو چیکار کنم \
                    ! اصلا این چی هستش؟ لطفا اسم کتاب خود را وارد کنید.")
except Exception as exception:
    print(exception.args[0])
