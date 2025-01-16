import os
import frontmatter
from fasthtml.common import *

POSTS_DIR = "posts"

def get_posts():
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            with open(os.path.join(POSTS_DIR, filename), 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                post['slug'] = filename[:-3]
                posts.append(post)
    return posts

def get_blog_index():
    posts = get_posts()
    post_items = [Li(A(post['title'], href=f"/posts/{post['slug']}")) for post in posts]
    return Titled("Blog Index", Ul(*post_items))

def get_post(slug):
    posts = get_posts()
    post = next((post for post in posts if post['slug'] == slug), None)
    if not post:
        return Titled("Post not found", P("Sorry, the post you requested was not found."))
    return Titled(post['title'], Div(post.content, cls="marked"))
