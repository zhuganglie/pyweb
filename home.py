from fasthtml.common import Div, H1, H2, H3, P, A, Img, Span, Section, Article, Button
from layout import root_layout
from blog import get_posts
from lucide_fasthtml import Lucide

def get_featured_posts(posts, count=3):
    """Get a selection of featured posts."""
    return posts[:count]

def get_home_page(current_path):
    posts = get_posts()
    featured_posts = get_featured_posts(posts)

    # Hero Section with improved design
    hero = Section(
        Div(
            Span("Welcome to YZC", cls="inline-block py-1 px-3 rounded-full bg-primary-100 dark:bg-primary-900/30 text-primary-700 dark:text-primary-300 text-sm font-semibold mb-6 tracking-wide uppercase"),
            H1("Politics, Made Simple.",
                cls="text-5xl md:text-6xl lg:text-7xl font-extrabold text-slate-900 dark:text-white mb-6 tracking-tight leading-tight"),
            P("Explore research that explains how politics shapes our world. Decoded for everyone.",
              cls="text-xl md:text-2xl text-slate-600 dark:text-slate-300 mb-10 max-w-2xl mx-auto leading-relaxed"),
            Div(
                Button(
                    "Browse Articles",
                    cls="bg-primary-600 hover:bg-primary-700 text-white font-semibold py-4 px-8 rounded-full transition-all shadow-lg hover:shadow-primary-500/30 hover:-translate-y-1 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 dark:focus:ring-offset-slate-900",
                    onclick="window.location.href='/posts'"
                ),
                Button(
                    "About Me",
                    cls="bg-white dark:bg-slate-800 hover:bg-slate-50 dark:hover:bg-slate-700 text-slate-900 dark:text-white font-semibold py-4 px-8 rounded-full transition-all shadow-md hover:shadow-lg border border-slate-200 dark:border-slate-700 hover:-translate-y-1 focus:outline-none focus:ring-2 focus:ring-slate-500 focus:ring-offset-2 dark:focus:ring-offset-slate-900",
                    onclick="window.location.href='/about'"
                ),
                cls="flex flex-col sm:flex-row gap-4 justify-center"
            ),
            cls="max-w-4xl mx-auto text-center relative z-10"
        ),
        Div(cls="absolute top-0 left-0 w-full h-full bg-gradient-to-b from-primary-50/50 to-transparent dark:from-primary-900/10 dark:to-transparent -z-10"),
        cls="relative py-24 md:py-32 px-4 mb-20 overflow-hidden"
    )

    # Featured Posts Section with improved card design
    featured_items = []
    for post in featured_posts:
        date_str = post.get('date', '').strftime('%B %d, %Y') if post.get('date') else ''
        excerpt = post.get('excerpt', '') or (post.content[:150] + '...' if len(post.content) > 150 else post.content)
        read_time = post.get('read_time', 5)

        featured_items.append(
            Article(
                A(
                    Div(
                        Div(
                            Span("Featured", cls="inline-block text-xs font-bold text-white bg-primary-600 px-2 py-1 rounded mb-3"),
                            H3(post['title'], cls="text-2xl font-bold text-slate-900 dark:text-white mb-3 group-hover:text-primary-600 dark:group-hover:text-primary-400 transition-colors leading-tight"),
                            P(excerpt, cls="text-slate-600 dark:text-slate-300 mb-4 line-clamp-3"),
                            Div(
                                Span(date_str, cls="text-sm font-medium text-slate-500 dark:text-slate-400"),
                                Span("•", cls="mx-2 text-slate-300 dark:text-slate-600"),
                                Span(f"{read_time} min read", cls="text-sm font-medium text-slate-500 dark:text-slate-400"),
                                cls="flex items-center"
                            ),
                            cls="p-8"
                        ),
                        cls="h-full bg-white dark:bg-slate-800 rounded-2xl shadow-sm hover:shadow-xl border border-slate-100 dark:border-slate-700 transition-all duration-300 group hover:-translate-y-1"
                    ),
                    href=f"/posts/{post['slug']}",
                    cls="no-underline block h-full"
                ),
                cls="h-full"
            )
        )

    featured_section = Section(
        Div(
            H2("Featured Insights", cls="text-3xl font-bold text-slate-900 dark:text-white mb-2"),
            P("Curated articles to get you started.", cls="text-slate-600 dark:text-slate-400 text-lg"),
            cls="mb-10 text-center"
        ),
        Div(
            *featured_items,
            cls="grid grid-cols-1 md:grid-cols-3 gap-8"
        ),
        cls="mb-24 max-w-6xl mx-auto px-4"
    )

    # Topics Section with visual improvements
    explore = Section(
        Div(
            H2("Explore Topics", cls="text-3xl font-bold text-slate-900 dark:text-white mb-2"),
            P("Dive deep into specific areas of political science.", cls="text-slate-600 dark:text-slate-400 text-lg"),
            cls="mb-10 text-center"
        ),
        Div(
            A(
                Div(
                    Div(Lucide("landmark", size="32", cls="text-primary-600 dark:text-primary-400"), cls="mb-4 p-3 bg-primary-50 dark:bg-primary-900/30 rounded-xl w-fit"),
                    H3("Political Institutions", cls="text-xl font-bold mb-2 text-slate-900 dark:text-white"),
                    P("Understand how governments and political systems function", cls="text-slate-600 dark:text-slate-400"),
                    cls="p-8 h-full"
                ),
                href="/tags/政治制度",
                cls="block bg-white dark:bg-slate-800 rounded-2xl border border-slate-100 dark:border-slate-700 hover:border-primary-200 dark:hover:border-primary-800 hover:shadow-lg transition-all duration-300 hover:-translate-y-1 group"
            ),
            A(
                Div(
                    Div(Lucide("scale", size="32", cls="text-secondary-600 dark:text-secondary-400"), cls="mb-4 p-3 bg-secondary-50 dark:bg-secondary-900/30 rounded-xl w-fit"),
                    H3("Political Economy", cls="text-xl font-bold mb-2 text-slate-900 dark:text-white"),
                    P("Explore the relationship between politics and economics", cls="text-slate-600 dark:text-slate-400"),
                    cls="p-8 h-full"
                ),
                href="/tags/政治经济",
                cls="block bg-white dark:bg-slate-800 rounded-2xl border border-slate-100 dark:border-slate-700 hover:border-secondary-200 dark:hover:border-secondary-800 hover:shadow-lg transition-all duration-300 hover:-translate-y-1 group"
            ),
            A(
                Div(
                    Div(Lucide("flag", size="32", cls="text-emerald-600 dark:text-emerald-400"), cls="mb-4 p-3 bg-emerald-50 dark:bg-emerald-900/30 rounded-xl w-fit"),
                    H3("Contentious Politics", cls="text-xl font-bold mb-2 text-slate-900 dark:text-white"),
                    P("Learn about protests, revolutions, and social movements", cls="text-slate-600 dark:text-slate-400"),
                    cls="p-8 h-full"
                ),
                href="/tags/抗争政治",
                cls="block bg-white dark:bg-slate-800 rounded-2xl border border-slate-100 dark:border-slate-700 hover:border-emerald-200 dark:hover:border-emerald-800 hover:shadow-lg transition-all duration-300 hover:-translate-y-1 group"
            ),
            cls="grid grid-cols-1 md:grid-cols-3 gap-6"
        ),
        cls="mb-24 max-w-6xl mx-auto px-4"
    )

    # New section: About the Author
    about_section = Section(
        Div(
            Div(
                Img(src="images/avatar.jpg", alt="Profile Photo", loading="lazy",
                     cls="w-32 h-32 rounded-full object-cover border-4 border-white dark:border-slate-700 shadow-lg mb-6 md:mb-0 md:mr-8"),
                cls="flex-shrink-0"
            ),
            Div(
                H2("About the Author", cls="text-3xl font-bold text-slate-900 dark:text-white mb-4"),
                P("Drawing from years of academic research and grassroots experience, I decode complex political concepts and present them in accessible ways. My interests focus on institutional design, political behavior, and comparative government.",
                  cls="text-lg text-slate-600 dark:text-slate-300 mb-6 leading-relaxed"),
                A(
                    "Read more about me →",
                    href="/about",
                    cls="inline-flex items-center font-semibold text-primary-600 dark:text-primary-400 hover:text-primary-700 dark:hover:text-primary-300 transition-colors"
                ),
                cls="flex-grow"
            ),
            cls="flex flex-col md:flex-row items-center md:items-start bg-slate-50 dark:bg-slate-800/50 rounded-3xl p-8 md:p-12 border border-slate-100 dark:border-slate-700"
        ),
        cls="mb-24 max-w-5xl mx-auto px-4"
    )

    content = Div(
        hero,
        featured_section,
        explore,
        about_section,
        cls="w-full"
    )

    return root_layout(content, current_path if current_path else "/")
