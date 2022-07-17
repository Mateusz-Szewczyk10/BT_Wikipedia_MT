

import requests
import wikipedia

print("START")
pages = 10
titles = [wikipedia.random(1) for i in range(pages)]
new_list = []

print(titles)

new_list = ["'https://en.wikipedia.org/w/api.php?action=query&prop=langlinks&format=json&lllang=de&titles=" + str(x) + "'" for x in titles]

print(new_list)

# response = requests.get('https://de.wikipedia.org/w/api.php?action=query&prop=langlinks&format=json&lllang=en&titles=Türkei')

# print(response.text)

# json_api = response.json()

#print(json_api["query"]["pages"]["9145"]["langlinks"][0]["*"])

print("END")