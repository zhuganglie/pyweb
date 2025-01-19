from fasthtml.common import *
from datetime import datetime

def root_layout(content, current_path="/"):
    return Main(
            Header(
                H1(A("Insights", href="/", cls="no-underline text-black text-3xl lg:text-4xl font-bold")),
                Nav(
                    Ul(
                        Li(A("Home", href="/"), cls="active" if current_path == "/" or current_path.startswith("/posts") else ""),
                        Li(A("About", href="/about"), cls="active" if current_path.startswith("/about")  else ""),
                        Li(A("Tags", href="/tags"), cls="active" if current_path.startswith("/tags")  else ""),
                        cls="list-none flex gap-8"
                    )
                ),
                cls="flex flex-col items-center justify-center p-4 gap-8 mb-8"
            ),
            content,
            Footer(
                P(f"© {datetime.now().year}", B('Insights', cls="ml-5") ),
                cls="flex justify-center p-4"
            ),
            cls="flex flex-col items-center justify-center w-full lg:w-2/3 m-auto p-2"
)
