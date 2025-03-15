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
                        src="/public/images/avatar.jpeg",
                        alt="Profile Photo",
                        cls="w-32 h-32 rounded-full object-cover border-4 border-white shadow-lg"
                    ),
                    cls="relative -mt-16 mb-4"
                ),
                H1("About Me", cls="text-3xl font-bold mb-3"),
                P("A Reader with Passion", cls="text-xl text-slate-600 mb-6"),
                Div(
                    A(Lucide("mail", size="18"), "email",
                      href="mailto:pyrrhonianpig@gmail.com",
                      cls="flex items-center gap-2 text-slate-700 hover:text-slate-900"),
                    A(Lucide("twitter", size="18"), "twitter",
                      href="https://twitter.com/zhugangliet",
                      cls="flex items-center gap-2 text-slate-700 hover:text-slate-900"),
                    A(Lucide("github", size="18"), "github",
                      href="https://github.com/zhuganglie",
                      cls="flex items-center gap-2 text-slate-700 hover:text-slate-900"),
                    cls="flex flex-col sm:flex-row gap-4 sm:gap-6"
                ),
                cls="text-center sm:text-left"
            ),
            cls="bg-white p-8 rounded-lg shadow-sm border border-slate-100 relative mt-12"
        ),
        cls="bg-gradient-to-br from-slate-700 to-slate-900 pt-24 pb-12 px-6 rounded-lg mb-12"
    )

    # Main content sections
    mission_section = Article(
        H2("My Mission", cls="text-2xl font-bold mb-4 flex items-center gap-2"),
        P("Welcome to my blog where I explore complex political science research and make it accessible to curious minds. I believe that understanding political systems and behaviors helps us navigate our social world and make more informed decisions.",
          cls="mb-4 text-slate-700 leading-relaxed"),
        P("This platform is dedicated to bridging the gap between academic knowledge and everyday understanding, presenting research findings in clear, engaging ways that connect to real-world issues.",
          cls="mb-4 text-slate-700 leading-relaxed"),
        cls="mb-10"
    )

    focus_section = Article(
        H2("Research Focus", cls="text-2xl font-bold mb-4 flex items-center gap-2"),
        P("My work explores a range of interconnected topics in political science:", cls="mb-4 text-slate-700"),
        Div(
            Div(
                Lucide("landmark", size="24", cls="text-indigo-600 mb-2"),
                H3("Political Institutions", cls="font-bold mb-2"),
                P("The evolution of democracy and authoritarianism, institutional design, and governance systems",
                  cls="text-slate-600"),
                cls="p-4 bg-slate-50 rounded-lg"
            ),
            Div(
                Lucide("scale", size="24", cls="text-amber-600 mb-2"),
                H3("Political Economy", cls="font-bold mb-2"),
                P("How political decisions shape economic outcomes, resource distribution, and development patterns",
                  cls="text-slate-600"),
                cls="p-4 bg-slate-50 rounded-lg"
            ),
            Div(
                Lucide("users", size="24", cls="text-emerald-600 mb-2"),
                H3("Political Behavior", cls="font-bold mb-2"),
                P("The psychology of political decision-making, social movements, and collective action",
                  cls="text-slate-600"),
                cls="p-4 bg-slate-50 rounded-lg"
            ),
            Div(
                Lucide("globe", size="24", cls="text-blue-600 mb-2"),
                H3("Comparative Politics", cls="font-bold mb-2"),
                P("Cross-national patterns in politics, regional dynamics, and cultural influences on governance",
                  cls="text-slate-600"),
                cls="p-4 bg-slate-50 rounded-lg"
            ),
            cls="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6"
        ),
        cls="mb-10"
    )

    background_section = Article(
        H2("Personal Background", cls="text-2xl font-bold mb-4 flex items-center gap-2"),
        P("I'm an educator and researcher with a passion for social sciences. Beyond my academic work, I enjoy cycling through urban landscapes, reading across disciplines, and coding projects that bring data to life.",
          cls="mb-4 text-slate-700 leading-relaxed"),
        P("My experience as a grassroots community leader has shaped my perspective on how politics affects everyday lives. This combination of academic knowledge and practical engagement informs my approach to analyzing political phenomena.",
          cls="mb-4 text-slate-700 leading-relaxed"),
        P("Through this blog, I hope to share my enthusiasm for political science while making complex concepts both fascinating and accessible. I welcome you to join me on this journey of exploration and understanding.",
          cls="text-slate-700 leading-relaxed"),
        cls="mb-10"
    )

    connect_section = Article(
        H2("Let's Connect", cls="text-2xl font-bold mb-4"),
        P("I value dialogue and welcome your thoughts, questions, or suggestions for topics you'd like to see covered. Feel free to reach out through any of the channels below.",
          cls="mb-6 text-slate-700"),
        Div(
            Div(
                Lucide("mail", size="20", cls="text-slate-600"),
                A("email",
                  href="mailto:pyrrhonianpig@gmail.com",
                  cls="text-slate-700 hover:text-slate-900"),
                cls="flex items-center gap-3"
            ),
            Div(
                Lucide("twitter", size="20", cls="text-slate-600"),
                A("twitter",
                  href="https://twitter.com/zhugangliet",
                  cls="text-slate-700 hover:text-slate-900"),
                cls="flex items-center gap-3"
            ),
            Div(
                Lucide("github", size="20", cls="text-slate-600"),
                A("github",
                  href="https://github.com/zhuganglie",
                  cls="text-slate-700 hover:text-slate-900"),
                cls="flex items-center gap-3"
            ),
            cls="space-y-3 bg-slate-50 p-6 rounded-lg"
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
