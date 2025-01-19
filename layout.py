from fasthtml.common import *
from datetime import datetime

def root_layout(content, current_path="/"):
    return Container(
            Header(
                H1(A("Insights", href="/", style="text-decoration: none; color: black;")),
                Nav(
                    Ul(
                        Li(A("Home", href="/"), cls="active" if current_path == "/" or current_path.startswith("/posts") else "", style="text-decoration:none; color:black;"),
                        Li(A("About", href="/about"), cls="active" if current_path.startswith("/about")  else "", style="text-decoration:none; color:black;"),
                        Li(A("Tags", href="/tags"), cls="active" if current_path.startswith("/tags")  else "", style="text-decoration:none; color:black;"),
                        cls="list-none flex gap-10"
                    )
                ),
                cls="flex flex-col justify-center p-4"
            ),
            content,
            Footer(
                P(f"© {datetime.now().year}", B('Insights', cls="ml-5") ),
                cls="flex justify-center p-4"
            ),
            cls=""
)
