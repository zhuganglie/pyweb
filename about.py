from fasthtml.common import Div, H2, H3, Li, P, Titled, Ul
from layout import root_layout

def get_about_page(current_path):
    content = Div(
    #    H1("About This Blog", cls="text-3xl font-bold mb-6"),

        Div(
            P("Welcome! This blog is dedicated to exploring interesting political science research that solves real-life puzzles and satisfies your curiosity." , cls="mb-4"),

            P("In this blog, we will explore:", cls="mb-2"),

            Ul(
               Li("Why democracies rise and fall"),
               Li("The causes and consequences of dictatorships"),
               Li("How political institutions shape economic outcomes"),
               Li("The role of culture and psychology in political behavior"),
            cls="list-disc pl-6 mb-4"
            ),

            P("I believe that making political science research accessible helps us better understand our society and make more informed decisions as citizens.", cls="mb-4"),

            H2("About the Author", cls="text-2xl font-bold mt-8 mb-4"),

            P("""
              With a background in political science and experience as a grassroots leader,
              I enjoy bridging the gap between academic research and everyday politics.
              This blog is my space to share fascinating political science insights in a
              way that helps everyone better understand the political world around us.
              """, cls="mb-4"),

            P("""
              Feel free to reach out and share your thoughts or suggest topics
              you'd like to see covered.
              """, cls="mb-4"),

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
