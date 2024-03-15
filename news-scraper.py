from flask import Flask, render_template, request
import requests
import config

app = Flask(__name__)

def get_company_news(company_name, api_key):
    """
    Fetches news articles about a company using the News API.
    """
    url= f"https://newsapi.org/v2/everything?q={company_name}&apiKey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data["articles"]
        return articles
    else:
        print(f"Error: {response.status_code}")
        return []
    
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        company_name = request.form['company']
        news_articles = get_company_news(company_name, config.NEWS_API_KEY)
        return render_template('results.html', company=company_name.capitalize(), articles=news_articles)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)