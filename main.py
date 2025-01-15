import os
import frontmatter
import fasthtml
from jinja2 import Environment, FileSystemLoader

# Directory containing the blog posts
POSTS_DIR = 'posts'
TEMPLATES_DIR = 'templates'

# Initialize Jinja2 environment
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

def parse_posts():
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith('.md'):
            with open(os.path.join(POSTS_DIR, filename), 'r') as file:
                post = frontmatter.load(file)
                posts.append({
                    'title': post['title'],
                    'tags': post['tags'],
                    'content': fasthtml.markdown(post.content),
                    'url': f"/posts/{filename.replace('.md', '.html')}"
                })
    return posts

def generate_post_html(post):
    template = env.get_template('post.html')
    return template.render(title=post['title'], content=post['content'], tags=post['tags'])

def generate_index_html(posts):
    template = env.get_template('index.html')
    return template.render(posts=posts)

def main():
    posts = parse_posts()

    # Generate HTML for each post
    for post in posts:
        html_content = generate_post_html(post)
        with open(f"output/posts/{post['url'].replace('/posts/', '')}", 'w') as file:
            file.write(html_content)

    # Generate index HTML
    index_html = generate_index_html(posts)
    with open('output/index.html', 'w') as file:
        file.write(index_html)

if __name__ == '__main__':
    main()
