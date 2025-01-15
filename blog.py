import os
import markdown
import yaml
from fasthtml.common import *

POSTS_DIR = "posts"

def load_posts():
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            with open(os.path.join(POSTS_DIR, filename), 'r', encoding='utf-8') as f:
                content = f.read()
                try:
                    frontmatter, markdown_content = content.split('---', 2)[1:]
                    metadata = yaml.safe_load(frontmatter)
                    html_content = markdown.markdown(markdown_content)
                    posts.append({
                        'title': metadata.get('title', 'No Title'),
                        'content': html_content,
                        'tags': metadata.get('tags', []),
                        'url': f'/post/{filename[:-3]}'
                    })
                except ValueError:
                    html_content = markdown.markdown(content)
                    posts.append({
                        'title': filename[:-3],
                        'content': html_content,
                        'tags': [],
                        'url': f'/post/{filename[:-3]}'
                    })
    return posts

def get_post(post_name):
    for filename in os.listdir(POSTS_DIR):
        if filename.startswith(post_name) and filename.endswith(".md"):
            with open(os.path.join(POSTS_DIR, filename), 'r', encoding='utf-8') as f:
                content = f.read()
                try:
                    frontmatter, markdown_content = content.split('---', 2)[1:]
                    metadata = yaml.safe_load(frontmatter)
                    html_content = markdown.markdown(markdown_content)
                    return {
                        'title': metadata.get('title', 'No Title'),
                        'content': html_content,
                        'tags': metadata.get('tags', [])
                    }
                except ValueError:
                    html_content = markdown.markdown(content)
                    return {
                        'title': filename[:-3],
                        'content': html_content,
                        'tags': []
                    }
    return None
