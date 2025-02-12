import os
import re
import math
import frontmatter
from fasthtml.common import *
from datetime import datetime
from lucide_fasthtml import Lucide
from urllib.parse import unquote, quote

POSTS_DIR = "posts"

def calculate_read_time(content):
    """Calculate the read time in minutes for given content."""
    words_per_minute = 200
    word_count = len(re.findall(r'\w+', content))
    minutes = math.ceil(word_count / words_per_minute)
    return minutes

def generate_excerpt(content, max_length=300):
    """Generate a short excerpt from the content."""
    # Remove markdown headers and special characters
    clean_content = re.sub(r'#{1,6}\s.*\n', '', content)
    clean_content = re.sub(r'[*_`]', '', clean_content)
    
    # Get first paragraph or truncate to max_length
    paragraphs = clean_content.split('\n\n')
    excerpt = next((p.strip() for p in paragraphs if p.strip()), '')
    
    if len(excerpt) > max_length:
        excerpt = excerpt[:max_length].rsplit(' ', 1)[0] + '...'
    return excerpt

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
        excerpt = generate_excerpt(post.content)
        read_time = calculate_read_time(post.content)
        
        post_items.append(Li(
            Div(
                Div(
                    Span(date_str, cls="text-base font-medium text-slate-500"),
                    Span("•", cls="mx-2 text-slate-400"),
                    Span(f"{read_time} min read", cls="text-slate-500"),
                    cls="flex items-center mb-3"
                ),
                A(post['title'], 
                  href=f"/posts/{post['slug']}", 
                  cls="text-2xl font-bold text-slate-800 hover:text-slate-600 transition-colors no-underline mb-3 block"),
                P(excerpt, cls="text-slate-600 leading-relaxed mb-4"),
                Div(*tags, cls="flex flex-wrap gap-2"),
                cls="hover:bg-slate-50 transition-colors p-6 rounded-xl"
            ),
            cls="mb-8"
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
    read_time = calculate_read_time(post.content)
    
    return root_layout(Div(Titled(post['title'],
        Div(
            Span(date_str, cls="text-base font-medium text-slate-500"),
            Span("•", cls="mx-2 text-slate-400"),
            Span(f"{read_time} min read", cls="text-slate-500"),
            cls="flex items-center mb-8"
        ),
        Div(post.content, cls="marked mt-8"),
        Div(
            P("Tags", cls="text-sm text-slate-500 mb-3"),
            Div(*tags, cls="flex flex-wrap gap-2 mb-8"),
            cls="mt-12 pt-8 border-t border-slate-100"
        )
    )), current_path if current_path else "/")

def get_posts_by_tag(tag, current_path=None):
    tag = unquote(tag)
    posts = get_posts()
    global _posts_cache
    if _posts_cache:
        posts = _posts_cache
    tagged_posts = [post for post in posts if tag in post['tags']]
    post_items = []
    for post in tagged_posts:
        tags = [A(Lucide("tag", size="12"), f"{t}", href=f"/tags/{t}", cls="flex items-center gap-1.5 text-sm px-2 py-1 bg-slate-100 rounded-full text-slate-700 hover:bg-slate-200 transition-colors") for t in post['tags']]
        date_str = post.get('date', '').strftime('%Y-%m-%d') if post.get('date') else ''
        excerpt = generate_excerpt(post.content)
        read_time = calculate_read_time(post.content)
        
        post_items.append(Li(
            Div(
                Div(
                    Span(date_str, cls="text-base font-medium text-slate-500"),
                    Span("•", cls="mx-2 text-slate-400"),
                    Span(f"{read_time} min read", cls="text-slate-500"),
                    cls="flex items-center mb-3"
                ),
                A(post['title'], 
                  href=f"/posts/{post['slug']}", 
                  cls="text-2xl font-bold text-slate-800 hover:text-slate-600 transition-colors no-underline mb-3 block"),
                P(excerpt, cls="text-slate-600 leading-relaxed mb-4"),
                Div(*tags, cls="flex flex-wrap gap-2"),
                cls="hover:bg-slate-50 transition-colors p-6 rounded-xl"
            ),
            cls="mb-8"
        ))
    return root_layout(
        Div(
            Titled(f"Posts tagged with '{tag}'"),
            P(f"{len(tagged_posts)} post{'' if len(tagged_posts) == 1 else 's'}", cls="text-slate-500 mb-8"),
            Ul(*post_items, cls="mt-8")
        ), 
        current_path if current_path else "/"
    )

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
