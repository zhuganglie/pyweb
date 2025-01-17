from fasthtml.common import *
from datetime import datetime

def root_layout(content, current_path="/"):
    return Container(
            Header(
                H1(A("Why?", href="/", style="text-decoration: none; color: black;")),
                Nav(
                    Ul(
                        Li(A("Home", href="/", style="text-decoration:none; color:black;"), cls="active" if current_path == "/" or current_path.startswith("/posts") else ""),
                        Li(A("About", href="/about", style="text-decoration:none; color:black;"), cls="active" if current_path.startswith("/about")  else ""),
                        Li(A("Tags", href="/tags", style="text-decoration:none; color:black;"), cls="active" if current_path.startswith("/tags")  else ""),
                        style="list-style-type:none; display:flex; gap:20px;"
                    )
                )
            ),
            content,
            Footer(
                P(f"© {datetime.now().year}", B('Why?', style="margin-left:10px;") )
            )
        )
