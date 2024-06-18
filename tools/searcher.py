# @author Sir Lord Dalibor JONIC, MSc BSc (c
__author__      = "Sir Lord Dalibor JONIC, MSc BSc"
__copyright__   = "BeMyInspiration 2024"
__license__     = "MIT"
__version__     = "1.0.0"
__maintainer__  = "Sir Lord Dalibor JONIC, MSc BSc"
__email__       = "dali.manu@gmail.com"
__status__      = "Production"
__description__ = "Google searcher with aration"

import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

def search(query, num_results=5, delay=2, max_retries=3):
    """
    Perform a web search and return the top results.
    Args:
        query (str): Search query.
        num_results (int): Number of results to return. Do at least 2 please.
        delay (int): Delay between requests in seconds.
        max_retries (int): Maximum number of retries for failed requests.
    Returns:
        list: List of top search results (title, link).
    """
    query = str(query)  # Convert query to string
    search_url = f"https://www.google.com/search?q={quote_plus(query)}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0'}
    results = []
    retries = 0

    while retries < max_retries:
        try:
            with requests.get(search_url, headers=headers, timeout=10) as response:
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "html.parser")
                result_divs = soup.find_all('div', class_='yuRUbf')
                for result in result_divs[:num_results]:
                    title = result.find('h3').get_text()
                    link = result.find('a')['href']
                    results.append((title, link))
                return results
        except (requests.RequestException, ValueError) as e:
            print(f"Error during search: {e}")
            retries += 1
            time.sleep(delay * (2 ** retries))

    return results