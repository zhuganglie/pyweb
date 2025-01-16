from fasthtml.common import *

def root_layout(content):
    return Titled(
        "",
        Container(
            Header(
                H1(A("Blog", href="/", style="text-decoration: none; color: black;")),
                Nav(
                    Ul(
                        Li(A("Home", href="/", style="text-decoration:none")),
                        Li(A("About", href="/about", style="text-decoration:none")),
                        Li(A("Tags", href="/tags", style="text-decoration:none")),
                        style="list-style-type:none; display:flex; gap:20px;"
                    )
                )
            ),
            content,
            Footer(
                P("© 2024 My Blog")
            )
        )
    )
