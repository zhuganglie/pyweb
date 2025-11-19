from fasthtml.common import Div, H1, H2, H3, Li, P, Titled, Ul, A, Img, Section, Article
from layout import root_layout
from lucide_fasthtml import Lucide

def get_about_page(current_path):
    # Hero section with profile info
    hero_section = Section(
        Div(
            Img(
                src="images/avatar.jpg",
                alt="Profile Photo",
                loading="lazy",
                cls="w-48 h-48 rounded-full object-cover border-4 border-white dark:border-slate-800 shadow-2xl mb-8 mx-auto"
            ),
            H1("About Me", cls="text-5xl font-extrabold mb-4 text-slate-900 dark:text-white tracking-tight"),
            P("Educator • Researcher • Community Leader", cls="text-xl font-medium text-primary-600 dark:text-primary-400 mb-8 uppercase tracking-wider"),
            Div(
                A(Lucide("mail", size="24"), href="mailto:pyrrhonianpig@gmail.com", cls="p-3 bg-white dark:bg-slate-800 rounded-full text-slate-600 dark:text-slate-400 hover:text-primary-600 dark:hover:text-primary-400 hover:shadow-md transition-all hover:-translate-y-1", **{"aria-label": "Send email"}),
                A(Lucide("twitter", size="24"), href="https://twitter.com/zhugangliet", cls="p-3 bg-white dark:bg-slate-800 rounded-full text-slate-600 dark:text-slate-400 hover:text-primary-600 dark:hover:text-primary-400 hover:shadow-md transition-all hover:-translate-y-1", **{"aria-label": "Visit Twitter profile"}),
                A(Lucide("github", size="24"), href="https://github.com/zhuganglie", cls="p-3 bg-white dark:bg-slate-800 rounded-full text-slate-600 dark:text-slate-400 hover:text-primary-600 dark:hover:text-primary-400 hover:shadow-md transition-all hover:-translate-y-1", **{"aria-label": "Visit GitHub profile"}),
                cls="flex justify-center gap-6"
            ),
            cls="text-center max-w-3xl mx-auto"
        ),
        cls="py-20 px-4 bg-slate-50 dark:bg-slate-900/50 border-b border-slate-200 dark:border-slate-800 mb-20"
    )

    # Main content sections
    mission_section = Article(
        H2("My Mission", cls="text-3xl font-bold mb-6 text-slate-900 dark:text-white"),
        Div(
            P("Welcome to my blog where I explore complex political science research and make it accessible to curious minds. I believe that understanding political systems and behaviors helps us navigate our social world and make more informed decisions.",
              cls="text-lg text-slate-600 dark:text-slate-300 leading-relaxed mb-6"),
            P("This platform is dedicated to bridging the gap between academic knowledge and everyday understanding, presenting research findings in clear, engaging ways that connect to real-world issues.",
              cls="text-lg text-slate-600 dark:text-slate-300 leading-relaxed"),
            cls="prose prose-lg prose-slate dark:prose-invert max-w-none"
        ),
        cls="mb-24 max-w-3xl mx-auto px-4"
    )

    focus_section = Article(
        Div(
            H2("Research Focus", cls="text-3xl font-bold mb-4 text-slate-900 dark:text-white text-center"),
            P("My work explores a range of interconnected topics in political science.", cls="text-xl text-slate-600 dark:text-slate-400 text-center mb-12"),
            cls="max-w-3xl mx-auto px-4"
        ),
        Div(
            Div(
                Div(Lucide("landmark", size="32", cls="text-primary-600 dark:text-primary-400"), cls="mb-6 p-4 bg-primary-50 dark:bg-primary-900/30 rounded-2xl w-fit"),
                H3("Political Institutions", cls="text-xl font-bold mb-3 text-slate-900 dark:text-white"),
                P("The evolution of democracy and authoritarianism, institutional design, and governance systems",
                  cls="text-slate-600 dark:text-slate-400 leading-relaxed"),
                cls="p-8 bg-white dark:bg-slate-800 rounded-3xl border border-slate-100 dark:border-slate-700 hover:shadow-lg transition-all duration-300 hover:-translate-y-1"
            ),
            Div(
                Div(Lucide("scale", size="32", cls="text-secondary-600 dark:text-secondary-400"), cls="mb-6 p-4 bg-secondary-50 dark:bg-secondary-900/30 rounded-2xl w-fit"),
                H3("Political Economy", cls="text-xl font-bold mb-3 text-slate-900 dark:text-white"),
                P("How political decisions shape economic outcomes, resource distribution, and development patterns",
                  cls="text-slate-600 dark:text-slate-400 leading-relaxed"),
                cls="p-8 bg-white dark:bg-slate-800 rounded-3xl border border-slate-100 dark:border-slate-700 hover:shadow-lg transition-all duration-300 hover:-translate-y-1"
            ),
            Div(
                Div(Lucide("users", size="32", cls="text-emerald-600 dark:text-emerald-400"), cls="mb-6 p-4 bg-emerald-50 dark:bg-emerald-900/30 rounded-2xl w-fit"),
                H3("Political Behavior", cls="text-xl font-bold mb-3 text-slate-900 dark:text-white"),
                P("The psychology of political decision-making, social movements, and collective action",
                  cls="text-slate-600 dark:text-slate-400 leading-relaxed"),
                cls="p-8 bg-white dark:bg-slate-800 rounded-3xl border border-slate-100 dark:border-slate-700 hover:shadow-lg transition-all duration-300 hover:-translate-y-1"
            ),
            Div(
                Div(Lucide("globe", size="32", cls="text-blue-600 dark:text-blue-400"), cls="mb-6 p-4 bg-blue-50 dark:bg-blue-900/30 rounded-2xl w-fit"),
                H3("Comparative Politics", cls="text-xl font-bold mb-3 text-slate-900 dark:text-white"),
                P("Cross-national patterns in politics, regional dynamics, and cultural influences on governance",
                  cls="text-slate-600 dark:text-slate-400 leading-relaxed"),
                cls="p-8 bg-white dark:bg-slate-800 rounded-3xl border border-slate-100 dark:border-slate-700 hover:shadow-lg transition-all duration-300 hover:-translate-y-1"
            ),
            cls="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-6xl mx-auto px-4"
        ),
        cls="mb-24 bg-slate-50/50 dark:bg-slate-900/50 py-24"
    )

    background_section = Article(
        H2("Personal Background", cls="text-3xl font-bold mb-6 text-slate-900 dark:text-white"),
        Div(
            P("I'm an educator and researcher with a passion for social sciences. Beyond my academic work, I enjoy cycling through urban landscapes, reading across disciplines, and coding projects that bring data to life.",
              cls="text-lg text-slate-600 dark:text-slate-300 leading-relaxed mb-6"),
            P("My experience as a grassroots community leader has shaped my perspective on how politics affects everyday lives. This combination of academic knowledge and practical engagement informs my approach to analyzing political phenomena.",
              cls="text-lg text-slate-600 dark:text-slate-300 leading-relaxed mb-6"),
            P("Through this blog, I hope to share my enthusiasm for political science while making complex concepts both fascinating and accessible. I welcome you to join me on this journey of exploration and understanding.",
              cls="text-lg text-slate-600 dark:text-slate-300 leading-relaxed"),
            cls="prose prose-lg prose-slate dark:prose-invert max-w-none"
        ),
        cls="mb-24 max-w-3xl mx-auto px-4"
    )

    content = Div(
        hero_section,
        mission_section,
        focus_section,
        background_section,
        cls="w-full"
    )

    return root_layout(
        Titled("About", content),
        current_path
    )
