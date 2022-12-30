#!/usr/bin/env python
# coding: utf-8

# In[3]:


import re
import nltk
from nltk.corpus import stopwords

# download required NLTK resources
nltk.download('stopwords')

# set up list of stop words
stop_words = set(stopwords.words('english'))

def process_message(message, response_array, response):
    # split message into list of words and remove stop words
    list_message = [word for word in re.split(r"\W+", message.lower()) if word not in stop_words]
    
    # scores the amount of words in the message that are in the response_array
    score = 0
    for word in list_message:
        if word in response_array:
            score += 1
    
    # returns the response and the score of the response
    return [score, response]

def get_response(message):
    # add your custom message here
    response_list = [
        process_message(message, ['hello', 'hi', 'hey'], 'Wassup!'),
        process_message(message, ['bye', 'goodbye'], 'Adios!'),
        process_message(message, ['how', 'are', 'you'], 'I am good thanks!'),
        process_message(message, ['your', 'name'], 'My name is Ash 2.0, nice to meet you'),
        process_message(message, ['help', 'me'], 'Worry no more because I got you!')
    ]
    
    # checks all of the response scores and returns the best matching response
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])
    
    # get max value for the best response and store it into a variable
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]
    
    # return the matching response to the user
    if winning_response == 0:
        bot_response = 'I did not understand what you wrote'
    else:
        bot_response = matching_response[1]
    return bot_response

# test your system
#print(get_response('help'))


# In[ ]:




