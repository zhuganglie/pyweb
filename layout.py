from fasthtml.common import Main, Header, Footer, Nav, P, B, H1, A, Ul, Li, Div, Span
from datetime import datetime

def root_layout(content, current_path="/"):
    # Create breadcrumbs based on current_path
      path_parts = [p for p in current_path.split('/') if p]
      breadcrumb_items = []
      current_path_build = ''

      # Always start with Home
      breadcrumb_items.append(A("Home", href="/"))

      # Build the rest of the breadcrumbs
      for part in path_parts:
          current_path_build += f'/{part}'
          # Capitalize and replace hyphens with spaces for display
          display_text = part.replace('-', ' ').title()
          breadcrumb_items.append(A(display_text, href=current_path_build))

      # Create breadcrumb navigation with separators and truncation
      breadcrumbs = Nav(
              Div(
                  *[item for pair in zip(
                      breadcrumb_items,
                      ["/" for _ in range(len(breadcrumb_items)-1)] + [""]
                  ) for item in pair],
                  cls="flex items-center gap-2 text-sm text-gray-600 overflow-hidden whitespace-nowrap"
              ),
              cls="w-full mb-4"
          ) if path_parts else ""

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
            breadcrumbs,
            content,
            Footer(
                P(f"© {datetime.now().year}", B('Insights', cls="mx-5")),
                cls="flex justify-center p-4"
            ),
            cls="flex flex-col items-center justify-center w-full lg:w-2/3 m-auto p-2"
)
