from fasthtml.common import Div, H1, H2, H3, P, A, Img, Span, Section, Article, Button
from layout import root_layout
from blog import get_posts, get_top_tags
from lucide_fasthtml import Lucide

def get_featured_posts(posts, count=3):
    """Get a selection of featured posts."""
    return posts[:count]

def get_home_page(current_path):
    posts = get_posts()
    featured_posts = get_featured_posts(posts)
    top_tags = get_top_tags(3)

    # Tag meta mapping for better visuals
    tag_meta = {
        "ai": {"icon": "bot", "desc": "使用 AI 构建工具、网站和工作流"},
        "social-science": {"icon": "book-open", "desc": "关于 AI 如何影响社会与研究的思考"},
        "creator": {"icon": "pen-tool", "desc": "将 AI 融入我的创作过程和工作流中"},
        "software": {"icon": "code", "desc": "系统设计、模式与最佳实践"},
        "web": {"icon": "layout", "desc": "前端框架、后端 API 与网页设计"},
        "life": {"icon": "user", "desc": "效率、爱好与随笔"},
    }

    # Hero Section with Notion-like minimalist design
    hero = Section(
        Div(
            H1("社会科学遇上人工智能",
                cls="text-4xl md:text-5xl lg:text-6xl font-bold text-slate-900 dark:text-white mb-6 tracking-tight leading-tight"),
            P("我是一名社会科学普及作家。我使用 Gemini 搭建了这个博客，以探索人工智能如何协助我的研究和工作。",
              cls="text-xl text-slate-600 dark:text-slate-400 mb-8 max-w-2xl leading-relaxed"),
            Div(
                Button(
                    "浏览文章",
                    cls="bg-slate-900 hover:bg-slate-800 dark:bg-white dark:hover:bg-slate-200 text-white dark:text-slate-900 font-medium py-2.5 px-6 rounded transition-colors focus:outline-none focus:ring-2 focus:ring-slate-400 focus:ring-offset-2 dark:focus:ring-offset-[#191919]",
                    onclick="window.location.href='/posts'"
                ),
                Button(
                    "关于",
                    cls="bg-white dark:bg-transparent hover:bg-slate-50 dark:hover:bg-slate-800 text-slate-900 dark:text-white font-medium py-2.5 px-6 rounded transition-colors border border-slate-200 dark:border-slate-700 focus:outline-none focus:ring-2 focus:ring-slate-400 focus:ring-offset-2 dark:focus:ring-offset-[#191919]",
                    onclick="window.location.href='/about'"
                ),
                cls="flex flex-col sm:flex-row gap-4"
            ),
            cls="max-w-3xl py-20 md:py-28"
        ),
        cls="mb-16 border-b border-slate-100 dark:border-slate-800"
    )

    # Featured Posts Section with minimalist card design
    featured_items = []
    for post in featured_posts:
        date_str = post.get('date', '').strftime('%Y年%m月%d日') if post.get('date') else ''
        excerpt = post.get('excerpt', '') or (post.content[:150] + '...' if len(post.content) > 150 else post.content)
        read_time = post.get('read_time', 5)

        featured_items.append(
            Article(
                A(
                    Div(
                        Div(
                            H3(post['title'], cls="text-lg font-semibold text-slate-900 dark:text-white mb-2 group-hover:underline leading-tight"),
                            P(excerpt, cls="text-sm text-slate-600 dark:text-slate-400 mb-4 line-clamp-2"),
                            Div(
                                Span(date_str, cls="text-xs text-slate-500 dark:text-slate-500"),
                                Span("•", cls="mx-2 text-slate-300 dark:text-slate-700"),
                                Span(f"阅读需要 {read_time} 分钟", cls="text-xs text-slate-500 dark:text-slate-500"),
                                cls="flex items-center mt-auto"
                            ),
                            cls="p-5 flex flex-col h-full"
                        ),
                        cls="h-full bg-white dark:bg-[#191919] rounded border border-slate-200 dark:border-slate-800 hover:border-slate-400 dark:hover:border-slate-600 transition-colors group"
                    ),
                    href=f"/posts/{post['slug']}",
                    cls="no-underline block h-full"
                ),
                cls="h-full"
            )
        )

    featured_section = Section(
        Div(
            H2("精选见解", cls="text-xl font-bold text-slate-900 dark:text-white mb-6"),
            cls="mb-6"
        ),
        Div(
            *featured_items,
            cls="grid grid-cols-1 md:grid-cols-3 gap-4"
        ),
        cls="mb-20"
    )

    # Topics Section with dynamic tags
    topic_items = []
    for tag_name, count in top_tags:
        meta = tag_meta.get(tag_name.lower())
        description = meta["desc"] if meta else f"浏览更多关于 {tag_name} 的文章"

        topic_items.append(
            A(
                Div(
                    H3(tag_name.title(), cls="text-base font-semibold mb-2 text-slate-900 dark:text-white group-hover:underline"),
                    P(description, cls="text-sm text-slate-600 dark:text-slate-400"),
                    cls="p-6 h-full flex flex-col justify-center"
                ),
                href=f"/tags/{tag_name}",
                cls="block bg-white dark:bg-[#191919] rounded border border-slate-200 dark:border-slate-800 hover:border-slate-400 dark:hover:border-slate-600 transition-colors group"
            )
        )

    explore = Section(
        Div(
            H2("探索主题", cls="text-xl font-bold text-slate-900 dark:text-white mb-6"),
            cls="mb-6"
        ),
        Div(
            *topic_items,
            cls="grid grid-cols-1 md:grid-cols-3 gap-4"
        ),
        cls="mb-20"
    )

    # About the Author minimalist section
    about_section = Section(
        Div(
            Div(
                Img(src="/public/images/avatar.jpg", alt="Profile Photo", loading="lazy",
                     cls="w-20 h-20 rounded object-cover border border-slate-200 dark:border-slate-700 mb-4 md:mb-0 md:mr-6"),
                cls="flex-shrink-0"
            ),
            Div(
                H2("关于作者", cls="text-xl font-bold text-slate-900 dark:text-white mb-2"),
                P("我是一名社会科学普及作家与传播者。虽然我没有软件开发背景，但我使用 Gemini 搭建了这个博客，以此探索并记录人工智能如何辅助我的研究、写作和传播过程。",
                  cls="text-sm text-slate-600 dark:text-slate-300 mb-4 leading-relaxed"),
                A(
                    "了解更多 →",
                    href="/about",
                    cls="inline-flex items-center text-sm font-medium text-slate-900 dark:text-white hover:underline transition-colors"
                ),
                cls="flex-grow"
            ),
            cls="flex flex-col md:flex-row items-center md:items-start bg-slate-50/50 dark:bg-[#202020] rounded p-6 border border-slate-200 dark:border-slate-800"
        ),
        cls="mb-20"
    )

    content = Div(
        hero,
        featured_section,
        explore,
        about_section,
        cls="w-full"
    )

    return root_layout(content, current_path if current_path else "/")
