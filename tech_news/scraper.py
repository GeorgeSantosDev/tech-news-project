import requests
import time
import re
from bs4 import BeautifulSoup
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)

    header = {"user-agent": "Fake user-agent"}

    try:
        response = requests.get(url, timeout=3, headers=header)
    except requests.ReadTimeout:
        return None

    if response.status_code == 200:
        return response.text

    return None


# Requisito 2
def scrape_updates(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    link_list = soup.find_all("a", {"class": "cs-overlay-link"})

    return [link["href"] for link in link_list]


# Requisito 3
def scrape_next_page_link(html_content):
    if html_content == "":
        return None

    soup = BeautifulSoup(html_content, "html.parser")
    next_page_element = soup.find("a", {"class": "next"})

    return next_page_element["href"]


# Requisito 4
def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    url = soup.find("link", {"rel": "canonical"})
    title = soup.find("h1", {"class": "entry-title"})
    timestamp = soup.find("li", {"class": "meta-date"})
    writer = soup.find("span", {"class": "author"}).find("a")
    reading_time = soup.find("li", {"class": "meta-reading-time"})
    summary = soup.find("div", {"class": "entry-content"}).find_all("p")
    category = soup.find("a", {"class": "category-style"}).find_all("span")

    return {
        "url": url["href"],
        "title": title.text.strip(),
        "timestamp": timestamp.text,
        "writer": writer.text,
        "reading_time": int(re.search(r'\d+', reading_time.text).group()),
        "summary": summary[0].text.strip(),
        "category": category[1].text,
    }


# Requisito 5
def get_tech_news(amount):
    news_list = []
    next_page = "https://blog.betrybe.com/"

    while len(news_list) < int(amount):
        html = fetch(next_page)
        news_links_list = scrape_updates(html)

        for link in news_links_list:
            if len(news_list) < int(amount):
                new_html = fetch(link)
                new_infos = scrape_news(new_html)
                news_list.append(new_infos)

        if not next_page:
            break

        next_page_link = scrape_next_page_link(html)
        next_page = next_page_link
    create_news(news_list)
    return news_list
