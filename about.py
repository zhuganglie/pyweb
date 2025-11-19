from fasthtml.common import Div, H1, H2, H3, Li, P, Titled, Ul, A, Img, Section, Article
from layout import root_layout
from lucide_fasthtml import Lucide

def get_about_page(current_path):
    # Hero section with profile info
    hero_section = Section(
        Div(
            Div(
                Div(
                    Img(
                        src="/public/images/avatar.jpg",
                        alt="Profile Photo",
                        loading="lazy",
                        cls="w-32 h-32 rounded-full object-cover border-4 border-white dark:border-slate-700 shadow-lg transition-colors"
                    ),
                    cls="relative -mt-16 mb-4"
                ),
                H1("About Me", cls="text-3xl font-bold mb-3 dark:text-slate-100 transition-colors"),
                P("A Reader with Passion", cls="text-xl text-slate-600 dark:text-slate-300 mb-6 transition-colors"),
                Div(
                    A(Lucide("mail", size="18"), "email",
                      href="mailto:pyrrhonianpig@gmail.com",
                      cls="flex items-center gap-2 text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-slate-100 transition-colors focus:outline-none focus:ring-2 focus:ring-indigo-500",
                      **{"aria-label": "Send email"}),
                    A(Lucide("twitter", size="18"), "twitter",
                      href="https://twitter.com/zhugangliet",
                      cls="flex items-center gap-2 text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-slate-100 transition-colors focus:outline-none focus:ring-2 focus:ring-indigo-500",
                      **{"aria-label": "Visit Twitter profile"}),
                    A(Lucide("github", size="18"), "github",
                      href="https://github.com/zhuganglie",
                      cls="flex items-center gap-2 text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-slate-100 transition-colors focus:outline-none focus:ring-2 focus:ring-indigo-500",
                      **{"aria-label": "Visit GitHub profile"}),
                    cls="flex flex-col sm:flex-row gap-4 sm:gap-6"
                ),
                cls="text-center sm:text-left"
            ),
            cls="bg-white dark:bg-slate-800 p-8 rounded-lg shadow-sm border border-slate-100 dark:border-slate-700 relative mt-12 transition-colors"
        ),
        cls="bg-gradient-to-br from-slate-700 to-slate-900 dark:from-slate-800 dark:to-slate-950 pt-24 pb-12 px-6 rounded-lg mb-12 transition-colors"
    )

    # Main content sections
    mission_section = Article(
        H2("My Mission", cls="text-2xl font-bold mb-4 flex items-center gap-2 dark:text-slate-100 transition-colors"),
        P("Welcome to my blog where I explore complex political science research and make it accessible to curious minds. I believe that understanding political systems and behaviors helps us navigate our social world and make more informed decisions.",
          cls="mb-4 text-slate-700 dark:text-slate-300 leading-relaxed transition-colors"),
        P("This platform is dedicated to bridging the gap between academic knowledge and everyday understanding, presenting research findings in clear, engaging ways that connect to real-world issues.",
          cls="mb-4 text-slate-700 dark:text-slate-300 leading-relaxed transition-colors"),
        cls="mb-10"
    )

    focus_section = Article(
        H2("Research Focus", cls="text-2xl font-bold mb-4 flex items-center gap-2 dark:text-slate-100 transition-colors"),
        P("My work explores a range of interconnected topics in political science:", cls="mb-4 text-slate-700 dark:text-slate-300 transition-colors"),
        Div(
            Div(
                Lucide("landmark", size="24", cls="text-indigo-600 dark:text-indigo-400 mb-2 transition-colors"),
                H3("Political Institutions", cls="font-bold mb-2 dark:text-slate-100 transition-colors"),
                P("The evolution of democracy and authoritarianism, institutional design, and governance systems",
                  cls="text-slate-600 dark:text-slate-400 transition-colors"),
                cls="p-4 bg-slate-50 dark:bg-slate-800 rounded-lg transition-colors"
            ),
            Div(
                Lucide("scale", size="24", cls="text-amber-600 dark:text-amber-400 mb-2 transition-colors"),
                H3("Political Economy", cls="font-bold mb-2 dark:text-slate-100 transition-colors"),
                P("How political decisions shape economic outcomes, resource distribution, and development patterns",
                  cls="text-slate-600 dark:text-slate-400 transition-colors"),
                cls="p-4 bg-slate-50 dark:bg-slate-800 rounded-lg transition-colors"
            ),
            Div(
                Lucide("users", size="24", cls="text-emerald-600 dark:text-emerald-400 mb-2 transition-colors"),
                H3("Political Behavior", cls="font-bold mb-2 dark:text-slate-100 transition-colors"),
                P("The psychology of political decision-making, social movements, and collective action",
                  cls="text-slate-600 dark:text-slate-400 transition-colors"),
                cls="p-4 bg-slate-50 dark:bg-slate-800 rounded-lg transition-colors"
            ),
            Div(
                Lucide("globe", size="24", cls="text-blue-600 dark:text-blue-400 mb-2 transition-colors"),
                H3("Comparative Politics", cls="font-bold mb-2 dark:text-slate-100 transition-colors"),
                P("Cross-national patterns in politics, regional dynamics, and cultural influences on governance",
                  cls="text-slate-600 dark:text-slate-400 transition-colors"),
                cls="p-4 bg-slate-50 dark:bg-slate-800 rounded-lg transition-colors"
            ),
            cls="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6"
        ),
        cls="mb-10"
    )

    background_section = Article(
        H2("Personal Background", cls="text-2xl font-bold mb-4 flex items-center gap-2 dark:text-slate-100 transition-colors"),
        P("I'm an educator and researcher with a passion for social sciences. Beyond my academic work, I enjoy cycling through urban landscapes, reading across disciplines, and coding projects that bring data to life.",
          cls="mb-4 text-slate-700 dark:text-slate-300 leading-relaxed transition-colors"),
        P("My experience as a grassroots community leader has shaped my perspective on how politics affects everyday lives. This combination of academic knowledge and practical engagement informs my approach to analyzing political phenomena.",
          cls="mb-4 text-slate-700 dark:text-slate-300 leading-relaxed transition-colors"),
        P("Through this blog, I hope to share my enthusiasm for political science while making complex concepts both fascinating and accessible. I welcome you to join me on this journey of exploration and understanding.",
          cls="text-slate-700 dark:text-slate-300 leading-relaxed transition-colors"),
        cls="mb-10"
    )

    connect_section = Article(
        H2("Let's Connect", cls="text-2xl font-bold mb-4 dark:text-slate-100 transition-colors"),
        P("I value dialogue and welcome your thoughts, questions, or suggestions for topics you'd like to see covered. Feel free to reach out through any of the channels below.",
          cls="mb-6 text-slate-700 dark:text-slate-300 transition-colors"),
        Div(
            Div(
                Lucide("mail", size="20", cls="text-slate-600 dark:text-slate-400 transition-colors"),
                A("email",
                  href="mailto:pyrrhonianpig@gmail.com",
                  cls="text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-slate-100 transition-colors focus:outline-none focus:ring-2 focus:ring-indigo-500"),
                cls="flex items-center gap-3"
            ),
            Div(
                Lucide("twitter", size="20", cls="text-slate-600 dark:text-slate-400 transition-colors"),
                A("twitter",
                  href="https://twitter.com/zhugangliet",
                  cls="text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-slate-100 transition-colors focus:outline-none focus:ring-2 focus:ring-indigo-500"),
                cls="flex items-center gap-3"
            ),
            Div(
                Lucide("github", size="20", cls="text-slate-600 dark:text-slate-400 transition-colors"),
                A("github",
                  href="https://github.com/zhuganglie",
                  cls="text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-slate-100 transition-colors focus:outline-none focus:ring-2 focus:ring-indigo-500"),
                cls="flex items-center gap-3"
            ),
            cls="space-y-3 bg-slate-50 dark:bg-slate-800 p-6 rounded-lg transition-colors"
        ),
        cls="mb-10"
    )

    content = Div(
        hero_section,
        Div(
            mission_section,
            focus_section,
            background_section,
            connect_section,
            cls="max-w-3xl mx-auto"
        ),
        cls="space-y-8"
    )

    return root_layout(
        Titled("About", content),
        current_path
    )
