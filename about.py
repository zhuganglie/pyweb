from fasthtml.common import Div, H2, H3, Li, P, Titled, Ul
from layout import root_layout

def get_about_page(current_path):
    content = Div(
    #    H1("About This Blog", cls="text-3xl font-bold mb-6"),

        Div(
            P("Welcome! This blog is dedicated to exploring the fundamental questions about our modern way of life and the choices that shape our society." , cls="mb-4"),

            P("Here we dive deep into topics like:", cls="mb-2"),

            Ul(
               Li("The evolution of modern society and technology"),
               Li("Cultural patterns and their impacts"),
               Li("Future trends and their implications"),
               Li("Philosophy and critical thinking about everyday life"),
            cls="list-disc pl-6 mb-4"
            ),

            P("I believe that understanding why we live the way we do is crucial for making informed decisions about our future, both individually and collectively.", cls="mb-4"),

            H2("About the Author", cls="text-2xl font-bold mt-8 mb-4"),

            P("""
              I'm a writer and thinker passionate about understanding the underlying
              patterns that shape our world. With a background in technology and
              humanities, I bring a multidisciplinary perspective to exploring life's
              big questions.
              """, cls="mb-4"),

            P("""
              Feel free to reach out and share your thoughts or suggest topics
              you'd like to see covered.
              """, cls="mb-4"),

            Div(
                H3("Contact", cls="text-xl font-bold mb-2"),
                P("Email: blog@example.com", cls="mb-2"),
                P("Twitter: @bloghandle", cls="mb-2"),
                P("GitHub: github.com/bloghandle"),
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
