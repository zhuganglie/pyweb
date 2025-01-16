from fasthtml.common import *
from blog import get_blog_index, get_post

app, rt = fast_app(hdrs=(MarkdownJS(), HighlightJS(langs=['python', 'javascript', 'html', 'css']), ))

@rt("/")
def get():
    return get_blog_index()

@rt("/posts/{slug}")
def get(slug:str):
    return get_post(slug)

serve()
