from fasthtml.fastapp import fast_app
from fasthtml.components import Div, H2, Li, A, Ul, Link, Style
from fasthtml.js import MarkdownJS, HighlightJS
from blog import get_posts, render_post, render_index, get_tags, render_tag_index
from fasthtml.core import serve
from nav import navbar
from layout import layout

app, rt = fast_app(
    hdrs=(
        Link(
            href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
            rel="stylesheet",
        ),
        MarkdownJS(),
        HighlightJS(langs=["python", "javascript", "html", "css"]),
        Style("""
            .markdown h1 { @apply text-3xl font-bold mb-4; }
            .markdown h2 { @apply text-2xl font-semibold mb-3; }
            .markdown h3 { @apply text-xl font-semibold mb-2; }
            .markdown p { @apply mb-2; }
            .markdown ul { @apply list-disc list-inside mb-2; }
            .markdown ol { @apply list-decimal list-inside mb-2; }
            .markdown li { @apply mb-1; }
            .markdown a { @apply text-blue-500 hover:underline; }
            .markdown code { @apply bg-gray-100 px-2 py-1 rounded; }
            .markdown pre { @apply bg-gray-100 p-4 rounded overflow-x-auto; }
            .markdown blockquote { @apply border-l-4 border-gray-300 pl-4 italic mb-2; }
        """)
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
