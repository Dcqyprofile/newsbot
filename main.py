import feedparser
from dotenv import load_dotenv
from newspaper import Article
import openai
import os

load_dotenv() 
openai.api_key = os.getenv("OPENAI_API_KEY")

# RSS Feeds for each link to fetch latest articles in XML format
RSS_FEEDS = {
    "techcrunch": "https://techcrunch.com/feed/",
    "cnet": "https://www.cnet.com/rss/all/"
}

def fetch_articles(topic, source = None, max_results = 3):
    # source is what user wants -> techcrunch etc
    feeds = [RSS_FEEDS.get(source) if source else RSS_FEEDS.values()]
    all_entries = []
    # parse XML format into readable form
    for feed_url in feeds:
        # converts XML format into python readable dictionary format
        feed = feedparser.parse(feed_url)
        for entry in feed.entries():
            all_entries.append({
                "title": entry.title,
                "link": entry.link
            })
# only give me max 3
    return all_entries[:max_results]

def extract_text():
    return

def summarise_text():
    return

def summarise_with_openai():
    return

# summarise_with_ollama for llm switching

def article_parse():
    return


# main
def summarise_news():
    return


if __name__ == "__main__":
    summarise_news()

