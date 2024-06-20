# @author Sir Lord Dalibor JONIC, MSc BSc (c
__author__      = "Sir Lord Dalibor JONIC, MSc BSc"
__copyright__   = "BeMyInspiration 2024"
__license__     = "MIT"
__version__     = "1.0.0"
__maintainer__  = "Sir Lord Dalibor JONIC, MSc BSc"
__email__       = "dali.manu@gmail.com"
__status__      = "Production"
__description__ = "Google searcher with aration"

from duckduckgo_search import DDGS
import time
import json

def search(query, num_results=5, delay=2, max_retries=1):
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
    # Replace single quotes with double quotes
    input_str_clean = json.dumps(query)
    input_str_clean = input_str_clean.replace("'", "\"")
    # Remove any extraneous characters such as trailing quotes
    input_str_clean = input_str_clean.strip().strip("\"")
    print (query) 
 
    print (input_str_clean)
    try:
        parsed_data = json.loads(input_str_clean)
        query_content = parsed_data['query'] 
        print (parsed_data) 
        query = query_content  
        results = []
        retries = 0
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")

    while retries < max_retries:
        try:
            with DDGS() as ddgs:
                search_results = list(ddgs.text(query, max_results=num_results))
                
            for result in search_results:
                title = result['title']
                link = result['href']
                results.append((title, link))
            
            return results
        
        except Exception as e:
            print(f"Error during search: {e}")
            retries += 1
            time.sleep(delay * (2 ** retries))

    return results

# Example usage:
#query = "this is all about ai"
#search_results = search(query, num_results=5)
#print(search_results)