import os
import frontmatter
from fasthtml.common import *
from datetime import datetime
from lucide_fasthtml import Lucide
from urllib.parse import unquote

POSTS_DIR = "posts"

def get_posts():
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            with open(os.path.join(POSTS_DIR, filename), 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                post['slug'] = filename[:-3]
                post['tags'] = post.get('tags', [])
                date = post.get('date', None)
                if date:
                    try:
                        post['date'] = datetime.fromisoformat(str(date))
                    except ValueError:
                        post['date'] = datetime.min
                if post.get('draft') == True:
                    continue
                posts.append(post)
    posts.sort(key=lambda post: post.get('date', datetime.min), reverse=True)
    return posts

from layout import root_layout

def get_blog_index(current_path=None):
    posts = get_posts()
    post_items = []
    for post in posts:
        tags = [A( Lucide("tag", size="12"), f"{tag}", href=f"/tags/{tag}", cls=" flex items-center gap-1 text-sm") for tag in post['tags']]
        date_str = post.get('date', '').strftime('%Y-%m-%d') if post.get('date') else ''
        post_items.append(Li(
            P(date_str, cls="mb-2 text-sm "),
            A(post['title'], href=f"/posts/{post['slug']}", cls="no-underline text-xl"),
            " ",
            Div( *tags, cls="flex gap-2 mt-2"),
            cls="mb-5 gap-4"
        ))
    return root_layout(Ul(*post_items), current_path if current_path else "/")

def get_post(slug, current_path=None):
    posts = get_posts()
    post = next((post for post in posts if post['slug'] == slug), None)
    if not post:
        return Titled("Post not found", P("Sorry, the post you requested was not found."))
    tags = [A(Lucide("tag", size="15"), f"{tag}", href=f"/tags/{tag}", cls="flex items-center gap-1 ") for tag in post['tags']]
    date_str = post.get('date', '').strftime('%Y-%m-%d') if post.get('date') else ''
    return root_layout(Div(Titled(post['title'], P(date_str, cls="my-4"), Div(post.content, cls="marked"), P(*tags, cls="flex gap-2 my-2"))), current_path if current_path else "/")

def get_posts_by_tag(tag, current_path=None):
    tag = unquote(tag)
    posts = get_posts()
    tagged_posts = [post for post in posts if tag in post['tags']]
    post_items = [Li(A(post['title'], href=f"/posts/{post['slug']}"), cls="list-disc list-inside mb-2") for post in tagged_posts]
    return root_layout(Titled(f"Posts tagged with '{tag}'", Ul(*post_items, cls="mt-8")), current_path if current_path else "/")

def get_all_tags():
    posts = get_posts()
    tags = set()
    for post in posts:
        tags.update(post['tags'])
    return tags

def get_tag_list(current_path=None):
    posts = get_posts()
    tags = get_all_tags()
    tag_counts = {}
    for post in posts:
        for tag in post['tags']:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
    tag_items = [Li(A(f"{tag} ({tag_counts[tag]})", href=f"/tags/{tag}")) for tag in tags]
    return root_layout(Titled("All Tags", Ul(*tag_items, cls="mt-8 flex flex-wrap gap-4 list-none")), current_path if current_path else "/")
