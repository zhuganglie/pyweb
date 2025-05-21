from fasthtml.common import fast_app, Script, Link, Style, MarkdownJS, HighlightJS, serve, Socials, Favicon
from blog import get_blog_index, get_post, get_posts_by_tag, get_tag_list, get_posts, get_all_tags
from home import get_home_page
from about import get_about_page
from sitemap import generate_sitemap


# SEO Configuration
site_name = "YZC"
site_desc = "Insights from political science research"
site_url = "https://yzc.vercel.app"  # Update this to your actual domain
social_img = "/public/images/social/card-template.svg"
twitter_creator = "@YZC"  # Update this to your Twitter handle

app, rt = fast_app(
    live=True,
    pico=False,
    hdrs=(
        # Google Analytics
        Script(src="https://www.googletagmanager.com/gtag/js?id=G-P3PES4S528", async_=True),
        Script("window.dataLayer = window.dataLayer || [];\nfunction gtag(){dataLayer.push(arguments);}\ngtag('js', new Date());\ngtag('config', 'G-P3PES4S528');"),
        # SEO and Social Media Cards
        Socials(
            title=site_name,
            site_name=site_name,
            description=site_desc,
            image=social_img,
            url=site_url,
            w=1200,
            h=630,
            twitter_site="@YZC",
            creator=twitter_creator,
            card="summary_large_image"
        ),
        Favicon(
            light_icon="/public/favicon-32x32.png",
            dark_icon="/public/favicon-32x32.png"
        ),
        # Stylesheets
        Link(rel='stylesheet', href='/public/marked.css', type='text/css'),
        Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Ubuntu:wght@400;700&display=swap", type="text/css"),
        MarkdownJS(),
        HighlightJS(langs=['python', 'javascript', 'html', 'css']),
        Script(src="https://cdn.tailwindcss.com"),
        Style(
            ".active { font-weight: bold;}",
            "body {font-family: 'Ubuntu', sans-serif;}"
            ),

    ))

@rt("/")
def index(req):  # Changed function name to be more descriptive
    return get_home_page(req.url.path)

@rt("/posts")
def blog_index(req):  # Changed function name to be more descriptive
    return get_blog_index(req.url.path)

@rt("/posts/{slug}")
def get(slug: str, req):  # Changed function name to be more descriptive
    return get_post(slug, req.url.path)

@rt("/tags/{tag}")
def posts_by_tag(tag: str, req):  # Changed function name to be more descriptive
    return get_posts_by_tag(tag, req.url.path)

@rt("/tags")
def tag_list(req):  # Changed function name to be more descriptive
    return get_tag_list(req.url.path)

@rt("/about")
def about(req):
    return get_about_page(req.url.path)

@rt("/sitemap.xml")
def sitemap():
    """Generates and returns the sitemap XML."""
    return generate_sitemap(site_url)

if __name__ == "__main__":  # Added standard Python idiom
    serve()
