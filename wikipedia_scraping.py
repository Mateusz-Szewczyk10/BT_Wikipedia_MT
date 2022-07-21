

import requests
import wikipedia

print("START")
pages = 10
titles = [wikipedia.random(1) for i in range(pages)]
new_list = []

# print(titles)

new_list = ["https://de.wikipedia.org/w/api.php?action=query&prop=langlinks&format=json&lllang=de&titles=" + str(x) for x in titles]

# print(new_list)

# response = requests.get('https://de.wikipedia.org/w/api.php?action=query&prop=langlinks&format=json&lllang=en&titles=Türkei')
response_list = []
for item in new_list:
    try:
        response_list.append(requests.get(item).json())
    except:
        continue
print(response_list)



#print(json_api["query"]["pages"]["9145"]["langlinks"][0]["*"])

print("END")

response = requests.get('https://en.wikipedia.org/w/api.php?action=query&prop=langlinks&format=json&lllang=de&titles=Companion dog')

json_api = response.json()
german_list = []
for item1 in response_list:
    try:
        print("TEST:", item1)
        print("TRAIN:", next(iter(item1["query"]["pages"].values()))["langlinks"][0]["*"])
    except:
        continue
    # german_list.append(next(iter(json_api["query"]["pages"].values()))["langlinks"][0]["*"])

print(next(iter(json_api["query"]["pages"].values()))["langlinks"][0]["*"])
print(german_list)


# def Wikipedia_scraper(input):
