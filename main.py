from fasthtml.common import fast_app, Script, Link, Style, MarkdownJS, HighlightJS, serve, Socials, Favicon, Response
from blog import get_blog_index, get_post, get_posts_by_tag, get_tag_list, get_posts, get_all_tags
from home import get_home_page
from about import get_about_page
from sitemap import generate_sitemap
from feed import generate_rss


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
        Link(rel="preconnect", href="https://fonts.googleapis.com"),
        Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=True),
        Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap", type="text/css"),
        MarkdownJS(),
        HighlightJS(langs=['python', 'javascript', 'html', 'css']),
        Script(src="https://cdn.tailwindcss.com"),
        Script("""
            tailwind.config = {
                darkMode: 'class',
                theme: {
                    extend: {
                        fontFamily: {
                            sans: ['Inter', 'sans-serif'],
                            display: ['Outfit', 'sans-serif'],
                        },
                        colors: {
                            primary: {
                                50: '#f5f3ff',
                                100: '#ede9fe',
                                200: '#ddd6fe',
                                300: '#c4b5fd',
                                400: '#a78bfa',
                                500: '#8b5cf6',
                                600: '#7c3aed',
                                700: '#6d28d9',
                                800: '#5b21b6',
                                900: '#4c1d95',
                                950: '#2e1065',
                            },
                            secondary: {
                                50: '#fff1f2',
                                100: '#ffe4e6',
                                200: '#fecdd3',
                                300: '#fda4af',
                                400: '#fb7185',
                                500: '#f43f5e',
                                600: '#e11d48',
                                700: '#be123c',
                                800: '#9f1239',
                                900: '#881337',
                                950: '#4c0519',
                            }
                        },
                        transitionProperty: {
                            'theme': 'background-color, border-color, color, fill, stroke',
                        }
                    }
                }
            }
        """),
        Script(src="/public/ui.js"),
        Style(
            ".glass { background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border-bottom: 1px solid rgba(255, 255, 255, 0.3); }",
            "html.dark .glass { background: rgba(15, 23, 42, 0.7); border-bottom: 1px solid rgba(255, 255, 255, 0.05); }",
            ".active { font-weight: 600; color: #7c3aed; }",
            "html.dark .active { color: #a78bfa; }",
            "body { font-family: 'Inter', sans-serif; transition: background-color 0.3s ease, color 0.3s ease; }",
            "h1, h2, h3, h4, h5, h6 { font-family: 'Outfit', sans-serif; }",
            "html.dark { color-scheme: dark; }",
            # Screen reader only utility class
            ".sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0, 0, 0, 0); white-space: nowrap; border-width: 0; }",
            # Focus visible improvements
            "a:focus-visible, button:focus-visible { outline: 2px solid #6366f1; outline-offset: 2px; border-radius: 4px; }",
            # Smooth scrolling
            "html { scroll-behavior: smooth; }",
            # Loading images
            "img { image-rendering: auto; }",
            # Button hover improvements
            "button { cursor: pointer; }",
            # Selection color
            "::selection { background-color: #8b5cf6; color: white; }",
            "html.dark ::selection { background-color: #7c3aed; color: white; }",
            # Reduced motion support for accessibility
            "@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation-duration: 0.01ms !important; animation-iteration-count: 1 !important; transition-duration: 0.01ms !important; scroll-behavior: auto !important; } }"
            ),

    ))

@rt("/")
def index(req):  # Changed function name to be more descriptive
    return get_home_page(req.url.path)

@rt("/posts")
def blog_index(req, page: int = 1):  # Changed function name to be more descriptive
    return get_blog_index(req.url.path, page)

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

@rt("/feed.xml")
def feed():
    """Generates and returns the RSS feed."""
    posts = get_posts()
    return Response(generate_rss(posts, site_url, site_name, site_desc), headers={"Content-Type": "application/xml"})

if __name__ == "__main__":  # Added standard Python idiom
    serve()
