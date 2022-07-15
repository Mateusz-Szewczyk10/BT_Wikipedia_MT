

import requests
import wikipedia

pages = 500
titles = [wikipedia.random(1) for i in range(pages)]

print(titles)

new_list = "'https://de.wikipedia.org/w/api.php?action=query&prop=langlinks&format=json&lllang=en&titles=" + titles + "'"

print(new_list)

response = requests.get('https://de.wikipedia.org/w/api.php?action=query&prop=langlinks&format=json&lllang=en&titles=Türkei')

# print(response.text)

json_api = response.json()

#print(json_api["query"]["pages"]["9145"]["langlinks"][0]["*"])