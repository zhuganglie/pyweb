from fasthtml.common import *

def post_detail_template(title, date, tags, content):
    return Div(
        Div(
            H1(title, **{"class": "text-3xl font-bold text-center"}),
            P(f"Date: {date}", **{"class": "text-gray-600 text-center"}),
            **{"class": "text-center"}
        ),
        Div(content, **{"class": "my-4 prose"}),
        Div("Tags: ", *[A(tag, href=f"/tag/{tag}", cls="text-blue-500 hover:text-blue-700 no-underline mr-2") for tag in tags], cls= "text-gray-500 text-left")
    )
