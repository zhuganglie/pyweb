
import os
import markdown
from flask import Flask, render_template

app = Flask(__name__)
POSTS_DIR = "posts"

def get_posts():
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            with open(os.path.join(POSTS_DIR, filename), 'r') as f:
                content = f.read()
                html = markdown.markdown(content)
                title = filename[:-3].replace('-', ' ').title()
                tags = [tag.strip() for tag in extract_tags(content)]
                url = f"/post/{filename[:-3]}"
                posts.append({"title": title, "content": html, "tags": tags, "url": url})
    return posts

def extract_tags(content):
    lines = content.splitlines()
    for line in lines:
        if line.startswith("tags:"):
            return line[5:].split(",")
    return []

@app.route("/")
def index():
    posts = get_posts()
    return render_template("index.html", posts=posts)

@app.route("/post/<post_name>")
def post(post_name):
     posts = get_posts()
     for post in posts:
        if post["url"] == f"/post/{post_name}":
            return render_template("post.html", post=post)
     return "Post not found", 404

if __name__ == "__main__":
    app.run(debug=True)
