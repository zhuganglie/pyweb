from fasthtml.common import Main, Header, Footer, Nav, P, B, H1, A, Ul, Li, Div, Span
from datetime import datetime
from urllib.parse import unquote

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
          # Decode URL-encoded parts, capitalize, and replace hyphens with spaces for display
          display_text = unquote(part).replace('-', ' ').title()
          breadcrumb_items.append(A(display_text, href=current_path_build))

      # Create breadcrumb navigation with separators and truncation
      breadcrumbs = Nav(
              Div(
                  id="breadcrumb-container",
                  *[item for pair in zip(
                      breadcrumb_items,
                      ["/" for _ in range(len(breadcrumb_items)-1)] + [""]
                  ) for item in pair],
                  cls="flex items-center gap-2 text-sm text-gray-600 overflow-hidden whitespace-nowrap"
              ),
              cls="w-full mb-4"
          ) if path_parts else ""

      # Estimate the maximum number of characters allowed in breadcrumbs
      max_chars = 30  # Adjust this value based on your design and font size

      # Calculate the total number of characters in the breadcrumbs
      total_chars = sum(len(item.children[0]) for item in breadcrumb_items)

      # Truncate breadcrumbs if necessary
      if total_chars > max_chars:
          chars_to_remove = total_chars - max_chars
          for i in range(len(breadcrumb_items) - 1, 0, -1):
              item = breadcrumb_items[i]
              if chars_to_remove <= 0:
                  break
              text_len = len(item.children[0])
              if text_len <= chars_to_remove:
                  chars_to_remove -= text_len
                  breadcrumb_items.pop(i)
              else:
                  item.children = (item.children[0][:-chars_to_remove] + "...",)
                  chars_to_remove = 0

      # Create breadcrumb navigation with separators and truncation
      breadcrumbs = Nav(
          Div(
              *[item for pair in zip(
                  breadcrumb_items,
                  ["/" for _ in range(len(breadcrumb_items) - 1)] + [""]
              ) for item in pair],
              cls="flex items-center gap-2 text-sm text-gray-600 overflow-hidden whitespace-nowrap"
          ),
          cls="w-full mb-4"
      ) if path_parts else ""

      return Main(
          Header(
              H1(A("YZC", href="/", cls="no-underline text-slate-800 text-3xl lg:text-4xl font-extrabold hover:text-slate-600 transition-colors")),
              Nav(
                  Ul(
                      Li(A("Home", href="/"), cls="active hover:bg-slate-100 rounded-lg py-2 px-3 transition-colors" if current_path == "/" or current_path.startswith("/posts") else "hover:bg-slate-100 rounded-lg py-2 px-3 transition-colors"),
                      Li(A("About", href="/about"), cls="active hover:bg-slate-100 rounded-lg py-2 px-3 transition-colors" if current_path.startswith("/about") else "hover:bg-slate-100 rounded-lg py-2 px-3 transition-colors"),
                      Li(A("Tags", href="/tags"), cls="active hover:bg-slate-100 rounded-lg py-2 px-3 transition-colors" if current_path.startswith("/tags") else "hover:bg-slate-100 rounded-lg py-2 px-3 transition-colors"),
                      cls="list-none flex gap-2 sm:gap-6 text-base sm:text-lg whitespace-nowrap"
                  )
              ),
              cls="flex flex-col items-center justify-center py-8 px-4 gap-8 mb-8 border-b border-slate-200"
          ),
          breadcrumbs,
          content,
          Footer(
              P(f"© {datetime.now().year}", B('YZC', cls="mx-3 text-slate-700")),
              cls="flex justify-center py-8 px-4 mt-12 text-slate-500 border-t border-slate-200"
          ),
          cls="flex flex-col items-center justify-center w-full max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 min-h-screen bg-white"
      )
