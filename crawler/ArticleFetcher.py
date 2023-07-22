import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from .CrawledArticle import CrawledArticle
class ArticleFetcher():
    def fetch(self):
        url = "https://python.beispiel.programmierenlernen.io/index.php"

        while url != "":
            print(url)
            time.sleep(1)
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")

            for card in soup.select(".card"):
                image = urljoin(url, (card.select_one("img").attrs["src"]))
                emoji = card.select_one(".emoji").text
                heading = card.select(".card-title span")[1].text
                card_text = card.select_one(".card-text").text

                yield CrawledArticle(image, emoji, heading, card_text)

            next_button = soup.select_one(".navigation a")

            if next_button:
                next_link = urljoin(url, next_button.attrs["href"])
                url = next_link
            else:
                url = ""