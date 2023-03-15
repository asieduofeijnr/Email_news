import requests
import functions


api_key = "b420b2be71fc47ddade54c5bdbac676e"

url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-02-14&sortBy=publishedAt&apiKey=" \
      "b420b2be71fc47ddade54c5bdbac676e"

#Make a request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Access the article titles and description

body = ""
for article in content["articles"]:
    body = body + article["description"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
functions.send_email(body)