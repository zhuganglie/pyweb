from fasthtml.common import Div, H1, H2, H3, Li, P, Titled, Ul, A, Img, Section, Article, Svg, ft
from layout import root_layout
from lucide_fasthtml import Lucide

def get_about_page(current_path):
    # Hero section with profile info
    hero_section = Section(
        Div(
            Img(
                src="/public/images/avatar.jpg",
                alt="Profile Photo",
                loading="lazy",
                cls="w-24 h-24 rounded object-cover border border-slate-200 dark:border-slate-800 mb-6"
            ),
            H1("关于", cls="text-3xl md:text-4xl font-bold mb-4 text-slate-900 dark:text-white tracking-tight"),
            P("社会科学普及作家 • AI 探索者", cls="text-lg text-slate-600 dark:text-slate-400 mb-6"),
            Div(
                A(Lucide("github", size="20"), href="https://github.com/pilangzhizhu", cls="p-2 bg-white dark:bg-[#191919] border border-slate-200 dark:border-slate-800 rounded text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:border-slate-400 transition-colors", **{"aria-label": "发送邮件"}),
                A(
                    # Using a custom SVG for the X (formerly Twitter) logo
                    Svg(
                        ft("path", d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-9.56-6.638 9.56H.553l8.604-9.834L0 1.154h7.594l5.243 6.932 6.064-6.932zm-1.294 19.497h2.039L6.448 3.24H4.26L17.607 20.65z"),
                        viewBox="0 0 24 24",
                        width="20",
                        height="20",
                        fill="currentColor"
                    ),
                    href="https://x.com/pilangzhizhu",
                    cls="p-2 bg-white dark:bg-[#191919] border border-slate-200 dark:border-slate-800 rounded text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:border-slate-400 transition-colors",
                    **{"aria-label": "访问 X (Twitter)"}
                ),
                A(Lucide("rss", size="20"), href="/feed.xml", target="_blank", cls="p-2 bg-white dark:bg-[#191919] border border-slate-200 dark:border-slate-800 rounded text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:border-slate-400 transition-colors", **{"aria-label": "订阅 RSS"}),
                cls="flex gap-4"
            ),
            cls="max-w-3xl"
        ),
        cls="py-12 border-b border-slate-100 dark:border-slate-800 mb-16"
    )

    # Main content sections
    mission_section = Article(
        H2("我的使命", cls="text-2xl font-bold mb-4 text-slate-900 dark:text-white"),
        Div(
            P("欢迎！我是一名社会科学普及作家，致力于用通俗易懂的语言解析复杂的社会理论。最近，我开启了一段全新的旅程：探索人工智能如何增强和改变我的工作方式。",
              cls="text-base text-slate-700 dark:text-slate-300 leading-relaxed mb-4"),
            P("我使用 Gemini 从零开始搭建了这个博客。作为一名非技术人员，这个网站是我学习过程的真实记录。我的目标是探索 AI 如何在各个方面帮助我——从研究学术论文、整理思路，到撰写并向公众传播复杂的政治概念。",
              cls="text-base text-slate-700 dark:text-slate-300 leading-relaxed"),
            cls="prose prose-slate dark:prose-invert max-w-none"
        ),
        cls="mb-16 max-w-3xl"
    )

    focus_section = Article(
        Div(
            H2("关注领域", cls="text-2xl font-bold mb-2 text-slate-900 dark:text-white"),
            P("我目前正在探索和撰写的主题。", cls="text-slate-600 dark:text-slate-400 mb-6"),
            cls="max-w-3xl"
        ),
        Div(
            Div(
                Div(Lucide("bot", size="24", cls="text-slate-700 dark:text-slate-300"), cls="mb-3"),
                H3("为创作者赋能的 AI", cls="text-lg font-bold mb-2 text-slate-900 dark:text-white"),
                P("如何利用 AI 提升生产力、创造力以及内容创作的工作流。",
                  cls="text-sm text-slate-600 dark:text-slate-400 leading-relaxed"),
                cls="p-6 bg-white dark:bg-[#191919] rounded border border-slate-200 dark:border-slate-800"
            ),
            Div(
                Div(Lucide("book-open", size="24", cls="text-slate-700 dark:text-slate-300"), cls="mb-3"),
                H3("AI 与社会科学", cls="text-lg font-bold mb-2 text-slate-900 dark:text-white"),
                P("通过社会科学的视角审视人工智能的社会影响。",
                  cls="text-sm text-slate-600 dark:text-slate-400 leading-relaxed"),
                cls="p-6 bg-white dark:bg-[#191919] rounded border border-slate-200 dark:border-slate-800"
            ),
            Div(
                Div(Lucide("terminal", size="24", cls="text-slate-700 dark:text-slate-300"), cls="mb-3"),
                H3("借助 AI 学习编程", cls="text-lg font-bold mb-2 text-slate-900 dark:text-white"),
                P("我在 AI 助手的帮助下探索编程世界的个人历程。",
                  cls="text-sm text-slate-600 dark:text-slate-400 leading-relaxed"),
                cls="p-6 bg-white dark:bg-[#191919] rounded border border-slate-200 dark:border-slate-800"
            ),
            Div(
                Div(Lucide("users", size="24", cls="text-slate-700 dark:text-slate-300"), cls="mb-3"),
                H3("社区建设", cls="text-lg font-bold mb-2 text-slate-900 dark:text-white"),
                P("分享知识并培养一个探索 AI 的非技术人员社区。",
                  cls="text-sm text-slate-600 dark:text-slate-400 leading-relaxed"),
                cls="p-6 bg-white dark:bg-[#191919] rounded border border-slate-200 dark:border-slate-800"
            ),
            cls="grid grid-cols-1 md:grid-cols-2 gap-4 max-w-4xl"
        ),
        cls="mb-16"
    )

    background_section = Article(
        H2("我的背景", cls="text-2xl font-bold mb-4 text-slate-900 dark:text-white"),
        Div(
            P("多年来，我一直致力于通过引人入胜的内容向公众普及社会科学理论。我的视频和文章旨在帮助人们理解社会运作的底层结构。",
              cls="text-base text-slate-700 dark:text-slate-300 leading-relaxed mb-4"),
            P("随着 AI 的快速发展，我意识到这不仅仅是一次技术变革，更是一次巨大的社会变革。我决定不再仅仅作为一个旁观者，而是亲自去实践。我没有计算机科学学位，但我有好奇心，并且有 AI 工具作为我的帮手。",
              cls="text-base text-slate-700 dark:text-slate-300 leading-relaxed mb-4"),
            P("这个博客就是这份好奇心的结晶。感谢你加入我，与我一起学习、构建，并探索技术与社会的交汇点。",
              cls="text-base text-slate-700 dark:text-slate-300 leading-relaxed"),
            cls="prose prose-slate dark:prose-invert max-w-none"
        ),
        cls="mb-16 max-w-3xl"
    )

    content = Div(
        hero_section,
        mission_section,
        focus_section,
        background_section,
        cls="w-full"
    )

    return root_layout(
        Titled("关于", content),
        current_path
    )
