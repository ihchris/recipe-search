from flask import Flask, render_template, request
import requests

app = Flask(__name__)

APP_ID = 'YOUR_EDAMAM_APP_ID'  # Replace with your Edamam App ID
API_KEY = 'YOUR_EDAMAM_API_KEY'  # Replace with your Edamam API Key
API_URL = 'https://api.edamam.com/search'

@app.route('/', methods=['GET', 'POST'])
def home():
    query = request.form.get('query')
    if query:
        url = f"{API_URL}?q={query}&app_id={APP_ID}&app_key={API_KEY}"
        response = requests.get(url)
        recipes = response.json().get('hits', [])
    else:
        recipes = []
    return render_template('index.html', recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True)
