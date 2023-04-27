from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_title,
    search_by_date,
)
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories
import sys

entry = (
    "Selecione uma das opções a seguir:\n "
    "0 - Popular o banco com notícias;\n "
    "1 - Buscar notícias por título;\n "
    "2 - Buscar notícias por data;\n "
    "3 - Buscar notícias por categoria;\n "
    "4 - Listar top 5 categorias;\n "
    "5 - Sair.\n"
)


def analyzer_menu():
    response = input(entry)

    match response:
        case "0":
            news_quantity = input("Digite quantas notícias serão buscadas: ")
            return get_tech_news(news_quantity)
        case "1":
            new_title = input("Digite o título: ")
            search_by_title(new_title)
        case "2":
            date = input("Digite a data no formato aaaa-mm-dd: ")
            search_by_date(date)
        case "3":
            category = input("Digite a categoria: ")
            search_by_category(category)
        case "4":
            return top_5_categories()
        case "5":
            return print("Encerrando script\n")
        case _:
            return sys.stderr.write("Opção inválida\n")
