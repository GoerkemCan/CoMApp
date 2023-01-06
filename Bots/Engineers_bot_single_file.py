#!/usr/bin/env python
# coding: utf-8

# This is a combination of the xml parsing script + the engineers bot that seeks to parse the xml file via text on telegram

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

import logging
import xml.etree.ElementTree as ET
import lxml
import lxml.etree as ET
from telegram.ext import *
import responses22
import docx


API_KEY = '5847519772:AAGZG66Umo-aLayYoVxg7J4oxoYq4GsY0oU'
filename = "example1.xml"
new = "new1.xml"


# Set up logging
logging.basicConfig(format='%(asctime)s -%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting bot...')


def parse(filename):
    # Parse the XML file
    global tree
    global root
    tree = ET.parse(filename)
    root = tree.getroot()
    

def task_find(filename):
    # Search the XML file for a specific task based on the user-provided input string
    tasks = root[-3]   
    temp = []
    temp2 = []
    global found

    word = word_find(sentence)

    for i in tasks:
        temp.append(i)
        z1 = temp.index(i)
        task = tasks[z1]

        for n in task:
            temp2.append(n.text)
            if n.text == word:
                print(n.text)
                z2 = temp2.index(n.text) % 43

                print(z1, z2)  # root[-3][z1][z2] gives out where the assignment name is located
                print(root[-3][z1][z2].text)

                found = root[-3][z1][z2]

                return found


def changer():
    # Modify the text of the found element based on the user-provided input string
    flag = sieve(sentence)
       
    change = found.text + " Completed"
    
    if flag == "completed":
            found.text = change
        
def sieve(sentence):
    # Check the user-provided input string for certain keywords and return a flag indicating the type of action indicated by the string
    flag = None
    lower = sentence.lower()
    
    if ("completed" in lower) or ("done" in lower) or ("finished" in lower):
               
        flag = "completed"
        
        return flag
            
    
    elif "delay" in lower:
                
        flag = "delayed"
        
        return flag
    
    else:
        return flag


def word_find(sentence):
    # Extract the task name from the user-provided input string
    flag = sieve(sentence)
    
    if flag == "completed" or flag == "delayed":
        title = sentence.title()
    
        word = title.replace("Assignment Completed: ", "")
        print(word)
        
        return word


def write(new):
    # Write the modified XML tree to a new file
    tree.write(new)


def help_command(update, context):
    update.message.reply_text("Hello, here are the progress pictures of the construction")
    


def start_command(update, context):
    # Call the task_find function and send the found task to the user
    found = task_find(filename)
    update.message.reply_text(f'Task found: {found.text}')
    


def custom_command(update, context):
    # Call the changer function and update the status of the found task
    changer()
    update.message.reply_text('Task status updated')


def handle_message(update, context):
    # Get the user's message, pass it to the sieve and word_find functions, and send the resulting flag and word back to the user
    text = update.message.text
    flag = sieve(text)
    word = word_find(text)
    update.message.reply_text(f'Flag: {flag}, Word: {word}')


def error(update, context):
    logging.error(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    # Set up the Updater and Dispatcher
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Add the command handlers
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    # Handle messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Start the bot
    updater.start_polling(2.0)
    updater.idle()

    


# The below code is the suggested improvement on the code above

# In[ ]:


import lxml.etree as ET

API_KEY = '5847519772:AAGZG66Umo-aLayYoVxg7J4oxoYq4GsY0oU'
filename = "example1.xml"
new = "new1.xml"

logging.basicConfig(format='%(asctime)s -%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting bot...')

def parse(filename):
    tree = ET.parse(filename)
    return tree.getroot()

def task_find(root, word):
    tasks = root[-3]   
    temp = {}
    for i, task in enumerate(tasks):
        for n, element in enumerate(task):
            temp[element.text] = (i, n)
            if element.text == word:
                return task[n]

def changer(found):
    change = found.text + " Completed"
    found.text = change
        
def sieve(sentence):
    lower = sentence.lower()
    flags = {"completed": "completed", "done": "completed", "finished": "completed", "delay": "delayed"}
    for keyword, flag in flags.items():
        if keyword in lower:
            return flag
    return None

def word_find(sentence):
    flag = sieve(sentence)
    if flag in ["completed", "delayed"]:
        return sentence.replace("Assignment Completed: ", "")

def write(tree, new):
    tree.write(new)

def help_command(update, context):
    update.message.reply_text("Hello, here are the progress pictures of the construction")
    
def start_command(update, context):
    root = parse(filename)
    found = task_find(root, word_find(sentence))
    update.message.reply_text(f'Task found: {found.text}')
    
def custom_command(update, context):
    root = parse(filename)
    found = task_find(root, word_find(sentence))
    changer(found)
    update.message.reply_text('Task status updated')

def handle_message(update, context):
    text = update.message.text
    flag = sieve(text)
    word = word_find(text)
    update.message.reply_text(f'Flag: {flag}, Word: {word}')

def error(update, context):
    logging.error(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    # Set up the Updater and pass it the API key
    updater = Updater(API_KEY, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    # Add message handler
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Add error handler
    dp.add_error_handler(error)

    # Start the bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

