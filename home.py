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
            H1("Politics, Made Simple.",
                cls="text-4xl md:text-5xl lg:text-6xl font-bold text-slate-900 dark:text-slate-100 mb-4 transition-colors"),
            P("Explore research that explains how politics shapes our world",
              cls="text-xl text-slate-600 dark:text-slate-300 mb-8 transition-colors"),
            Button(
                "Browse All Articles",
                cls="bg-slate-800 hover:bg-slate-700 dark:bg-slate-700 dark:hover:bg-slate-600 text-white font-bold py-3 px-6 rounded-lg transition-colors focus:outline-none focus:ring-2 focus:ring-indigo-500",
                onclick="window.location.href='/posts'"
            ),
            cls="max-w-2xl mx-auto text-center"
        ),
        cls="py-16 px-4 bg-gradient-to-br from-slate-50 to-slate-100 dark:from-slate-800 dark:to-slate-700 rounded-lg mb-12 transition-colors"
    )

    # Featured Posts Section with improved card design
    featured_items = []
    for post in featured_posts:
        date_str = post.get('date', '').strftime('%Y-%m-%d') if post.get('date') else ''
        excerpt = post.get('excerpt', '') or (post.content[:150] + '...' if len(post.content) > 150 else post.content)

        featured_items.append(
            Article(
                Span("Featured", cls="inline-block text-xs font-semibold text-teal-600 dark:text-teal-400 mb-2 px-2 py-1 bg-teal-50 dark:bg-teal-900/30 rounded-full transition-colors"),
                A(
                    H3(post['title'], cls="text-xl font-bold text-slate-900 dark:text-slate-100 hover:text-slate-700 dark:hover:text-slate-300 transition-colors mb-3"),
                    href=f"/posts/{post['slug']}",
                    cls="no-underline block"
                ),
                P(date_str, cls="text-sm text-slate-500 dark:text-slate-400 mb-3 transition-colors"),
                P(excerpt, cls="text-slate-600 dark:text-slate-300 mb-4 line-clamp-3 transition-colors"),
                Div(
                    *[
                        A(
                            Lucide("tag", size="12"),
                            f"{tag}",
                            href=f"/tags/{tag}",
                            cls="flex items-center gap-1.5 text-sm px-2 py-1 bg-slate-100 dark:bg-slate-700 rounded-full text-slate-700 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-600 transition-colors"
                        ) for tag in post.get('tags', [])
                    ],
                    cls="flex flex-wrap gap-2"),
                cls="p-6 bg-white dark:bg-slate-800 rounded-lg shadow-sm border border-slate-100 dark:border-slate-700 hover:border-slate-200 dark:hover:border-slate-600 hover:shadow-md transition-all"
            )
        )

    featured_section = Section(
        H2("Featured Insights", cls="text-2xl font-bold text-slate-900 dark:text-slate-100 mb-6 transition-colors"),
        Div(
            *featured_items,
            cls="grid grid-cols-1 md:grid-cols-3 gap-6"
        ),
        cls="mb-16"
    )

    # Topics Section with visual improvements
    explore = Section(
        H2("Explore Topics", cls="text-2xl font-bold text-slate-900 dark:text-slate-100 mb-6 transition-colors"),
        Div(
            A(
                Div(
                    Lucide("landmark", size="32", cls="mb-4 text-indigo-600 dark:text-indigo-400 transition-colors"),
                    H3("Political Institutions", cls="text-lg font-bold mb-2 dark:text-slate-100 transition-colors"),
                    P("Understand how governments and political systems function", cls="text-sm text-slate-600 dark:text-slate-300 transition-colors"),
                    cls="text-center p-6"
                ),
                href="/tags/政治制度",
                cls="block bg-slate-50 dark:bg-slate-800 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-700 hover:shadow-md hover:scale-102 transition-all duration-200 ease-in-out"
            ),
            A(
                Div(
                    Lucide("scale", size="32", cls="mb-4 text-amber-600 dark:text-amber-400 transition-colors"),
                    H3("Political Economy", cls="text-lg font-bold mb-2 dark:text-slate-100 transition-colors"),
                    P("Explore the relationship between politics and economics", cls="text-sm text-slate-600 dark:text-slate-300 transition-colors"),
                    cls="text-center p-6"
                ),
                href="/tags/政治经济",
                cls="block bg-slate-50 dark:bg-slate-800 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-700 hover:shadow-md hover:scale-102 transition-all duration-200 ease-in-out"
            ),
            A(
                Div(
                    Lucide("flag", size="32", cls="mb-4 text-rose-600 dark:text-rose-400 transition-colors"),
                    H3("Contentious Politics", cls="text-lg font-bold mb-2 dark:text-slate-100 transition-colors"),
                    P("Learn about protests, revolutions, and social movements", cls="text-sm text-slate-600 dark:text-slate-300 transition-colors"),
                    cls="text-center p-6"
                ),
                href="/tags/抗争政治",
                cls="block bg-slate-50 dark:bg-slate-800 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-700 hover:shadow-md hover:scale-102 transition-all duration-200 ease-in-out"
            ),
            cls="grid grid-cols-1 md:grid-cols-3 gap-6"
        ),
        cls="mb-16"
    )

    # New section: About the Author
    about_section = Section(
        H2("About the Author", cls="text-2xl font-bold text-slate-900 dark:text-slate-100 mb-6 transition-colors"),
        Div(
            Div(
                Img(src="public/images/avatar.jpg", alt="Profile Photo", loading="lazy",
                     cls="w-24 h-24 rounded-full bg-slate-200 dark:bg-slate-700 mb-4 mx-auto md:mx-0 transition-colors"),
                cls="md:w-1/4"
            ),
            Div(
                H3("A Reader with Passion", cls="text-xl font-bold mb-3 dark:text-slate-100 transition-colors"),
                P("Drawing from years of academic research and grassroots experience, I decode complex political concepts and present them in accessible ways. My interests focus on institutional design, political behavior, and comparative government.",
                  cls="text-slate-600 dark:text-slate-300 mb-4 transition-colors"),
                A(
                    "Read more about me",
                    href="/about",
                    cls="inline-flex items-center text-indigo-600 dark:text-indigo-400 hover:text-indigo-800 dark:hover:text-indigo-300 transition-colors"
                ),
                cls="md:w-3/4"
            ),
            cls="flex flex-col md:flex-row items-center md:items-start gap-6 p-8 bg-slate-50 dark:bg-slate-800 rounded-lg transition-colors"
        ),
        cls="mb-12"
    )

    content = Div(
        hero,
        featured_section,
        explore,
        about_section,
        cls="container mx-auto px-4 max-w-4xl"
    )

    return root_layout(content, current_path if current_path else "/")
