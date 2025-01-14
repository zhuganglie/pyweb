from fasthtml.components import A, Li, Ul, Div

def navbar():
    links = [
        Li(A("Home", href="/", cls="text-white hover:text-gray-200")),
        Li(A("Tags", href="/tags", cls="text-white hover:text-gray-200")),
    ]
    return Div(Ul(*links, cls="flex space-x-4"), cls="bg-gray-800 p-4")
