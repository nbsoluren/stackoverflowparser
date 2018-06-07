from bs4 import BeautifulSoup

import requests

file = open("mydivs.txt","a")

url = input("Enter Stack Overflow URL: ")

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data,"html.parser")

#This parses the content
title = soup.find('title')

#Prints the Question of Stack Overflow
print (title.renderContents())
file.write("Question: "+soup.find('a', {"class": "question-hyperlink"}).text + '\n')
file.write('\n')
#Print Details of the question
file.write('Description of QUestion:')
postcell = soup.findAll("div", {"class": "postcell"})
for desc in postcell:
    textblock = desc.findAll("div", {"class": "post-text"})
    for p in textblock:
        p = desc.findAll(['p','code'])
        for fin in p:
            if(fin.name == 'code'):
                file.write ("code:"+'\n')
                file.write ('\t'+fin.text+'\n')
            else:
                file.write (fin.text+'\n')



ansCnt = 0
answercell = soup.findAll("div", {"class": "answercell"})
for ans in answercell:
    ansCnt+=1
    file.write("Answer #: " + str(ansCnt) + '\n')
    textblock = ans.findAll("div", {"class": "post-text"})
    for p in textblock:
        p = ans.findAll(['p','code'])
        for fin in p:
            if(fin.name == 'code'):
                file.write ("code:"+'\n')
                file.write ('\t'+fin.text+'\n')
            else:
                file.write (fin.text+'\n')


mydivs = soup.findAll("div", {"class": "answercell"})
# print(mydivs)



#
# file.write(str(mydivs))
file.close()
