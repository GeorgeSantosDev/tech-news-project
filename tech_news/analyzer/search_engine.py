from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})

    if len(news) > 0:
        return [(new["title"], new["url"]) for new in news]

    return news


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    news = search_news({"category": {"$regex": category, "$options": "i"}})

    if len(news) > 0:
        return [(new["title"], new["url"]) for new in news]

    return news
