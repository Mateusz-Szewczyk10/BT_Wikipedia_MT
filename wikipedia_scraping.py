

import requests
import wikipedia
import time

start_time = time.time()
pages = 1000
titles = [wikipedia.random(1) for i in range(pages)]
new_list = []
response_list = []
german_list = []

new_list = ["https://en.wikipedia.org/w/api.php?action=query&prop=langlinks&format=json&lllang=de&titles=" + str(x) for x in titles]


for item in new_list:
    try:
        response_list.append(requests.get(item).json())
    except:
        continue

# print(response_list)

for item1 in response_list:
    try:
        print("{{'German Title':", next(iter(item1["query"]["pages"].values()))["langlinks"][0]["*"], "}, {'English Title':", next(iter(item1["query"]["pages"].values()))["title"], "}}")
        german_list.append("{'German Title':", next(iter(item1["query"]["pages"].values()))["langlinks"][0]["*"], "}, {'English Title':", next(iter(item1["query"]["pages"].values()))["title"], "}}")
    except:
        continue

print(german_list)


# def Wikipedia_scraper(input):


print(time.time() - start_time, "seconds")