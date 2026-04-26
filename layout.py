from fasthtml.common import Main, Header, Footer, Nav, P, B, H1, H2, H3, H4, H5, H6, A, Ul, Li, Div, Span, Button
from datetime import datetime
from urllib.parse import unquote
from lucide_fasthtml import Lucide

HOME = "首页"
POSTS = "文章"
TAGS = "标签"
ABOUT = "关于"

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

    path_map = {
        "posts": POSTS,
        "tags": TAGS,
        "about": ABOUT
    }

    for part in path_parts:
        current_path_build += f'/{part}'
        decoded_part = unquote(part)
        display_text = path_map.get(decoded_part.lower(), decoded_part.replace('-', ' ').title())
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
        classes = "active text-slate-900 dark:text-white font-semibold bg-slate-200/60 dark:bg-slate-700/60 px-3 md:px-4 py-2 rounded-full transition-all" if is_active else "text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100/50 dark:hover:bg-slate-800/50 transition-all px-3 md:px-4 py-2 rounded-full"
        return Li(A(text, href=href, cls=classes))

    # Skip to content link for accessibility
    skip_link = A(
        "跳转到主要内容",
        href="#main-content",
        cls="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:z-50 focus:px-4 focus:py-2 focus:bg-slate-900 focus:text-white focus:rounded transition-all"
    )

    return Main(
        skip_link,
        Div(id="reading-progress", cls="fixed top-0 left-0 h-0.5 bg-slate-900 dark:bg-white z-[60] transition-all duration-300", style="width: 0%"),
        Header(
            Div(
                # Avatar/Logo for the dock
                A(
                    Span("YZC", cls="text-slate-900 dark:text-white font-bold tracking-tight text-sm"),
                    href="/",
                    cls="flex items-center justify-center px-4 h-10 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 transition-colors mr-1 md:mr-2"
                ),
                Nav(
                    Ul(
                        nav_link(HOME, "/"),
                        nav_link(POSTS, "/posts"),
                        nav_link(TAGS, "/tags"),
                        nav_link(ABOUT, "/about"),
                        cls="list-none flex items-center gap-1 text-sm"
                    ),
                    cls="flex items-center"
                ),
                cls="flex items-center p-1.5 bg-white/70 dark:bg-[#191919]/70 backdrop-blur-xl border border-slate-200/60 dark:border-slate-700/60 shadow-sm rounded-full"
            ),
            cls="fixed top-4 md:top-8 left-1/2 -translate-x-1/2 z-50 transition-all duration-300 w-max max-w-[95vw] overflow-x-auto no-scrollbar"
        ),
        Div(
            breadcrumbs,
            Div(content, id="main-content"),
            cls="w-full max-w-4xl mx-auto px-6 pt-28 md:pt-32 pb-16 flex-grow"
        ),
        Footer(
            Div(
                Div(
                    H3("YZC", cls="text-base font-bold text-slate-900 dark:text-white mb-2"),
                    P("探索人工智能如何助力社会科学传播与研究。", cls="text-slate-500 dark:text-slate-400 text-sm max-w-xs"),
                    cls="col-span-1 md:col-span-2"
                ),
                Div(
                    H4("导航", cls="text-xs font-semibold text-slate-900 dark:text-white uppercase tracking-wider mb-3"),
                    Ul(
                        Li(A("首页", href="/", cls="text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition-colors text-sm")),
                        Li(A("文章", href="/posts", cls="text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition-colors text-sm")),
                        Li(A("标签", href="/tags", cls="text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition-colors text-sm")),
                        Li(A("关于", href="/about", cls="text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition-colors text-sm")),
                        cls="space-y-1"
                    )
                ),
                Div(
                    H4("联系我", cls="text-xs font-semibold text-slate-900 dark:text-white uppercase tracking-wider mb-3"),
                    Ul(
                        Li(A("X (Twitter)", href="https://x.com/pilangzhizhu", target="_blank", cls="text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition-colors text-sm")),
                        Li(A("GitHub", href="https://github.com/pilangzhizhu", target="_blank", cls="text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition-colors text-sm")),
                        Li(A("RSS", href="/feed.xml", target="_blank", cls="text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition-colors text-sm")),
                        cls="space-y-1"
                    )
                ),
                cls="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8"
            ),
            Div(
                P(f"© {datetime.now().year} YZC. 由 AI 辅助构建。", cls="text-slate-400 dark:text-slate-500 text-xs"),
                cls="pt-8 border-t border-slate-100 dark:border-slate-800"
            ),
            cls="w-full max-w-4xl mx-auto px-6 py-12 border-t border-slate-100 dark:border-slate-800 mt-auto"
        ),
        # Back to Top Button
        Button(
            Lucide("arrow-up", size="18"),
            id="back-to-top",
            cls="fixed bottom-8 right-8 bg-white dark:bg-slate-800 text-slate-900 dark:text-white border border-slate-200 dark:border-slate-700 p-2.5 rounded shadow-sm opacity-0 invisible transition-all duration-300 hover:bg-slate-50 dark:hover:bg-slate-700 hover:-translate-y-1 focus:outline-none focus:ring-2 focus:ring-slate-900 z-50",
            **{"aria-label": "回到顶部"}
        ),
        cls="flex flex-col min-h-screen bg-white dark:bg-[#191919] transition-colors font-sans text-slate-800 dark:text-slate-200"
    )
