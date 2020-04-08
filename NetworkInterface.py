
'''
import re
import os
#
def save_command(command,filename):
    stream = os.popen(command)
    text = stream.read()
    text = re.sub(' : ',',',text)
    text= re.sub(" ", "", text)
    #text = re.sub(',' ',text)
    text=text.replace("..........","")
    file1 = open(filename,"w+")
    file1.write(text)
    exit(0)
'''    
def cleantext(text):
    text= re.sub(" ", "", text)
    text = re.sub(':',',',text)
    text=text.replace(".","")
    return text

def save_file(filename):
    file1 = open(filename,"w+")
    file1.write(text)
    exit(0)

def read_command(command):
    stream = os.popen(command)
    text = stream.read()
    return text

text=read_command('ipconfig /all')
text=cleantext(text)
save_file('output1.csv')
'''
save_command('ipconfig /all','output1.csv')