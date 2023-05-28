from bs4 import BeautifulSoup

with open("web-scrap/index.html") as file:
    html_code = file.read()

soup = BeautifulSoup(html_code, "html.parser")

print(soup.title.string)