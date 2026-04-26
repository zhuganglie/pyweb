from feed import generate_rss
from blog import get_posts
from main import site_url, site_name, site_desc

def main():
    posts = get_posts()
    xml_content = generate_rss(posts, site_url, site_name, site_desc)
    with open('feed.xml', 'w', encoding='utf-8') as f:
        f.write(xml_content)
    print('feed.xml has been successfully generated!')

if __name__ == "__main__":
    main()
