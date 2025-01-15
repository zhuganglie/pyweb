from fasthtml.common import *

app, rt = fast_app()

@rt('/')
def index():
 return Titled("FastHTML", P("Let's do this!"))


serve()
