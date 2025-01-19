from fasthtml.common import *
from blog import get_blog_index, get_post, get_posts_by_tag, get_tag_list
from layout import root_layout

app, rt = fast_app(
    pico=False,
    hdrs=(
    #   Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/normalize.css@8.0.1/normalize.min.css", type="text/css"),
    #   Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/sakura.css/css/sakura.css', type='text/css'),
        Link(rel='stylesheet', href='/public/marked.css', type='text/css'),
        MarkdownJS(),
        HighlightJS(langs=['python', 'javascript', 'html', 'css']),
        Script(src="https://cdn.tailwindcss.com"),
        Style(
            ".active { font-weight: bold;}",
            )
    ))

@rt("/")
def index(req):  # Changed function name to be more descriptive
    return get_blog_index(req.url.path)

@rt("/posts/{slug}")
def get(slug: str, req):  # Changed function name to be more descriptive
    return get_post(slug, req.url.path)

@rt("/tags/{tag}")
def posts_by_tag(tag: str, req):  # Changed function name to be more descriptive
    return get_posts_by_tag(tag, req.url.path)

@rt("/tags")
def tag_list(req):  # Changed function name to be more descriptive
    return get_tag_list(req.url.path)

@rt("/about")
def about(req):  # Changed function name to be more descriptive
    return root_layout(
        Titled("About", P("This blog explores why we live the way we live.")),
        req.url.path if req else "/"
    )

if __name__ == "__main__":  # Added standard Python idiom
    serve()
