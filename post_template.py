from fasthtml.common import *

def post_detail_template(title, date, tags, content):
    return Div(
        Div(H1(title, **{"class":"text-3xl font-bold text-center"}),
            P(f"Date: {date}", **{"class":"text-gray-600 text-center"})),
        Div(NotStr(content), **{"class":"my-4"}),
        P(f"Tags: {', '.join(tags)}", **{"class":"text-gray-500 text-left"})
    )
