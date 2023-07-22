import crawler

fetcher = crawler.ArticleFetcher()

for article in fetcher.fetch():
    print(article.emoji + ": " + article.heading)