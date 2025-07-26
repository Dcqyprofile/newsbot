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

# fetch the articles! Connects to an RSS feed and collect all recent article URLs
# Get a bunch of Recent url links but not article itself
def fetch_articles(source = None, max_results = 10):
    # source is what user wants -> techcrunch etc
    feeds = [RSS_FEEDS.get(source) if source else RSS_FEEDS.values()]
    all_entries = []
    # parse XML format into readable form
    for url in feeds:
        # converts XML format into python readable dictionary format
        feed = feedparser.parse(url)
        for entry in feed.entries():
            all_entries.append({
                "title": entry.title,
                "link": entry.link
            })
    return all_entries[:max_results]

# extract the text!
# parsing actual article page
def extract_text(url):
    try:
        # Article scraps and extracts content
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        return f"[error extracting article] {e}"
        

# summarise it for me!
def summarise_text():
    return

# semantic filtering using prompts
def semantic_filter():
    return

# use summarise text inside of openai
def summarise_with_openai():
    prompt = "Extract the most important information and present it as a bullet-point list:\n\n{text[:4000]}"
    try:
        response = openai.ChatCompletion.create()
    return

# summarise_with_ollama for llm switching

# def article_parse():
#     return


# # main
# def summarise_news():
#     return


if __name__ == "__main__":
    summarise_news()

