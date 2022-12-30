#!/usr/bin/env python
# coding: utf-8


import logging
from telegram.ext import *
import responses22
import docx



API_KEY = '###'


#set up the logging
logging.basicConfig(format='%(asctime)s -%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('starting Bot...')




def help_command(update, context):
    update.message.reply_text("Hello, I am the CoMApp construction manager")



#there is a file with tasks for the day that the function reads and sends to the workers
def start_command(update, context):
    update.message.reply_text('Here are your tasks for the day')
    # Open the text file
    with open('Tasks.txt', 'r') as f:
        # Read the contents of the file
        text = f.read()
    # Send the text as a message in the Telegram chat
    update.message.reply_text(text)




def custom_command(update, context):
    # Open the text file in append mode
    with open('Tasks.txt', 'a') as f:
        # Write "Done for the day" at the end of the file
        f.write('Done for the day')
    update.message.reply_text('Task completed for the day')




def handle_message(update, context):
    text = str(update.message.text).lower()
    response = responses22.get_response(text)
    logging.info(f'User ({update.message.chat.id}) says: {text}')
    #bot response
    update.message.reply_text(response)




#handling errors
def error(update, context):
    logging.error(f'Update {update} caused error {context.error}')




if __name__ == '__main__':
    updater = Updater(API_KEY, use_context = True)
    #create a dispatcher to register the handlers and make them useable
    dp = updater.dispatcher
    
    #commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))
    #handle messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    #Log all errors
    dp.add_error_handler(error)
    #Run the bot
    updater.start_polling(2.0)
    updater.idle()
    

