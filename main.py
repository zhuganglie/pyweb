import os
import markdown
from fasthtml.common import *

app, rt = fast_app()

POSTS_DIR = 'posts'

def get_posts():
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith('.md'):
            with open(os.path.join(POSTS_DIR, filename), 'r') as f:
                content = f.read()
                title, date, tags = extract_metadata(content)
                posts.append({'title': title, 'date': date, 'tags': tags, 'filename': filename})
    return posts

def extract_metadata(content):
    lines = content.splitlines()
    title = lines[0].replace('# ', '')
    date = lines[1].replace('Date: ', '')
    tags = lines[2].replace('Tags: ', '').split(', ')
    return title, date, tags

@rt("/")
def get():
    posts = get_posts()
    post_items = [Div(H2(A(post['title'], href=f"/posts/{post['filename']}")), 
                      P(f"Date: {post['date']}"), 
                      P(f"Tags: {', '.join(post['tags'])}")) for post in posts]
    return Titled("Blog Home", Div(*post_items))

@rt("/posts/{filename}")
def post_detail(filename: str):
    with open(os.path.join(POSTS_DIR, filename), 'r') as f:
        content = f.read()
        html_content = markdown.markdown(content)
    return Titled("Post Detail", Div(NotStr(html_content)))

serve()
