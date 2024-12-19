import os
import glob
import markdown
from fasthtml.common import *
import frontmatter

app, rt = fast_app()

POSTS_DIR = 'posts'

def get_posts():
    posts = []
    for filepath in glob.glob(os.path.join(POSTS_DIR, '*.md')):
        post = frontmatter.load(filepath)
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
    return Titled("Blog Home", Div(*post_items))

@rt("/posts/{filename}")
def post_detail(filename: str):
    with open(os.path.join(POSTS_DIR, filename), 'r') as f:
        content = f.read()
        html_content = markdown.markdown(content)
    return Titled("Post Detail", Div(NotStr(html_content)))

serve()
