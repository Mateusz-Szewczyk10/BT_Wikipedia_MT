

import requests



request = requests.get("https://en.wikipedia.org/w/api.php?action=query&prop=langlinks&format=json&lllang=de&titles=Companion%20dog")

print(request.summary())