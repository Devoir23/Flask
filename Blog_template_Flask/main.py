from flask import Flask, render_template
import requests
import random
import datetime
from post import Post

url = "https://api.npoint.io/c790b4d5cab58020d391"
posts = requests.get(url).json()
posts_objets = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    posts_objets.append(post_obj)

current_year = datetime.datetime.now().year
app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts_objets, year=current_year)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts_objets:
        if blog_post.id == index:
            requested_post=blog_post
    return render_template("post.html", post=requested_post, year=current_year)

if __name__ == "__main__":
    app.run(debug=True)
