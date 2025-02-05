from fasthtml.common import Main, Header, Footer, Nav, P, B, H1, A, Ul, Li, Div, Span
from datetime import datetime
from urllib.parse import unquote

HOME = "Home"
POSTS = "Posts"
TAGS = "Tags"
ABOUT = "About"

def root_layout(content, current_path="/"):
    """
    Provides the root layout for all pages.

    Args:
        content: The content to be rendered within the layout.
        current_path: The current path of the page.

    Returns:
        The HTML for the root layout.
    """

    # Breadcrumb creation
    path_parts = [p for p in current_path.split('/') if p]
    breadcrumb_items = [A(HOME, href="/")]  # Always start with Home
    current_path_build = ''

    for part in path_parts:
        current_path_build += f'/{part}'
        display_text = unquote(part).replace('-', ' ').title()
        breadcrumb_items.append(A(display_text, href=current_path_build))

    breadcrumbs = Nav(
        Div(
            *[item for pair in zip(
                breadcrumb_items,
                ["/" for _ in range(len(breadcrumb_items) - 1)] + [""]
            ) for item in pair],
            cls="flex items-center gap-2 text-sm text-gray-600"
        ),
        cls="w-full mb-4 truncate"
    ) if path_parts else ""

    def nav_link(text, href):
        """Helper function to generate navigation links with conditional 'active' class."""
        is_active = current_path == href if href == "/" else current_path.startswith(href)
        classes = "active hover:bg-slate-100 rounded-lg py-2 px-3 transition-colors" if is_active else "hover:bg-slate-100 rounded-lg py-2 px-3 transition-colors"
        return Li(A(text, href=href, cls=classes))

    return Main(
        Header(
            H1(A("YZC", href="/", cls="no-underline text-slate-800 text-3xl lg:text-4xl font-extrabold hover:text-slate-600 transition-colors")),
            Nav(
                Ul(
                    nav_link(HOME, "/"),
                    nav_link(POSTS, "/posts"),
                    nav_link(TAGS, "/tags"),
                    nav_link(ABOUT, "/about"),
                    cls="list-none flex gap-2 sm:gap-6 text-base sm:text-lg whitespace-nowrap"
                )
            ),
            cls="flex flex-col items-center justify-center py-8 px-4 gap-8 mb-8 border-b border-slate-200"
        ),
        breadcrumbs,
        content,
        Footer(
            P(f"© {datetime.now().year}", B('YZC', cls="mx-3 text-slate-700")),
            cls="flex justify-center py-8 px-4 mt-12 text-slate-500 border-t border-slate-200"
        ),
        cls="flex flex-col items-center justify-center w-full max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 min-h-screen bg-white"
    )
