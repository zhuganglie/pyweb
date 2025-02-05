import os
import frontmatter
from fasthtml.common import *
from datetime import datetime
from lucide_fasthtml import Lucide
from urllib.parse import unquote, quote

POSTS_DIR = "posts"

# Add a cache for posts to avoid reading from disk every time
_posts_cache = None

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
    global _posts_cache
    _posts_cache = posts # Cache the loaded posts

    return posts

from layout import root_layout

def get_blog_index(current_path=None):
    posts = get_posts()
    post_items = []
    global _posts_cache
    if _posts_cache:
        posts = _posts_cache
    for post in posts:
        tags = [A(Lucide("tag", size="12"), f"{tag}", href=f"/tags/{tag}", cls="flex items-center gap-1.5 text-sm px-2 py-1 bg-slate-100 rounded-full text-slate-700 hover:bg-slate-200 transition-colors") for tag in post['tags']]
        date_str = post.get('date', '').strftime('%Y-%m-%d') if post.get('date') else ''
        post_items.append(Li(
            P(date_str, cls="mb-2 text-sm text-slate-600"),
            A(post['title'], href=f"/posts/{post['slug']}", cls="text-xl font-semibold text-slate-800 hover:text-slate-600 transition-colors no-underline"),
            " ",
            Div(*tags, cls="flex flex-wrap gap-2 mt-3"),
            cls="mb-8 pb-6 border-b border-slate-100 last:border-0"
        ))
    return root_layout(Ul(*post_items), current_path if current_path else "/")

def get_post(slug, current_path=None):
    posts = get_posts()
    global _posts_cache
    if _posts_cache:
        posts = _posts_cache
    post = next((post for post in posts if post['slug'] == slug), None)
    if not post:
        return Titled("Post not found", P("Sorry, the post you requested was not found."))
    tags = [A(Lucide("tag", size="15"), f"{tag}", href=f"/tags/{tag}", cls="flex items-center gap-1.5 px-3 py-1.5 bg-slate-100 rounded-full text-slate-700 hover:bg-slate-200 transition-colors") for tag in post['tags']]
    date_str = post.get('date', '').strftime('%Y-%m-%d') if post.get('date') else ''
    return root_layout(Div(Titled(post['title'],
        P(date_str, cls="my-4 text-slate-600"),
        Div(post.content, cls="marked mt-12"),
        P("Tags:", cls="text-slate-700 font-medium mt-12 mb-3"),
        Div(*tags, cls="flex flex-wrap gap-2 mb-8")
    )), current_path if current_path else "/")

def get_posts_by_tag(tag, current_path=None):
    tag = unquote(tag)
    posts = get_posts()
    global _posts_cache
    if _posts_cache:
        posts = _posts_cache
    tagged_posts = [post for post in posts if tag in post['tags']]
    post_items = [Li(A(post['title'], href=f"/posts/{post['slug']}", cls="text-slate-800 hover:text-slate-600 transition-colors"), cls="list-disc list-inside mb-3 text-lg") for post in tagged_posts]
    return root_layout(Titled(f"Posts tagged with '{tag}'", Ul(*post_items, cls="mt-8")), current_path if current_path else "/")

def get_all_tags():
    posts = get_posts()
    tags = set()
    global _posts_cache
    if _posts_cache:
        posts = _posts_cache
    for post in posts:
        tags.update(post['tags'])
    return tags

def get_tag_list(current_path=None):
    posts = get_posts()
    tags = get_all_tags()
    global _posts_cache
    if _posts_cache:
        posts = _posts_cache
    tag_counts = {}
    for post in posts:
        for tag in post['tags']:
            decoded_tag = unquote(tag)
            tag_counts[decoded_tag] = tag_counts.get(decoded_tag, 0) + 1
    tag_items = [Li(A(f"{tag} ({tag_counts[tag]})", href=f"/tags/{quote(tag)}", cls="inline-flex items-center px-4 py-2 bg-slate-100 rounded-full text-slate-700 hover:bg-slate-200 transition-colors")) for tag in tags]
    return root_layout(Titled("All Tags", Ul(*tag_items, cls="mt-8 flex flex-wrap gap-3 list-none")), current_path if current_path else "/")
