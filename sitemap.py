from blog import get_posts, get_all_tags
from urllib.parse import quote
from datetime import datetime

def generate_sitemap(site_url: str) -> str:
    """
    Generates a sitemap for search engines.

    Args:
        site_url (str): The base URL of the website.

    Returns:
        str: The sitemap XML content.
    """

    def url_entry(loc: str, lastmod: datetime = None, changefreq: str = None, priority: str = None) -> str:
        """
        Creates a URL entry for the sitemap.

        Args:
            loc (str): The URL location.
            lastmod (datetime, optional): Last modification date. Defaults to None.
            changefreq (str, optional): Change frequency. Defaults to None.
            priority (str, optional): Priority. Defaults to None.

        Returns:
            str: The URL entry XML.
        """
        entry = [f"<loc>{site_url}{loc}</loc>"]
        if lastmod:
            entry.append(f"<lastmod>{lastmod:%Y-%m-%d}</lastmod>")
        if changefreq:
            entry.append(f"<changefreq>{changefreq}</changefreq>")
        if priority:
            entry.append(f"<priority>{priority}</priority>")
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
        try:
            lastmod = post.get('date', datetime.now())
        except:
            lastmod = datetime.now()
        urls.append(url_entry(loc, lastmod=lastmod, changefreq="monthly", priority="0.9"))

    # Add all tag pages
    for tag in get_all_tags():
        urls.append(url_entry(f"/tags/{quote(tag)}", changefreq="weekly", priority="0.6"))

    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap_xml += '\n'.join(urls)
    sitemap_xml += '\n</urlset>'

    return sitemap_xml, {'Content-Type': 'application/xml'}
