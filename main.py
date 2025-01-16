from fasthtml.common import *
from blog import get_blog_index, get_post, get_posts_by_tag, get_tag_list
from layout import root_layout

app, rt = fast_app(
    pico=False,
    hdrs=(
        Link(rel='stylesheet', href='assets/normalize.min.css', type='text/css'),
        Link(rel='stylesheet', href='assets/sakura.css', type='text/css'),
        MarkdownJS(),
        HighlightJS(langs=['python', 'javascript', 'html', 'css']),
        ))

@rt("/")
def get(req):
    return get_blog_index(req.path)

@rt("/posts/{slug}")
def get(slug:str, req):
    return get_post(slug, req.path)

@rt("/tags/{tag}")
def get(tag:str, req):
    return get_posts_by_tag(tag, req.path)

@rt("/tags")
def get(req):
    return get_tag_list(req.path)

@rt("/about")
def get(req):
    return root_layout(Titled("About", P("This is the about page.")), req.path if req else "/")

serve()
