import os
import frontmatter
from fasthtml.components import Titled, Div, H2, Li, A, Ul

POSTS_DIR = "posts"

def get_posts():
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            with open(os.path.join(POSTS_DIR, filename), 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                post.metadata['slug'] = filename[:-3]
                posts.append(post)
    return posts

def render_post(post):
    return Titled(
        post["title"],
        Div(
            H2(post["title"], cls="text-2xl font-bold mb-4"),
            Div(f"Tags: {', '.join(post.get('tags', []))}", cls="text-gray-600 mb-4"),
            Div(post.content, cls="markdown prose"),
        ),
    )

def render_index(posts):
    links = [
        Li(A(post["title"], href=f"/post/{post.metadata['slug']}"))
        for post in posts
    ]
    return Titled("Blog Index", Ul(*links))

def get_tags(posts):
    tags = set()
    for post in posts:
        tags.update(post.get('tags', []))
    return sorted(list(tags))

def render_tag_index(posts, tag):
    links = [
        Li(A(post["title"], href=f"/post/{post.metadata['slug']}"))
        for post in posts
        if tag in post.get("tags", [])
    ]
    return Titled(f"Posts tagged with {tag}", Ul(*links))
