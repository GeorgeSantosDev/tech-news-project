from tech_news.database import search_news
import datetime


def validate_date(date):
    try:
        year, month, day = map(int, date.split('-'))
        datetime.datetime(year, month, day)
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 7
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})

    if len(news) > 0:
        return [(new["title"], new["url"]) for new in news]

    return news


# Requisito 8
def search_by_date(date):
    validate_date(date)

    new_format_date = '/'.join(date.split('-')[::-1])

    news = search_news({"timestamp": {"$eq": new_format_date}})

    if len(news) > 0:
        return [(new["title"], new["url"]) for new in news]

    return news


# Requisito 9
def search_by_category(category):
    news = search_news({"category": {"$regex": category, "$options": "i"}})

    if len(news) > 0:
        return [(new["title"], new["url"]) for new in news]

    return news
