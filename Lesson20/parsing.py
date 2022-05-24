import json
from dataclasses import dataclass, asdict
from pprint import pprint

from bs4 import BeautifulSoup

import requests


@dataclass
class Point:
    title: str
    subtitles: list


headers = {
    "user-agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) "
                  "AppleWebKit / 537.36(KHTML, likeGecko) "
                  "Chrome / 100.0.4896.75 Safari / 537.36",
}
url = "https://teachmeskills.by/kursy-programmirovaniya/obuchenie-python-online"


def main(url, headers):

    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    all_html = soup.find_all("div", class_="t517__sectioninfowrapper")

    aaa = []

    for i in all_html:

        title = i.find("strong")
        text = i.find_all("li")

        subtitles = []

        for t in text:
            subtitles.append(t.text.strip())

        aaa.append(asdict(Point(title.text.strip(), subtitles)))

    return json.dumps(aaa, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    print(main(url, headers))
