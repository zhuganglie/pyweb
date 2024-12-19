from fasthtml.common import *

def post_detail_template(title, date, tags, content):
    return Div(
        Div(H1(title, style="text-align: center;"),
            P(f"Date: {date}", style="text-align: center;")),
        Div(NotStr(content)),
        P(f"Tags: {', '.join(tags)}", style="text-align: left;")
    )
