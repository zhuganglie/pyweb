import os
import glob
import markdown
from fasthtml.common import *
import frontmatter
from post_template import post_detail_template

app, rt = fast_app(
    hdrs=(
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
                'filename': os.path.basename(filepath)
            })
    return posts

@rt("/")
def get():
    posts = get_posts()
    post_items = [Div(H2(A(post['title'], href=f"/posts/{post['filename']}")),
                      P(f"Date: {post['date']}"),
                      P(f"Tags: {', '.join(post['tags'])}")) for post in posts]
    return Titled("Blog Home", Div(A("Tags", href="/tags"), *post_items))

@rt("/posts/{filename}")
def post_detail(filename: str):
    with open(os.path.join(POSTS_DIR, filename), 'r') as f:
        content = f.read()
    post = frontmatter.load(os.path.join(POSTS_DIR, filename))
    html_content = markdown.markdown(post.content)
    return Titled("", post_detail_template(post['title'], post.get('date', 'No Date'), post.get('tags', []), html_content))

@rt("/tags")
def tags():
    posts = get_posts()
    tag_counts = {}
    for post in posts:
        for tag in post['tags']:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
    tag_items = [Div(H2(A(f"{tag} ({count})", href=f"/tag/{tag}"))) for tag, count in tag_counts.items()]
    return Titled("Tags", Div(*tag_items))

@rt("/tag/{tag}")
def tag_detail(tag: str):
    posts = get_posts()
    tagged_posts = [post for post in posts if tag in post['tags']]
    post_items = [Div(H2(A(post['title'], href=f"/posts/{post['filename']}")),
                      P(f"Date: {post['date']}"),
                      P(f"Tags: {', '.join(post['tags'])}")) for post in tagged_posts]
    return Titled(f"Posts tagged with {tag}", Div(*post_items))

serve()
