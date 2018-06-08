from bs4 import BeautifulSoup
import requests
import json
def stackParser(url):

    #initialization
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data,"html.parser")
    #Putting it all together
    data = {}
    data["question"] = partParser(soup,"question")[0]
    data["answers"] = partParser(soup, "answers")

    return json.dumps(data)

    # print(json.dumps(data))




def partParser(soup,type):

    key = "answercell"
    #retrieves header if question
    if (type == "question"):
        question = soup.find('a', {"class": "question-hyperlink"}).text
        key = "postcell"
        print("this is idenfied as a # QUESTION: ")

    dataPack = []
    for chunk in soup.findAll("div", {"class": key}):
        data = {}
        authors = []
        comments = []
        description = ""
        upvotes = ""
        for p in chunk.findAll("div", {"class": "post-text"}):
            for fin in chunk.findAll(['p','code']):
                if(fin.name == 'code'):
                    description += ('\t'+fin.text+'\n')
                else:
                    description += (fin.text+'\n')

        for p in chunk.findAll("div", {"class": "user-details"}):
            for fin in p.findAll(['a']):
                authors.append(fin.text)

        for fin in chunk.find_next_sibling().findAll("li", {"class": "comment"}):
                pseudocomments = {}
                pseudocomments["score"] = fin.find("div", {"class": "comment-score"}).text
                pseudocomments["comment"] = fin.find("span", {"class": "comment-copy"}).text
                pseudocomments["author"] = fin.find("a", {"class": "comment-user"}).text
                comments.append(pseudocomments)

        upvotesans = chunk.find_previous_sibling().find("span", {"class": "vote-count-post"}).text

        data["description"] = description
        data["authors"] = authors
        data["upvotes"] = upvotes
        data["comments"] = comments
        dataPack.append(data)
    return dataPack



# url = 'https://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python'
# main(url)
