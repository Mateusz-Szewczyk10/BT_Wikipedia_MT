

import requests



# request = requests.get("https://en.wikipedia.org/w/api.php?action=query&prop=langlinks&format=json&lllang=de&titles=Companion%20dog")

request = requests.get("https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=&explaintext=&titles=Albert+Einstein&format=json&prop=langlinks&lllang=de")

print(request.json())