from covid_news_handling import news_API_request, parse_news_API
from covid_news_handling import update_news

def test_news_API_request():
    assert isinstance(news_API_request(), list)
    assert news_API_request('Covid COVID-19 coronavirus') == news_API_request()

def test_parse_news_API():
    news = news_API_request()
    filtered = parse_news_API(news)
    assert isinstance(filtered, list)

def test_update_news():
    assert isinstance(update_news('test'), list)
