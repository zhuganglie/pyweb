from fasthtml.fastapp import fast_app
from fasthtml.components import Div, H2, Li, A, Ul, Link
from fasthtml.js import MarkdownJS, HighlightJS
from blog import get_posts, render_post, render_index, get_tags, render_tag_index
from fasthtml.core import serve
from nav import navbar
from layout import layout

app, rt = fast_app(
    hdrs=(
        MarkdownJS(),
        HighlightJS(langs=["python", "javascript", "html", "css"]),
    )
)

posts = get_posts()

@rt("/")
def index():
    return layout("Blog Index", render_index(posts))

@rt("/post/{slug}")
def get(slug: str):
    for post in posts:
        if post.metadata['slug'] == slug:
            return layout(render_post(post))
    return "Post not found"

@rt("/tag/{tag}")
def tag(tag: str):
    return layout(f"Posts tagged with {tag}", render_tag_index(posts, tag))

@rt("/tags")
def tags():
    links = [Li(A(tag, href=f"/tag/{tag}")) for tag in get_tags(posts)]
    return layout("Tags", Ul(*links))

serve()
