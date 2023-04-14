from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    news = find_news()

    if len(news) == 0:
        return []

    categories = dict()

    for new in news:
        if new["category"] in categories:
            categories[new["category"]] += 1
        else:
            categories[new["category"]] = 1

    top_5 = list(categories.items())
    top_5.sort(key=lambda x: (x[1]*-1, x[0]))

    return [category[0] for category in top_5[:5]]
