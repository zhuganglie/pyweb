from fasthtml.common import *
from blog import load_posts, get_post

app, rt = fast_app()

@rt('/')
def index():
    posts = load_posts()
    return Titled("Blog Index",  Template("templates/index.html", posts=posts))

@rt('/post/{post_name}')
def post(post_name):
    post = get_post(post_name)
    if post:
        return Titled(post['title'], Template("templates/post.html", **post))
    return  Titled("Not found", P("That post does not exist"))

serve()
