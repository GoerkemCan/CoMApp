#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
import xml.etree.ElementTree as ET

# Connect to the database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create the table
cursor.execute('''CREATE TABLE tasks (task_id INTEGER PRIMARY KEY, task_name TEXT, status TEXT)''')

# Parse the XML file
tree = ET.parse('example1.xml')
root = tree.getroot()
tasks = root[-3]

# Iterate over the tasks in the XML file and insert them into the table
for task in tasks:
    task_id = task.attrib['id']
    task_name = task[0].text
    status = task[1].text
    cursor.execute('''INSERT INTO tasks (task_id, task_name, status) VALUES (?, ?, ?)''', (task_id, task_name, status))

# Commit the changes to the database
conn.commit()

# Close the connection to the database
conn.close()


# In[ ]:




