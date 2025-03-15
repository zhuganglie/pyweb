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
                cls="text-4xl md:text-5xl lg:text-6xl font-bold text-slate-900 mb-4"),
            P("Explore research that explains how politics shapes our world",
              cls="text-xl text-slate-600 mb-8"),
            Button(
                "Browse All Articles",
                cls="bg-slate-800 hover:bg-slate-700 text-white font-bold py-3 px-6 rounded-lg transition-colors",
                onclick="window.location.href='/posts'"
            ),
            cls="max-w-2xl mx-auto text-center"
        ),
        cls="py-16 px-4 bg-gradient-to-br from-slate-50 to-slate-100 rounded-lg mb-12"
    )

    # Featured Posts Section with improved card design
    featured_items = []
    for post in featured_posts:
        date_str = post.get('date', '').strftime('%Y-%m-%d') if post.get('date') else ''
        excerpt = post.get('excerpt', '') or (post.content[:150] + '...' if len(post.content) > 150 else post.content)

        featured_items.append(
            Article(
                Span("Featured", cls="inline-block text-xs font-semibold text-teal-600 mb-2 px-2 py-1 bg-teal-50 rounded-full"),
                A(
                    H3(post['title'], cls="text-xl font-bold text-slate-900 hover:text-slate-700 transition-colors mb-3"),
                    href=f"/posts/{post['slug']}",
                    cls="no-underline block"
                ),
                P(date_str, cls="text-sm text-slate-500 mb-3"),
                P(excerpt, cls="text-slate-600 mb-4 line-clamp-3"),
                Div(
                    *[
                        A(
                            Lucide("tag", size="12"),
                            f"{tag}",
                            href=f"/tags/{tag}",
                            cls="flex items-center gap-1.5 text-sm px-2 py-1 bg-slate-100 rounded-full text-slate-700 hover:bg-slate-200 transition-colors"
                        ) for tag in post.get('tags', [])
                    ],
                    cls="flex flex-wrap gap-2"),
                cls="p-6 bg-white rounded-lg shadow-sm border border-slate-100 hover:border-slate-200 hover:shadow-md transition-all"
            )
        )

    featured_section = Section(
        H2("Featured Insights", cls="text-2xl font-bold text-slate-900 mb-6"),
        Div(
            *featured_items,
            cls="grid grid-cols-1 md:grid-cols-3 gap-6"
        ),
        cls="mb-16"
    )

    # Topics Section with visual improvements
    explore = Section(
        H2("Explore Topics", cls="text-2xl font-bold text-slate-900 mb-6"),
        Div(
            A(
                Div(
                    Lucide("landmark", size="32", cls="mb-4 text-indigo-600"),
                    H3("Political Institutions", cls="text-lg font-bold mb-2"),
                    P("Understand how governments and political systems function", cls="text-sm text-slate-600"),
                    cls="text-center p-6"
                ),
                href="/tags/政治制度",
                cls="block bg-slate-50 rounded-lg hover:bg-slate-100 transition-colors hover:shadow-sm"
            ),
            A(
                Div(
                    Lucide("scale", size="32", cls="mb-4 text-amber-600"),
                    H3("Political Economy", cls="text-lg font-bold mb-2"),
                    P("Explore the relationship between politics and economics", cls="text-sm text-slate-600"),
                    cls="text-center p-6"
                ),
                href="/tags/政治经济",
                cls="block bg-slate-50 rounded-lg hover:bg-slate-100 transition-colors hover:shadow-sm"
            ),
            A(
                Div(
                    Lucide("flag", size="32", cls="mb-4 text-rose-600"),
                    H3("Contentious Politics", cls="text-lg font-bold mb-2"),
                    P("Learn about protests, revolutions, and social movements", cls="text-sm text-slate-600"),
                    cls="text-center p-6"
                ),
                href="/tags/抗争政治",
                cls="block bg-slate-50 rounded-lg hover:bg-slate-100 transition-colors hover:shadow-sm"
            ),
            cls="grid grid-cols-1 md:grid-cols-3 gap-6"
        ),
        cls="mb-16"
    )

    # New section: About the Author
    about_section = Section(
        H2("About the Author", cls="text-2xl font-bold text-slate-900 mb-6"),
        Div(
            Div(
                Img(src="public/images/avatar.jpeg", alt="Profile Photo",
                     cls="w-24 h-24 rounded-full bg-slate-200 mb-4 mx-auto md:mx-0"),
                cls="md:w-1/4"
            ),
            Div(
                H3("A Reader with Passion", cls="text-xl font-bold mb-3"),
                P("Drawing from years of academic research and grassroots experience, I decode complex political concepts and present them in accessible ways. My interests focus on institutional design, political behavior, and comparative government.",
                  cls="text-slate-600 mb-4"),
                A(
                    "Read more about me",
                    href="/about",
                    cls="inline-flex items-center text-indigo-600 hover:text-indigo-800"
                ),
                cls="md:w-3/4"
            ),
            cls="flex flex-col md:flex-row items-center md:items-start gap-6 p-8 bg-slate-50 rounded-lg"
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
