from fasthtml.common import Main, Header, Footer, Nav, P, B, H1, H2, H3, H4, H5, H6, A, Ul, Li, Div, Span, Button
from datetime import datetime
from urllib.parse import unquote
from lucide_fasthtml import Lucide

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
            cls="flex items-center gap-2 text-sm text-gray-600 dark:text-gray-400"
        ),
        cls="w-full mb-4 truncate"
    ) if path_parts else ""

    def nav_link(text, href):
        """Helper function to generate navigation links with conditional 'active' class."""
        is_active = current_path == href if href == "/" else current_path.startswith(href)
        classes = "active text-primary-600 dark:text-primary-400 font-semibold" if is_active else "text-slate-600 dark:text-slate-400 hover:text-primary-600 dark:hover:text-primary-400 transition-colors"
        return Li(A(text, href=href, cls=classes))

    # Theme toggle button
    theme_toggle = Button(
        Span(Lucide("sun", size="20"), cls="sun-icon hidden"),
        Span(Lucide("moon", size="20"), cls="moon-icon"),
        id="theme-toggle",
        cls="p-2 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-700 transition-colors focus:outline-none focus:ring-2 focus:ring-indigo-500",
        title="Toggle dark mode",
        **{"aria-label": "Toggle dark mode"}
    )

    # Skip to content link for accessibility
    skip_link = A(
        "Skip to main content",
        href="#main-content",
        cls="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:z-50 focus:px-4 focus:py-2 focus:bg-indigo-600 focus:text-white focus:rounded-lg focus:shadow-lg transition-all"
    )

    return Main(
        skip_link,
        Div(id="reading-progress", cls="fixed top-0 left-0 h-1 bg-primary-600 dark:bg-primary-400 z-[60] transition-all duration-300", style="width: 0%"),
        Header(
            Div(
                H1(A("YZC", href="/", cls="no-underline text-slate-800 dark:text-slate-100 text-2xl lg:text-3xl font-extrabold hover:text-primary-600 dark:hover:text-primary-400 transition-colors tracking-tight")),
                Nav(
                    Ul(
                        nav_link(HOME, "/"),
                        nav_link(POSTS, "/posts"),
                        nav_link(TAGS, "/tags"),
                        nav_link(ABOUT, "/about"),
                        cls="list-none flex gap-1 sm:gap-2 text-sm sm:text-base font-medium"
                    ),
                    cls="hidden md:block"
                ),
                Div(
                    theme_toggle,
                    # Mobile menu button could go here
                    cls="flex items-center gap-2"
                ),
                cls="flex items-center justify-between w-full max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 h-16"
            ),
            cls="fixed top-0 left-0 right-0 z-50 glass transition-all duration-300"
        ),
        Div(
            breadcrumbs,
            Div(content, id="main-content"),
            cls="w-full max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 pt-24 pb-12 flex-grow"
        ),
        Footer(
            Div(
                Div(
                    H3("YZC", cls="text-lg font-bold text-slate-900 dark:text-white mb-4"),
                    P("Insights from political science research, decoded for everyone.", cls="text-slate-600 dark:text-slate-400 text-sm max-w-xs"),
                    cls="col-span-1 md:col-span-2"
                ),
                Div(
                    H4("Navigation", cls="text-sm font-semibold text-slate-900 dark:text-white uppercase tracking-wider mb-4"),
                    Ul(
                        Li(A("Home", href="/", cls="text-slate-600 dark:text-slate-400 hover:text-primary-600 dark:hover:text-primary-400 transition-colors text-sm")),
                        Li(A("Posts", href="/posts", cls="text-slate-600 dark:text-slate-400 hover:text-primary-600 dark:hover:text-primary-400 transition-colors text-sm")),
                        Li(A("Tags", href="/tags", cls="text-slate-600 dark:text-slate-400 hover:text-primary-600 dark:hover:text-primary-400 transition-colors text-sm")),
                        Li(A("About", href="/about", cls="text-slate-600 dark:text-slate-400 hover:text-primary-600 dark:hover:text-primary-400 transition-colors text-sm")),
                        cls="space-y-2"
                    )
                ),
                Div(
                    H4("Connect", cls="text-sm font-semibold text-slate-900 dark:text-white uppercase tracking-wider mb-4"),
                    Ul(
                        Li(A("Twitter", href="https://twitter.com/zhugangliet", target="_blank", cls="text-slate-600 dark:text-slate-400 hover:text-primary-600 dark:hover:text-primary-400 transition-colors text-sm")),
                        Li(A("GitHub", href="https://github.com/zhuganglie", target="_blank", cls="text-slate-600 dark:text-slate-400 hover:text-primary-600 dark:hover:text-primary-400 transition-colors text-sm")),
                        Li(A("Email", href="mailto:pyrrhonianpig@gmail.com", cls="text-slate-600 dark:text-slate-400 hover:text-primary-600 dark:hover:text-primary-400 transition-colors text-sm")),
                        cls="space-y-2"
                    )
                ),
                cls="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8"
            ),
            Div(
                P(f"© {datetime.now().year} YZC. All rights reserved.", cls="text-slate-500 dark:text-slate-500 text-sm"),
                cls="pt-8 border-t border-slate-200 dark:border-slate-800 text-center"
            ),
            cls="w-full max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-12 border-t border-slate-200 dark:border-slate-800"
        ),
        # Back to Top Button
        Button(
            Lucide("arrow-up", size="20"),
            id="back-to-top",
            cls="fixed bottom-8 right-8 bg-slate-900 dark:bg-slate-700 text-white p-3 rounded-full shadow-lg opacity-0 invisible transition-all duration-300 hover:bg-primary-600 dark:hover:bg-primary-500 hover:-translate-y-1 focus:outline-none focus:ring-2 focus:ring-primary-500 z-50",
            **{"aria-label": "Back to top"}
        ),
        cls="flex flex-col min-h-screen bg-slate-50 dark:bg-slate-900 transition-colors font-sans text-slate-900 dark:text-slate-100"
    )
