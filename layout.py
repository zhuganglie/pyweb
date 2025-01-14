from fasthtml.components import Container, Titled
from nav import navbar

def layout(title, *content):
    return Titled(title, Container(navbar(), *content))
