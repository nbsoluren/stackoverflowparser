from bs4 import BeautifulSoup

import requests

url = input("Enter Stack Overflow URL: ")

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data,"html.parser")

#This parses the content
title = soup.find('title')

#Prints the Question
print()
print (title.renderContents())
