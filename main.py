from fasthtml.common import fast_app, Script, Link, Style, MarkdownJS, HighlightJS, serve, Socials, Favicon, Response
from blog import get_blog_index, get_post, get_posts_by_tag, get_tag_list, get_posts, get_all_tags
from home import get_home_page
from about import get_about_page
from sitemap import generate_sitemap
from feed import generate_rss


# SEO Configuration
site_name = "YZC"
site_desc = "探索人工智能如何助力社会科学传播与研究"
site_url = "https://yzc.vercel.app"  # Update this to your actual domain
social_img = "/public/images/social/card-template.svg"
twitter_creator = "@YZC"  # Update this to your X handle

_fast_app_res = fast_app(
    live=False,
    pico=False,
    html_kw={"lang": "zh-CN"},
    hdrs=(
        # Google Analytics
        #Script(src="https://www.googletagmanager.com/gtag/js?id=G-P3PES4S528", async_=True),
        #Script("window.dataLayer = window.dataLayer || [];\nfunction gtag(){dataLayer.push(arguments);}\ngtag('js', new Date());\ngtag('config', 'G-P3PES4S528');"),
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
        Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap", type="text/css"),
        MarkdownJS(),
        Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css"),
        HighlightJS(langs=['python', 'javascript', 'html', 'css']),
        Script(src="https://cdn.tailwindcss.com?plugins=typography"),
        Script("""
            tailwind.config = {
                darkMode: 'media',
                theme: {
                    extend: {
                        fontFamily: {
                            sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'],
                            display: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'],
                        },
                        colors: {
                            primary: {
                                50: '#f9fafb',
                                100: '#f1f5f9',
                                200: '#e2e8f0',
                                300: '#cbd5e1',
                                400: '#94a3b8',
                                500: '#64748b',
                                600: '#475569',
                                700: '#334155',
                                800: '#1e293b',
                                900: '#0f172a',
                                950: '#020617',
                            }
                        },
                        transitionProperty: {
                            'theme': 'background-color, border-color, color, fill, stroke',
                        },
                        typography: {
                            DEFAULT: {
                                css: {
                                    color: '#37352f',
                                    a: {
                                        color: 'inherit',
                                        textDecoration: 'underline',
                                        textDecorationThickness: '1px',
                                        textUnderlineOffset: '2px',
                                        '&:hover': { color: '#0f172a' },
                                    },
                                    h1: { color: '#0f172a', fontWeight: '600', letterSpacing: '-0.02em' },
                                    h2: { color: '#0f172a', fontWeight: '600', letterSpacing: '-0.02em', borderBottom: '1px solid #e2e8f0', paddingBottom: '0.3em' },
                                    h3: { color: '#0f172a', fontWeight: '600' },
                                    strong: { color: '#0f172a', fontWeight: '600' },
                                    code: { color: '#eb5757', backgroundColor: 'rgba(135,131,120,0.15)', padding: '0.2em 0.4em', borderRadius: '3px', fontWeight: '400' },
                                    'code::before': { content: '""' },
                                    'code::after': { content: '""' },
                                    blockquote: { 
                                        borderLeftColor: '#0f172a', 
                                        fontStyle: 'normal', 
                                        color: '#f3f4f6', 
                                        fontWeight: '450', 
                                        borderLeftWidth: '4px',
                                        backgroundColor: '#2d2d2d',
                                        padding: '1em 1.5em',
                                        borderRadius: '4px',
                                    },
                                    'blockquote p:first-of-type::before': { content: 'none' },
                                    'blockquote p:last-of-type::after': { content: 'none' },
                                },
                            },
                            invert: {
                                css: {
                                    color: '#d4d4d4',
                                    a: { '&:hover': { color: '#f8fafc' } },
                                    h1: { color: '#f8fafc' },
                                    h2: { color: '#f8fafc', borderBottomColor: '#334155' },
                                    h3: { color: '#f8fafc' },
                                    strong: { color: '#f8fafc' },
                                    code: { color: '#ff7b72', backgroundColor: 'rgba(255,255,255,0.1)' },
                                    blockquote: { 
                                        borderLeftColor: '#f8fafc', 
                                        color: '#f3f4f6',
                                        backgroundColor: '#2d2d2d',
                                    },
                                },
                            },
                        },
                    }
                }
            }
        """),
        Script(src="/public/ui.js"),
        Style(
            ".notion-header { background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(8px); border-bottom: 1px solid #f1f5f9; }",
            "@media (prefers-color-scheme: dark) { .notion-header { background: rgba(15, 23, 42, 0.95); border-bottom: 1px solid #1e293b; } }",
            ".active { font-weight: 600; color: #0f172a; }",
            "@media (prefers-color-scheme: dark) { .active { color: #f8fafc; } }",
            "body { font-family: 'Inter', sans-serif; transition: background-color 0.3s ease, color 0.3s ease; color: #37352f; background-color: #ffffff; }",
            "@media (prefers-color-scheme: dark) { body { color: #d4d4d4; background-color: #191919; } }",
            "h1, h2, h3, h4, h5, h6 { font-family: 'Inter', sans-serif; font-weight: 700; color: #050505; letter-spacing: -0.02em; }",
            "@media (prefers-color-scheme: dark) { h1, h2, h3, h4, h5, h6 { color: #ffffff !important; } }",
            "@media (prefers-color-scheme: dark) { :root { color-scheme: dark; } }",
            ".sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0, 0, 0, 0); white-space: nowrap; border-width: 0; }",
            "a:focus-visible, button:focus-visible { outline: 2px solid #94a3b8; outline-offset: 2px; border-radius: 4px; }",
            "html { scroll-behavior: smooth; }",
            "img { image-rendering: auto; }",
            "button { cursor: pointer; }",
            "::selection { background-color: #e2e8f0; color: #0f172a; }",
            "@media (prefers-color-scheme: dark) { ::selection { background-color: #334155; color: #f8fafc; } }",
            "@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation-duration: 0.01ms !important; animation-iteration-count: 1 !important; transition-duration: 0.01ms !important; scroll-behavior: auto !important; } }"
            ),

    ))

app = _fast_app_res[0]
rt = _fast_app_res[1]

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

@rt("/sitemap")
def sitemap():
    """Generates and returns the sitemap XML."""
    return generate_sitemap(site_url)

@rt("/feed")
def feed():
    """Generates and returns the RSS feed."""
    posts = get_posts()
    return Response(generate_rss(posts, site_url, site_name, site_desc), headers={"Content-Type": "application/xml"})

if __name__ == "__main__":  # Added standard Python idiom
    serve()
