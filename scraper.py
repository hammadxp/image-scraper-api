import requests
from bs4 import BeautifulSoup
import validators


def scraper(url):

    try:
        htmlData = requests.get(url).text
        bsData = BeautifulSoup(htmlData, "html.parser")
        imgTags = bsData.find_all("img")

        imgs = [
            {
                'title': img.get('title', ''),
                'alt': img.get('alt', ''),
                'src': img.get('src', '')
            }
            for img in imgTags
        ]

        # f"{img.get('src', '') if validators.url(img.get('src', '')) else url + img.get('src', '')}"

        return imgs

    except Exception as e:
        raise e
