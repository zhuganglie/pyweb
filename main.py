from fasthtml.common import *
from blog import load_posts, get_post

app, rt = fast_app()

@rt('/')
def index():
    posts = load_posts()
    return Titled("Blog Index", Div(posts=posts, template="templates/index.html"))

@rt('/post/{post_name}')
def post(post_name):
    post = get_post(post_name)
    if not post: return _not_found()
    return Titled(post['title'], Div(post=post, template="templates/post.html"))

def _not_found(): return Titled('Oh no!', Div('We could not find that page :('))

serve()
