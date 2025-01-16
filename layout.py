from fasthtml.common import *

def root_layout(content):
    return Titled(
        "Blog",
        Container(
            Header(
                H1(A("Blog", href="/")),
                Nav(
                    Ul(
                        Li(A("Home", href="/")),
                        Li(A("About", href="/about")),
                    )
                )
            ),
            content,
            Footer(
                P("© 2024 My Blog")
            )
        )
    )
