import requests
import time
from bs4 import BeautifulSoup


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
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
