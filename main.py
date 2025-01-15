from fasthtml.common import *

app, rt = fast_app()

@rt('/')
def index():

    return Div("Hello")


serve()
