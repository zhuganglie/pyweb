from fasthtml.common import Div, H2, H3, Li, P, Titled, Ul
from layout import root_layout

def get_about_page(current_path):
    content = Div(
        Div(
            P("Welcome! This blog explores political science research that solves real-life puzzles and satisfies curiosity.", cls="mb-4"),
            P("Topics include:", cls="mb-2"),
            Ul(
                Li("Why democracies rise and fall"),
                Li("Causes and consequences of dictatorships"),
                Li("How political institutions shape economic outcomes"),
                Li("The role of culture and psychology in political behavior"),
                cls="list-disc pl-6 mb-4"
            ),
            P("Making political science accessible helps us understand society and make informed decisions.", cls="mb-4"),
            H2("About the Author", cls="text-2xl font-bold mt-8 mb-4"),
            P("I'm an educator passionate about social sciences. I enjoy cycling, reading, and coding. As a grassroots leader, I value community engagement.", cls="mb-4"),
            P("This blog shares my passion for political science, making it fascinating and accessible. Enjoy the journey!", cls="mb-4"),
            P("Feel free to reach out with thoughts or topic suggestions.", cls="mb-4"),
            Div(
                H3("Contact", cls="text-xl font-bold mb-2"),
                P("Email: pyrrhonianpig@gmail.com", cls="mb-2"),
                P("Twitter: @zhugangliet", cls="mb-2"),
                P("GitHub: github.com/zhuganglie"),
                cls="bg-gray-100 p-6 rounded-lg mt-8",
            ),
            cls="prose max-w-none",
        ),
        cls="mt-8"
    )

    return root_layout(
        Titled("About", content),
        current_path
    )
