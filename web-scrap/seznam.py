import sys
from bs4 import BeautifulSoup
import requests

response3 = requests.get("https://www.seznam.cz/")
soup = BeautifulSoup(response3.text, "html.parser")

articles = soup.find_all(class_="article__title")
with open ("web-scrap/seznam.txt", "w") as file:
    for article in articles:
        one_article_text = article.getText()
        one_article_link = article.get("href")
        if "Policie" in one_article_text or "Kopeček" in one_article_text:
            try:
                file.write(one_article_text)
                file.write("\n")
                file.write(one_article_link)
                file.write("\n")
            except UnicodeEncodeError:
                try:
                    print(article.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
                except:
                    print("Unable to display the article")
