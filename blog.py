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
                post['tags'] = post.get('tags', [])
                posts.append(post)
    return posts

def get_blog_index():
    posts = get_posts()
    post_items = []
    for post in posts:
        tags = [A(f"#{tag}", href=f"/tags/{tag}") for tag in post['tags']]
        post_items.append(Li(A(post['title'], href=f"/posts/{post['slug']}"), " ", *tags))
    return Titled("Blog Index", Ul(*post_items))

def get_post(slug):
    posts = get_posts()
    post = next((post for post in posts if post['slug'] == slug), None)
    if not post:
        return Titled("Post not found", P("Sorry, the post you requested was not found."))
    tags = [A(f"#{tag}", href=f"/tags/{tag}") for tag in post['tags']]
    return Titled(post['title'], Div(post.content, cls="marked"), P(*tags))
def get_posts_by_tag(tag):
    posts = get_posts()
    tagged_posts = [post for post in posts if tag in post['tags']]
    post_items = [Li(A(post['title'], href=f"/posts/{post['slug']}")) for post in tagged_posts]
    return Titled(f"Posts tagged with '{tag}'", Ul(*post_items))
