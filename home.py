from fasthtml.common import Div, H1, H2, P, A, Span
from layout import root_layout
from blog import get_posts
from lucide_fasthtml import Lucide

def get_featured_posts(posts, count=3):
    return posts[:count]

def get_home_page(current_path):
    posts = get_posts()
    featured_posts = get_featured_posts(posts)
    
    # Hero Section
    hero = Div(
        H1("Making Political Science Accessible", cls="text-4xl font-bold text-slate-900 mb-4"),
        P("Explore fascinating research that explains how politics shapes our world", 
          cls="text-xl text-slate-600 mb-8"),
        cls="text-center py-16 bg-slate-50 rounded-lg mb-12 px-4"
    )
    
    # Featured Posts Section
    featured_items = []
    for post in featured_posts:
        tags = [
            A(
                Lucide("tag", size="12"), 
                f"{tag}", 
                href=f"/tags/{tag}", 
                cls="flex items-center gap-1.5 text-sm px-2 py-1 bg-slate-100 rounded-full text-slate-700 hover:bg-slate-200 transition-colors"
            ) for tag in post.get('tags', [])
        ]
        
        date_str = post.get('date', '').strftime('%Y-%m-%d') if post.get('date') else ''
        
        featured_items.append(
            Div(
                Span("Featured", cls="text-xs font-semibold text-teal-600 mb-2 block"),
                A(
                    post['title'],
                    href=f"/posts/{post['slug']}", 
                    cls="text-2xl font-bold text-slate-900 hover:text-slate-700 transition-colors block mb-3"
                ),
                P(date_str, cls="text-sm text-slate-600 mb-3"),
                Div(*tags, cls="flex flex-wrap gap-2"),
                cls="mb-8 p-6 bg-white rounded-lg shadow-sm border border-slate-100 hover:border-slate-200 transition-colors"
            )
        )
    
    featured_section = Div(
        H2("Featured Insights", cls="text-2xl font-bold text-slate-900 mb-6"),
        *featured_items,
        cls="mb-12"
    )
    
    # Explore Section
    explore = Div(
        H2("Explore Topics", cls="text-2xl font-bold text-slate-900 mb-6"),
        Div(
            A(
                Div(
                    Lucide("landmark", size="24", cls="mb-3"),
                    "Political Institutions",
                    cls="text-center p-6"
                ),
                href="/tags/政治制度",
                cls="block bg-slate-50 rounded-lg hover:bg-slate-100 transition-colors"
            ),
            A(
                Div(
                    Lucide("scale", size="24", cls="mb-3"),
                    "Political Economy",
                    cls="text-center p-6"
                ),
                href="/tags/政治经济",
                cls="block bg-slate-50 rounded-lg hover:bg-slate-100 transition-colors"
            ),
            A(
                Div(
                    Lucide("flag", size="24", cls="mb-3"),
                    "Contentious Politics",
                    cls="text-center p-6"
                ),
                href="/tags/抗争政治",
                cls="block bg-slate-50 rounded-lg hover:bg-slate-100 transition-colors"
            ),
            cls="grid grid-cols-1 md:grid-cols-3 gap-6"
        ),
        cls="mb-12"
    )
    
    content = Div(
        hero,
        featured_section,
        explore,
        cls="container mx-auto px-4 max-w-4xl"
    )
    
    return root_layout(content, current_path if current_path else "/")
