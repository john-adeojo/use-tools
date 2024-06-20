from duckduckgo_search import DDGS

results = DDGS().text("python programming", max_results=3)
print(results)