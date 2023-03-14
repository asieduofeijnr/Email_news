import requests

api_key = "b420b2be71fc47ddade54c5bdbac676e"

url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-02-14&sortBy=publishedAt&apiKey=" \
      "b420b2be71fc47ddade54c5bdbac676e"

#Make a request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Access the article titles and description
a = 0
for article in content["articles"]:
    print(a + 1,"-----", article["title"])
    print(a + 1,"-----", article["description"])
    print(a + 1,"-----", article["content"] + "\n")
    a = a + 1