from fasthtml.components import A, Li, Ul, Div

def navbar():
    links = [
        Li(A("Home", href="/")),
        Li(A("Tags", href="/tags")),
    ]
    return Div(Ul(*links), cls="bg-gray-800 p-4")
