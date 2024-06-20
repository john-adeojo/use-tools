from duckduckgo_search import DDGS

def search(query, num_results=5, delay=2, max_retries=3):
    """
    Perform a web search using DuckDuckGo and return the top results.
    Args:
        query (str): Search query.
        num_results (int): Number of results to return. At least 5.
        delay (int): Delay between retries in seconds.
        max_retries (int): Maximum number of retries for failed requests.
    Returns:
        list: List of top search results (title, link).
    """ 
    results = DDGS().text(query, max_results=num_results)
    return results

#print(results)