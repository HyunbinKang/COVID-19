from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='bf2de3379545477084975ecd19266962')


top_headlines = newsapi.get_top_headlines(country='us')
type(top_headlines)
top_headlines.keys()
print(top_headlines['totalResults'])

articles = top_headlines['articles']
for x, y in enumerate(articles):
       print(f'{x}  {y["author"]}')
