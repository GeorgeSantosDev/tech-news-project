from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest
from unittest.mock import MagicMock

expected = {
    "readable": [
        {
            "unfilled_time": 3,
            "chosen_news": [
                (
                    "Não deixe para depois: Python é a linguagem do momento",
                    4,
                ),
                (
                    "Selenium, BeautifulSoup ou Parsel?",
                    3,
                ),
            ],
        },
    ],
    "unreadable": [
        ("FastAPI e Flask: frameworks para APIs em Python", 15),
        ("A biblioteca Pandas e o sucesso da linguagem Python", 12),
    ],
}


@pytest.fixture
def mocked_value():
    return [
        {
            "title": "Não deixe para depois: Python é a linguagem do momento",
            "reading_time": 4,
        },
        {
            "title": "Selenium, BeautifulSoup ou Parsel?",
            "reading_time": 3,
        },
        {
            "title": "FastAPI e Flask: frameworks para APIs em Python",
            "reading_time": 15,
        },
        {
            "title": "A biblioteca Pandas e o sucesso da linguagem Python",
            "reading_time": 12,
        },
    ]


error_message = "Valor 'available_time' deve ser maior que zero"


def test_reading_plan_group_news(mocked_value):
    with pytest.raises(ValueError, match=error_message):
        ReadingPlanService.group_news_for_available_time(0)

    ReadingPlanService._db_news_proxy = MagicMock(return_value=mocked_value)
    response = ReadingPlanService.group_news_for_available_time(10)

    assert len(response["readable"]) == 1
    assert len(response["unreadable"]) == 2
    assert response["readable"] == expected["readable"]
    assert response["unreadable"] == expected["unreadable"]
