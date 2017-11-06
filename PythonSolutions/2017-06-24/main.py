import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import re

title = input('Name of the Wikipedia page:\n')

# title = "London Stock Exchange"
# Convert to proper link
title = title.replace(" ", "_")

visited = [title]

url = "http://en.wikipedia.org/wiki/" + title
page = urllib.request.urlopen(url)
not_found = True

while not_found:
    soup = BeautifulSoup.BeautifulSoup(page.read())
    title = soup.find(id="firstHeading").contents[0]
    print(title)

    body = soup.find(id="bodyContent")
    paragraphs = soup.findAll("p")
    for p in paragraphs:
        text = "".join(str(s) for s in p.contents)
        text = re.sub('\(([^\n)]*)\)(?![^<>]*>)', '', text)
        reconstructed = BeautifulSoup.BeautifulSoup(text)
        [x.extract() for x in reconstructed.findAll(['sup', 'span'])]
        firstLink = reconstructed.find('a')
        if firstLink is not None:
            link = firstLink['href']
            url = 'http://en.wikipedia.org' + link
            title = firstLink['title']
            if title in visited:
                not_found = False
                print('Loop found at', title)
                break

            if title == "Philosophy":
                print(title)
                not_found = False
                break

            page = urllib.request.urlopen(url)
            visited.append(title)
            break


