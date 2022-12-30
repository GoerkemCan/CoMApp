import xml.etree.ElementTree as ET
import lxml


# defs
def parse(filename):
    
    global tree
    global root
    tree = ET.parse(filename)
    root = tree.getroot()
    
    
def task_find(filename):
    
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
                
                print(z1, z2) # root[-3][z1][z2] gives out where the assignment name is located
                print(root[-3][z1][z2].text)
                
                found = root[-3][z1][z2]
                
                return found
            

def changer():
    flag = sieve(sentence)
       
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
        print(word)
        
        return word


        
def write(new):
    tree.write(new)






# Input
sentence = "Assignment Completed: Open Bpmn File"
filename = "example1.xml"
new = "new1.xml"


parse(filename) 
task_find(filename)
changer()
write(new)

