from fasthtml.common import *

def root_layout(content, current_path="/"):
    return Titled(
        "",
        Container(
            Header(
                H1(A("Blog", href="/", style="text-decoration: none; color: black;")),
                Nav(
                    Ul(
                        Li(A("Home", href="/", style="text-decoration:none"), cls="active" if current_path == "/" or current_path.startswith("/posts") else ""),
                        Li(A("About", href="/about", style="text-decoration:none"), cls="active" if current_path.startswith("/about")  else ""),
                        Li(A("Tags", href="/tags", style="text-decoration:none"), cls="active" if current_path.startswith("/tags")  else ""),
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
