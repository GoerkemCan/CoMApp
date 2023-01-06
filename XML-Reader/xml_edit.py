import xml.etree.ElementTree as ET
from datetime import datetime, timedelta


# defs
def parse(filename):
    
    global tree
    global root
    tree = ET.parse(filename)
    root = tree.getroot()
    
    
def task_find():
    
    tasks = root[-3]   
    temp = []
    temp2 = []
    
    word = word_find(sentence)
    
    for i in tasks:
        
        temp.append(i)
        z1 = temp.index(i)
        task = tasks[z1]
        
        for n in task:
            
            temp2.append(n.text)
            if n.text == word:
                z2 = temp2.index(n.text) % 43
                # root[-3][z1][z2] gives out where the assignment name is located
                
                found = root[-3][z1][z2]
                
                return z1, z2
         
            

def changer():
    flag = sieve(sentence)
    z1, z2 = task_find()
    
    found = root[-3][z1][z2]
    
    change = found.text + " Completed"
    
    if flag == "completed":
        found.text = change
        
    
    
def sieve(sentence):
    
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
    flag = sieve(sentence)
    
    if flag == "completed" or flag == "delayed":
        title = sentence.title()
    
        word = title.replace("Assignment Completed: ", "")
        
        return word


        
def write(new):
    tree.write(new)    
    
def add_time( days=0, months=0, years=0):
  
    z1, z2 = task_find()
    print(z1)
    print(z2)
    date_string = root[-3][z1][11].text
  
    # Convert the date string to a datetime object
    date = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")
  
    # Add the specified number of days, months, and years to the date
    date = date + timedelta(days=days)
    date = date.replace(year=date.year + years)
    date = date.replace(month=date.month + months)
  
    # Return the modified datetime object as a formatted string
    return date.strftime("%Y-%m-%dT%H:%M:%S")



# Input
sentence = "Assignment Completed: Open Bpmn File"
filename = "example1.xml"
new = "new1.xml"


parse(filename) 
task_find()
changer()
write(new)
add_time( days=2, months=3, years=1)
