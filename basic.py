from bs4 import BeautifulSoup

import requests

class StackObject:
   def __init__(self,question, description, answers, upvotes, authors):
      self.question = question
      self.authors = authors
      self.upvotes = upvotes
      self.description = description
      self.answers = answers


data = {}
data["answers"] = {}
data["question"] = {}

print(data)
url = input("Enter Stack Overflow URL: ")

r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data,"html.parser")



#Prints the Question of Stack Overflow
question = soup.find('a', {"class": "question-hyperlink"}).text

description = ""
postcell = soup.findAll("div", {"class": "postcell"})
for desc in postcell:
    textblock = desc.findAll("div", {"class": "post-text"})
    for p in textblock:
        p = desc.findAll(['p','code'])
        for fin in p:
            if(fin.name == 'code'):
                description += '\t'+fin.text+'\n'
            else:
                description += fin.text+'\n'

answers = []
answercell = soup.findAll("div", {"class": "answercell"})
for ans in answercell:
    anstext = ""
    textblock = ans.findAll("div", {"class": "post-text"})
    for p in textblock:
        p = ans.findAll(['p','code'])
        for fin in p:
            if(fin.name == 'code'):
                anstext += ('\t'+fin.text+'\n')
            else:
                anstext += (fin.text+'\n')
    answers.append(anstext)

authors = []
postcell = soup.findAll("div", {"class": "postcell"})
for ans in postcell:
    textblock = ans.findAll("div", {"class": "user-details"})
    for p in textblock:
        k = p.findAll(['a'])
        for fin in k:
            authors.append(fin.text)

upvotes = soup.find("span", {"class": "vote-count-post"}).text


data = {}
data["question"] = {
    "header": question,
    "description": description,
    "authors": authors,
    "upvotes": upvotes
}
data["answers"] = [{}]

print(data)
