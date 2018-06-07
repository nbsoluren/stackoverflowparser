from bs4 import BeautifulSoup
import requests

#asks for user input
#url = input("Enter Stack Overflow URL: ")
url = 'https://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python'

#initialization
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data,"html.parser")

#Retrieves the question
question = soup.find('a', {"class": "question-hyperlink"}).text

#Retrieve question Description
description = ""
postAuthors = []
for desc in soup.findAll("div", {"class": "postcell"}):
    for p in desc.findAll("div", {"class": "post-text"}):
        for fin in desc.findAll(['p','code']):
            if(fin.name == 'code'):
                description += '\t'+fin.text+'\n'
            else:
                description += fin.text+'\n'
    for p in desc.findAll("div", {"class": "user-details"}):
        for fin in p.findAll(['a']):
            postAuthors.append(fin.text)



#Retrieves # of upvotes
upvotes = soup.find("span", {"class": "vote-count-post"}).text

#Retrieves answers of the question
answers =[]
for ans in soup.findAll("div", {"class": "answercell"}):
    pseudoans = {}
    ansAuthors = []
    anstext = ""
    upvotesans = ""
    for p in ans.findAll("div", {"class": "post-text"}):
        for fin in ans.findAll(['p','code']):
            if(fin.name == 'code'):
                anstext += ('\t'+fin.text+'\n')
            else:
                anstext += (fin.text+'\n')
    for p in ans.findAll("div", {"class": "user-details"}):
        for fin in p.findAll(['a']):
            ansAuthors.append(fin.text)


    upvotesans = ans.find_previous_sibling().find("span", {"class": "vote-count-post"}).text


    pseudoans["answer"] = anstext
    pseudoans["authors"] = ansAuthors
    pseudoans["upvotes"] = upvotesans
    answers.append(pseudoans)


#Putting it all together
data = {}
data["question"] = {
    "header": question,
    "description": description,
    "authors": postAuthors,
    "upvotes": upvotes
}
data["answers"] = answers

print(data)
