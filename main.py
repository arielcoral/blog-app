from flask import Flask, render_template
import requests

app = Flask(__name__)

def req():
    url = "https://api.npoint.io/dfe0ea69d6ec08c8f4a0"
    response = requests.get(url)
    posts = response.json()
    return posts

@app.route('/')
def home():
    posts = req()
    return render_template("index.html", posts=posts)

@app.route('/post/<int:num>')
def post(num):
    url = "https://api.npoint.io/dfe0ea69d6ec08c8f4a0"
    response = requests.get(url)
    posts = response.json()
    the_post = None
    for post in posts:
        if post['id'] == num:
            the_post = post
            break
    return render_template("post.html", hpost=the_post)

if __name__ == "__main__":
    app.run(debug=True)
