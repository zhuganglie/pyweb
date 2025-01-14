from fasthtml.components import Container, Titled, Main
from nav import navbar

def layout(title, *content):
    return Titled(title, Main(navbar(), Container(*content)))
