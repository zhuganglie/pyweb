from fasthtml.common import fast_app, Script, Link, Style, MarkdownJS, HighlightJS, serve, Socials, Favicon
from blog import get_blog_index, get_post, get_posts_by_tag, get_tag_list, get_posts, get_all_tags
from home import get_home_page
from datetime import datetime
from urllib.parse import quote
from about import get_about_page


# SEO Configuration
site_name = "YZC"
site_desc = "Insights on comparative politics and political economy"
site_url = "https://yzc.vercel.app"  # Update this to your actual domain
social_img = "/public/images/social/card-template.svg"
twitter_creator = "@YZC"  # Update this to your Twitter handle

app, rt = fast_app(
    live=True,
    pico=False,
    hdrs=(
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
            )
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
def sitemap(req):
    """Generate a sitemap for search engines."""
    def url_entry(loc, lastmod=None, changefreq=None, priority=None):
        entry = [f"<loc>{site_url}{loc}</loc>"]
        if lastmod: entry.append(f"<lastmod>{lastmod:%Y-%m-%d}</lastmod>")
        if changefreq: entry.append(f"<changefreq>{changefreq}</changefreq>")
        if priority: entry.append(f"<priority>{priority}</priority>")
        return f"<url>{''.join(entry)}</url>"

    urls = []
    
    # Add static pages
    urls.append(url_entry("/", changefreq="daily", priority="1.0"))
    urls.append(url_entry("/posts", changefreq="daily", priority="0.9"))
    urls.append(url_entry("/about", changefreq="monthly", priority="0.8"))
    urls.append(url_entry("/tags", changefreq="weekly", priority="0.7"))
    
    # Add all posts
    posts = get_posts()
    for post in posts:
        loc = f"/posts/{post['slug']}"
        lastmod = post.get('date', datetime.now())
        urls.append(url_entry(loc, lastmod=lastmod, changefreq="monthly", priority="0.9"))
    
    # Add all tag pages
    for tag in get_all_tags():
        urls.append(url_entry(f"/tags/{quote(tag)}", changefreq="weekly", priority="0.6"))
    
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap_xml += '\n'.join(urls)
    sitemap_xml += '\n</urlset>'
    
    return sitemap_xml, {'Content-Type': 'application/xml'}

if __name__ == "__main__":  # Added standard Python idiom
    serve()
