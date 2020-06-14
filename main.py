from flask import Flask,render_template
from darksky.api import DarkSky
import requests

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/list"

querystring = {"category":"generalnews","region":"IN"}

headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "5b9fba41ddmsh2f2caea5dd3684bp13a7a2jsna70b2449b028"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

l = response.json()
news = []
for i in range(10):
    a = l["items"]["result"][i]
    news.append([a["title"],a["link"]])
app = Flask(__name__)

@app.route("/")
def index():
    title = "Homepage"
    finance_news = news
    return render_template("index.html",title=title,news = finance_news)

