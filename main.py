from fasthtml.common import *
from blog import get_posts, render_post, render_index, get_tags, render_tag_index

app, rt = fast_app(
    hdrs=(MarkdownJS(), HighlightJS(langs=['python', 'javascript', 'html', 'css']), )
)

posts = get_posts()

@rt("/")
def index():
    return render_index(posts)

@rt("/post/{slug}")
def get(slug: str):
    for post in posts:
        if post.metadata['slug'] == slug:
            return render_post(post)
    return "Post not found"

@rt("/tag/{tag}")
def tag(tag: str):
    return render_tag_index(posts, tag)

@rt("/tags")
def tags():
    links = [Li(A(tag, href=f"/tag/{tag}")) for tag in get_tags(posts)]
    return Titled("Tags", Ul(*links))

serve()
