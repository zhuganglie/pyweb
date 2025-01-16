from fasthtml.common import *
from blog import get_blog_index, get_post, get_posts_by_tag, get_tag_list
from layout import root_layout

app, rt = fast_app(hdrs=(MarkdownJS(), HighlightJS(langs=['python', 'javascript', 'html', 'css']), ))

@rt("/")
def get():
    return get_blog_index()

@rt("/posts/{slug}")
def get(slug:str):
    return get_post(slug)

@rt("/tags/{tag}")
def get(tag:str):
    return get_posts_by_tag(tag)

@rt("/tags")
def get():
    return get_tag_list()

@rt("/about")
def get():
    return root_layout(Titled("About", P("This is the about page.")))

serve()
