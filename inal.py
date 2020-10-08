from glob import glob
import logging
from random import choice
import settings

from telegram.ext import Updater, CommandHandler, MessageHandler , Filters




logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s",
                    level = logging.INFO,
                    filename="li.log"
                    )


def greet_user(bot,update):
    text = "Вызван /start"
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot,update):
    user_text = "Привет, {}! Ты написал:  {}".format(update.message.chat.first_name ,update.message.text) 
    logging.info("Firstname: %s, User:  %s , Chat id: %s , Message: %s ",update.message.chat.first_name,    update.message.chat.last_name , 
                                update.message.chat.id , update.message.text ,) 
    update.message.reply_text(user_text)

def send_cat_picture(bot, update):
    cat_list = glob ("images/cat*jp*g")
    cat_pic = choice(cat_list)
    bot.send_photo(chat_id = update.message.chat_id, photo=open(cat_pic,"rb"))




def main():
    mybot = Updater(settings.API_KEY,request_kwargs=settings.PROXY)

    logging.info("Бот запускается")
    

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("cat", send_cat_picture))
    
    
    dp.add_handler(MessageHandler(Filters.text,talk_to_me))
    
    
    
    mybot.start_polling()
    mybot.idle()


main()
