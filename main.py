import os
import glob
import markdown
from fasthtml.common import *
import frontmatter
from post_template import post_detail_template
import datetime

def navbar():
    return Div(
        A("Home", href="/",  **{"class": "text-lg font-semibold text-gray-800 hover:text-gray-600"}),
        " | ",
        A("Tags", href="/tags", **{"class": "text-lg font-semibold text-gray-800 hover:text-gray-600"}),
        style="text-align: center; margin-bottom: 25px; padding: 10px;"
    )

from fasthtml.core import serve
from fasthtml.common import Titled, Link

app, rt = fast_app(
    head=(
        Link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/tailwindcss@3.4.1/tailwind.min.css",
            type="text/css",
        ),
    )
)

POSTS_DIR = 'posts'

def get_posts():
    posts = []
    for filepath in glob.glob(os.path.join(POSTS_DIR, '*.md')):
        post = frontmatter.load(filepath)
        if post.get('draft') != True:
            posts.append({
                'title': post['title'],
                'date': post.get('date', 'No Date'),
                'tags': post.get('tags', []),
                'filename': os.path.basename(filepath),

            })
    posts.sort(key=lambda post: datetime.datetime.strptime(post['date'], '%Y-%m-%d') if post['date'] != 'No Date' else datetime.datetime.min, reverse=True)
    return posts

@rt("/")
def get():
    posts = get_posts()
    post_items = [Div(H2(A(post['title'], href=f"/posts/{post['filename']}", **{"class": "text-2xl font-bold hover:text-blue-700"})),
                      P(f"Date: {post['date']}", **{"class": "text-gray-600"}),
                      P(f"Tags: {', '.join(post['tags'])}", **{"class": "text-gray-500"})) for post in posts]
    return Titled("AI's Blog", Div(navbar(), *post_items, **{"class": "max-w-3xl mx-auto px-4 sm:px-6 lg:px-8"}))

@rt("/posts/{filename}")
def post_detail(filename: str):
    with open(os.path.join(POSTS_DIR, filename), 'r') as f:
        content = f.read()
    post = frontmatter.load(os.path.join(POSTS_DIR, filename))
    html_content = markdown.markdown(post.content)
    return Titled("", Div(navbar(), post_detail_template(post['title'], post.get('date', 'No Date'), post.get('tags', []), html_content), **{"class": "max-w-3xl mx-auto px-4 sm:px-6 lg:px-8"}))

@rt("/tags")
def tags():
    posts = get_posts()
    tag_counts = {}
    for post in posts:
        for tag in post['tags']:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
    tag_items = [Div(H2(A(f"{tag} ({count})", href=f"/tag/{tag}", **{"class": "text-xl font-semibold hover:text-blue-700"}))) for tag, count in tag_counts.items()]
    return Titled("Tags", Div(navbar(), *tag_items, **{"class": "max-w-3xl mx-auto px-4 sm:px-6 lg:px-8"}))

@rt("/tag/{tag}")
def tag_detail(tag: str):
    posts = get_posts()
    tagged_posts = [post for post in posts if tag in post['tags']]
    post_items = [Div(H2(A(post['title'], href=f"/posts/{post['filename']}", **{"class": "text-2xl font-bold hover:text-blue-700"})),
                      P(f"Date: {post['date']}", **{"class": "text-gray-600"}),
                      P(f"Tags: {', '.join(post['tags'])}", **{"class": "text-gray-500"})) for post in tagged_posts]
    return Titled(f"Posts tagged with {tag}", Div(navbar(), *post_items, **{"class": "max-w-3xl mx-auto px-4 sm:px-6 lg:px-8"}))

serve()
