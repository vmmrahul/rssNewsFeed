import feedparser


def trending(obj):
    if obj == '/':
        # NewsFeed = feedparser.parse("http://feeds.feedburner.com/ndtvnews-trending-news")
        NewsFeed = feedparser.parse("http://feeds.feedburner.com/ndtvnews-top-stories")
    elif obj == "Entertainment":
        NewsFeed = feedparser.parse("http://feeds.feedburner.com/ndtvmovies-latest")
    elif obj == "Business":
        NewsFeed = feedparser.parse("http://feeds.feedburner.com/ndtvprofit-latest")
    elif obj == "International":
        NewsFeed = feedparser.parse("http://feeds.feedburner.com/ndtvnews-world-news")
    elif obj == "National":
        NewsFeed = feedparser.parse("http://feeds.feedburner.com/ndtvnews-india-news")
    elif obj == "Science":
        NewsFeed = feedparser.parse("http://feeds.feedburner.com/gadgets360-latest")
    elif obj == "sports":
        NewsFeed = feedparser.parse("http://feeds.feedburner.com/ndtvsports-latest")
    elif obj == "AutoMobiles":
        NewsFeed = feedparser.parse("http://feeds.feedburner.com/carandbike-latest")
    elif obj == "Cities":
        NewsFeed = feedparser.parse("http://feeds.feedburner.com/ndtvnews-cities-news")
    elif obj == "Tech":
        NewsFeed = feedparser.parse("https://feeds.feedburner.com/gadgets360-latest")

    ndtvnewslist = []
    for i in range(0, len(NewsFeed)):
        dist = {}
        entry = NewsFeed.entries[i]
        # print(entry)
        dist['title'] = entry.title
        dist['storyimage'] = entry.storyimage
        dist['fullimage'] = entry.fullimage
        dist['desc'] = entry.summary_detail
        dist['urlsdata'] = entry.link
        ndtvnewslist.append(dist)
    return ndtvnewslist[:20]

# print(trending('/'))
