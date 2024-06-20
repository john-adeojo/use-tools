import requests
import time
import re
from html.parser import HTMLParser
from urllib.parse import quote_plus

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.results = []
        self.current_title = ""
        self.current_link = ""
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        #if tag == 'div' and ('class', '%yuRU%') in attrs:
        if tag == 'div' in attrs:
            self.current_title = ""
            self.current_link = ""
        elif tag == 'a' and self.current_title == "":
            for attr in attrs:
                if attr[0] == 'href':
                    self.current_link = attr[1]
                    break
        elif tag == 'h3':
            self.in_title = True

    def handle_data(self, data):
        if self.in_title:
            self.current_title += data

    def handle_endtag(self, tag):
        if tag == 'h3':
            self.in_title = False
        elif tag == 'div' and self.current_title and self.current_link:
            self.results.append((self.current_title, self.current_link))

def search(query, num_results=5, delay=2, max_retries=3):
    """
    Perform a web search and return the top results.
    Args:
        query (str): Search query.
        num_results (int): Number of results to return. Do at least 5 please.
        delay (int): Delay between requests in seconds.
        max_retries (int): Maximum number of retries for failed requests.
    Returns:
        list: List of top search results (title, link).
    """
    query = str(query)  # Convert query to string
    search_url = f"https://www.google.com/search?q={quote_plus(query)}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0'}
    retries = 0

    while retries < max_retries:
        try:
            with requests.get(search_url, headers=headers, timeout=10) as response:
                response.raise_for_status()
                parser = MyHTMLParser()
                parser.feed(response.text)
                return parser.results[:num_results]
        except (requests.RequestException, ValueError) as e:
            print(f"Error during search: {e}")
            retries += 1
            time.sleep(delay * (2 ** retries))

    return []