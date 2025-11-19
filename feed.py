from fasthtml.common import *
from datetime import datetime
import pytz

def generate_rss(posts, site_url="https://yzc.vercel.app", site_title="YZC", site_desc="Insights from political science research"):
    """Generates an RSS 2.0 feed."""
    
    rss_template = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
    <title>{title}</title>
    <link>{site_url}</link>
    <description>{description}</description>
    <language>en-us</language>
    <lastBuildDate>{build_date}</lastBuildDate>
    <atom:link href="{site_url}/feed.xml" rel="self" type="application/rss+xml" />
    {items}
</channel>
</rss>"""

    item_template = """
    <item>
        <title>{title}</title>
        <link>{link}</link>
        <guid>{guid}</guid>
        <pubDate>{pub_date}</pubDate>
        <description><![CDATA[{description}]]></description>
    </item>"""

    items = []
    for post in posts:
        # Ensure date is timezone aware or format correctly
        date = post.get('date')
        if date:
            if date.tzinfo is None:
                date = pytz.utc.localize(date)
            pub_date = date.strftime("%a, %d %b %Y %H:%M:%S %z")
        else:
            pub_date = ""

        link = f"{site_url}/posts/{post['slug']}"
        
        items.append(item_template.format(
            title=post['title'],
            link=link,
            guid=link,
            pub_date=pub_date,
            description=post.get('excerpt', '')
        ))

    return rss_template.format(
        title=site_title,
        site_url=site_url,
        description=site_desc,
        build_date=datetime.now(pytz.utc).strftime("%a, %d %b %Y %H:%M:%S %z"),
        items="".join(items)
    )
