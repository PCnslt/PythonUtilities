from dotenv import load_dotenv
import os as os
import requests
import datetime

QUESTION_IN_TITLE='tesla'
LANGUAGE = 'en'
news_from_date = (datetime.date.today()
                  - datetime.timedelta(days=3)).strftime('%Y-%m-%d') # 3 days ago
news_to_date= (datetime.date.today()
               - datetime.timedelta(days=3)).strftime('%Y-%m-%d') # yesterday

def get_news(topic, from_date, to_date, language):
    """ GET the news using to and from dates.
        Languages supported = en, sp
    """ 
    load_dotenv('.secrets')
    newsapi_org_key = os.getenv('NEWSAPI_ORG_KEY')
    
    get_news_url = 'https://newsapi.org/v2/everything?q='+topic+'&from='+from_date+'&to='+to_date+'&language='+language+'&sortBy=publishedAt&apiKey='+newsapi_org_key 
    r = requests.get(get_news_url, timeout=300)
    content = r.json()
    # print(type(content))
    # print(content)
    
    articles = content['articles']
    results = []
    for article in articles:
        article_title = article['title']
        article_description = article['description']
        results.append({
            "Title": article_title,
            "Description": article_description})
    
    return results

def get_top_news(topic, country, language):
    """ GET the top news by country.
        Languages supported = en, sp
    """ 
    load_dotenv('.secrets')
    newsapi_org_key = os.getenv('NEWSAPI_ORG_KEY')
    
    get_news_url = 'https://newsapi.org/v2/everything?q='+topic+'&top-headlines='+country+'&language='+language+'&sortBy=publishedAt&apiKey='+newsapi_org_key
    # print("Searching "+get_news_url)
    r = requests.get(get_news_url, timeout=300)
    content = r.json()
    
    # print(type(content))
    # print(content)
    articles = content['articles']
    results = []
    for article in articles:
        article_title = article['title']
        article_description = article['description']
        results.append({
            "Title": article_title,
            "Description": article_description})
    
    return results

# #get all news
# latest_news = get_news(QUESTION_IN_TITLE, news_from_date, news_to_date, LANGUAGE)
# for news in latest_news:
#     print(news['Title'])

#get top news
top_headlines = get_top_news(topic='tesla', country='us', language='en')
for news in top_headlines:
    print(news['Title'])
