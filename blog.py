import os
import re
import math
import frontmatter
from fasthtml.common import *
from datetime import datetime
from lucide_fasthtml import Lucide
from urllib.parse import unquote, quote
from functools import lru_cache
from layout import root_layout

POSTS_DIR = "posts"
WORDS_PER_MINUTE = 200
DEFAULT_EXCERPT_LENGTH = 300

# Post cache to avoid file system operations on every request
_posts_cache = None

class PostMetrics:
    """Helper class for calculating post metrics like read time and excerpts"""

    @staticmethod
    def calculate_read_time(content):
        """Calculate the read time in minutes for given content."""
        word_count = len(re.findall(r'\w+', content))
        minutes = math.ceil(word_count / WORDS_PER_MINUTE)
        return max(1, minutes)  # Ensure at least 1 minute read time

    @staticmethod
    def generate_excerpt(content, max_length=DEFAULT_EXCERPT_LENGTH):
        """Generate a short excerpt from the content."""
        # Remove markdown headers, code blocks, and special characters
        clean_content = re.sub(r'#{1,6}\s.*\n', '', content)
        clean_content = re.sub(r'```.*?```', '', clean_content, flags=re.DOTALL)
        clean_content = re.sub(r'[*_`]', '', clean_content)

        # Get first paragraph or truncate to max_length
        paragraphs = clean_content.split('\n\n')
        excerpt = next((p.strip() for p in paragraphs if p.strip()), '')

        if len(excerpt) > max_length:
            excerpt = excerpt[:max_length].rsplit(' ', 1)[0] + '...'
        return excerpt

class PostRepository:
    """Repository class to manage post data operations"""

    @staticmethod
    @lru_cache(maxsize=1)
    def get_posts():
        """Fetch all posts with metadata, sorted by date."""
        global _posts_cache
        if _posts_cache is not None:
            return _posts_cache

        posts = []
        if not os.path.exists(POSTS_DIR):
            return posts

        for filename in os.listdir(POSTS_DIR):
            if not filename.endswith(".md"):
                continue

            try:
                with open(os.path.join(POSTS_DIR, filename), 'r', encoding='utf-8') as f:
                    post = frontmatter.load(f)

                    # Process post metadata
                    post['slug'] = filename[:-3]
                    post['tags'] = post.get('tags', [])

                    # Handle date parsing
                    date = post.get('date', None)
                    if date:
                        try:
                            post['date'] = datetime.fromisoformat(str(date))
                        except (ValueError, TypeError):
                            post['date'] = datetime.min

                    # Skip draft posts
                    if post.get('draft') == True:
                        continue

                    # Add computed fields
                    post['excerpt'] = post.get('excerpt') or PostMetrics.generate_excerpt(post.content)
                    post['read_time'] = PostMetrics.calculate_read_time(post.content)

                    posts.append(post)
            except Exception as e:
                print(f"Error loading post {filename}: {e}")

        # Sort posts by date, newest first
        posts.sort(key=lambda post: post.get('date', datetime.min), reverse=True)
        _posts_cache = posts

        return posts

    @staticmethod
    def get_post_by_slug(slug):
        """Find a specific post by its slug."""
        return next((post for post in PostRepository.get_posts() if post['slug'] == slug), None)

    @staticmethod
    def get_posts_by_tag(tag):
        """Get all posts with a specific tag."""
        return [post for post in PostRepository.get_posts() if tag in post['tags']]

    @staticmethod
    def get_all_tags():
        """Get a unique set of all tags used in posts."""
        tags = set()
        for post in PostRepository.get_posts():
            tags.update(post['tags'])
        return sorted(tags)

    @staticmethod
    def get_tag_counts():
        """Get count of posts for each tag."""
        tag_counts = {}
        for post in PostRepository.get_posts():
            for tag in post['tags']:
                decoded_tag = unquote(tag)
                tag_counts[decoded_tag] = tag_counts.get(decoded_tag, 0) + 1
        return tag_counts

class PostView:
    """View class to generate HTML components for posts and tags"""

    @staticmethod
    def render_post_card(post):
        """Generate a post card for listings."""
        tags = [
            A(
                Lucide("tag", size="12"),
                f"{tag}",
                href=f"/tags/{tag}",
                cls="flex items-center gap-1.5 text-sm px-2 py-1 bg-slate-100 rounded-full text-slate-700 hover:bg-slate-200 transition-colors"
            ) for tag in post['tags']
        ]

        date_str = post.get('date', '').strftime('%Y-%m-%d') if post.get('date') else ''
        read_time = post.get('read_time', 0)

        return Li(
            Div(
                Div(
                    Span(date_str, cls="text-base font-medium text-slate-500"),
                    Span("•", cls="mx-2 text-slate-400") if date_str else "",
                    Span(f"{read_time} min read", cls="text-slate-500"),
                    cls="flex items-center mb-3"
                ),
                A(
                    post['title'],
                    href=f"/posts/{post['slug']}",
                    cls="text-2xl font-bold text-slate-800 hover:text-slate-600 transition-colors no-underline mb-3 block"
                ),
                P(post['excerpt'], cls="text-slate-600 leading-relaxed mb-4"),
                Div(*tags, cls="flex flex-wrap gap-2"),
                cls="hover:bg-slate-50 transition-colors p-6 rounded-xl"
            ),
            cls="mb-8 border-b border-slate-100 pb-8 last:border-0"
        )

    @staticmethod
    def render_tag_chip(tag, count=None):
        """Generate a tag chip for the tags page."""
        tag_text = f"{tag} ({count})" if count is not None else tag
        return Li(
            A(
                tag_text,
                href=f"/tags/{quote(tag)}",
                cls="inline-flex items-center px-4 py-2 bg-slate-100 rounded-full text-slate-700 hover:bg-slate-200 transition-colors"
            )
        )

    @staticmethod
    def render_related_posts(current_slug, max_posts=3):
        """Generate a section of related posts based on shared tags."""
        current_post = PostRepository.get_post_by_slug(current_slug)
        if not current_post or not current_post.get('tags'):
            return ""

        # Find posts that share tags with current post
        current_tags = set(current_post['tags'])
        related_posts = []

        for post in PostRepository.get_posts():
            if post['slug'] == current_slug:
                continue

            shared_tags = len(set(post.get('tags', [])) & current_tags)
            if shared_tags > 0:
                related_posts.append((post, shared_tags))

        # Sort by number of shared tags and limit
        related_posts.sort(key=lambda x: x[1], reverse=True)
        related_posts = related_posts[:max_posts]

        if not related_posts:
            return ""

        # Create related posts section
        related_items = []
        for post, _ in related_posts:
            date_str = post.get('date', '').strftime('%Y-%m-%d') if post.get('date') else ''
            related_items.append(
                Li(
                    A(
                        Div(
                            P(date_str, cls="text-sm text-slate-500 mb-1"),
                            P(post['title'], cls="font-semibold text-slate-800 hover:text-slate-600"),
                        ),
                        href=f"/posts/{post['slug']}",
                        cls="block p-4 hover:bg-slate-50 rounded-lg transition-colors"
                    )
                )
            )

        return Div(
            H3("Related Posts", cls="text-xl font-bold mb-4"),
            Ul(*related_items, cls="divide-y divide-slate-100"),
            cls="mt-12 pt-8 border-t border-slate-100"
        )

# Page generator functions that use the repository and view classes
def get_blog_index(current_path=None):
    """Generate the main blog index page."""
    posts = PostRepository.get_posts()

    if not posts:
        empty_state = Div(
            Lucide("file-text", size="48", cls="text-slate-300 mb-4"),
            H2("No Posts Yet", cls="text-2xl font-bold text-slate-700 mb-2"),
            P("Check back soon for new content.", cls="text-slate-500"),
            cls="text-center py-16"
        )
        return root_layout(empty_state, current_path)

    post_items = [PostView.render_post_card(post) for post in posts]

    header = Div(
        H1("All Posts", cls="text-3xl font-bold text-slate-800 mb-2"),
        P(f"{len(posts)} article{'' if len(posts) == 1 else 's'}", cls="text-slate-500"),
        cls="mb-8 pb-4 border-b border-slate-200"
    )

    content = Div(
        header,
        Ul(*post_items, cls="divide-y divide-slate-100"),
        cls="w-full"
    )

    return root_layout(content, current_path if current_path else "/")

def get_post(slug, current_path=None):
    """Generate a single post page."""
    post = PostRepository.get_post_by_slug(slug)

    if not post:
        not_found = Div(
            Lucide("alert-circle", size="48", cls="text-amber-500 mb-4"),
            H1("Post Not Found", cls="text-3xl font-bold mb-4"),
            P("The post you're looking for doesn't exist or has been removed.", cls="mb-6"),
            A("Back to All Posts", href="/posts", cls="bg-slate-800 hover:bg-slate-700 text-white py-2 px-4 rounded"),
            cls="text-center py-16"
        )
        return root_layout(Titled("Post not found", not_found), current_path)

        tags = [
                A(
                    Lucide("tag", size="15"),
                    f"{tag}",
                    href=f"/tags/{tag}",
                    cls="flex items-center gap-1.5 px-3 py-1.5 bg-slate-100 rounded-full text-slate-700 hover:bg-slate-200 transition-colors"
                ) for tag in post['tags']
            ]

        date_str = post.get('date', '').strftime('%Y-%m-%d') if post.get('date') else ''
        read_time = post.get('read_time', 0)

        # Post header with metadata
        header = Div(
                H1(post['title'], cls="text-3xl md:text-4xl font-bold mb-4 text-slate-800"),
                Div(
                    Span(date_str, cls="text-base font-medium text-slate-500"),
                    Span("•", cls="mx-2 text-slate-400") if date_str else "",
                    Span(f"{read_time} min read", cls="text-slate-500"),
                    cls="flex items-center mb-8"
                ),
                cls="mb-8 pb-4 border-b border-slate-100"
            )

        # Post content
        content = Div(
                header,
                Div(post.content, cls="marked prose prose-slate max-w-none"),
                Div(
                    P("Tags", cls="text-sm text-slate-500 mb-3"),
                    Div(*tags, cls="flex flex-wrap gap-2 mb-8"),
                    cls="mt-12 pt-8 border-t border-slate-100"
                ),
                PostView.render_related_posts(slug),
                cls="w-full"
            )

        return root_layout(Titled(post['title'], content), currepath)

    tags = [
        A(
            Lucide("tag", size="15"),
            f"{tag}",
            href=f"/tags/{tag}",
            cls="flex items-center gap-1.5 px-3 py-1.5 bg-slate-100 rounded-full text-slate-700 hover:bg-slate-200 transition-colors"
        ) for tag in post['tags']
    ]

    date_str = post.get('date', '').strftime('%Y-%m-%d') if post.get('date') else ''
    read_time = post.get('read_time', 0)

    # Post header with metadata
    header = Div(
        H1(post['title'], cls="text-3xl md:text-4xl font-bold mb-4 text-slate-800"),
        Div(
            Span(date_str, cls="text-base font-medium text-slate-500"),
            Span("•", cls="mx-2 text-slate-400") if date_str else "",
            Span(f"{read_time} min read", cls="text-slate-500"),
            cls="flex items-center mb-8"
        ),
        cls="mb-8 pb-4 border-b border-slate-100"
    )

    # Post content
    content = Div(
        header,
        Div(post.content, cls="marked prose prose-slate max-w-none"),
        Div(
            P("Tags", cls="text-sm text-slate-500 mb-3"),
            Div(*tags, cls="flex flex-wrap gap-2 mb-8"),
            cls="mt-12 pt-8 border-t border-slate-100"
        ),
        PostView.render_related_posts(slug),
        cls="w-full"
    )

    return root_layout(content, current_path)

def get_posts_by_tag(tag, current_path=None):
    """Generate a page showing all posts with a specific tag."""
    tag = unquote(tag)
    tagged_posts = PostRepository.get_posts_by_tag(tag)

    if not tagged_posts:
        empty_state = Div(
            Lucide("tag-off", size="48", cls="text-slate-300 mb-4"),
            H2(f"No Posts Tagged '{tag}'", cls="text-2xl font-bold text-slate-700 mb-2"),
            P("This tag has no posts yet, or it may have been removed.", cls="text-slate-500 mb-6"),
            A("View All Tags", href="/tags", cls="text-slate-600 hover:text-slate-800"),
            cls="text-center py-16"
        )
        return root_layout(Titled(f"Tag: {tag}", empty_state), current_path )

    post_items = [PostView.render_post_card(post) for post in tagged_posts]

    header = Div(
        H1(f"Posts tagged with '{tag}'", cls="text-3xl font-bold text-slate-800 mb-2"),
        P(f"{len(tagged_posts)} post{'' if len(tagged_posts) == 1 else 's'}", cls="text-slate-500"),
        cls="mb-8 pb-4 border-b border-slate-200"
    )

    content = Div(
        header,
        Ul(*post_items, cls="divide-y divide-slate-100"),
        cls="w-full"
    )

    return root_layout(Titled(f"Tag: {tag}", content), current_path )

def get_tag_list(current_path=None):
    """Generate a page listing all tags."""
    tags = PostRepository.get_all_tags()
    tag_counts = PostRepository.get_tag_counts()

    if not tags:
        empty_state = Div(
            Lucide("tags", size="48", cls="text-slate-300 mb-4"),
            H2("No Tags Yet", cls="text-2xl font-bold text-slate-700 mb-2"),
            P("Tags will appear here once posts are added.", cls="text-slate-500 mb-6"),
            A("View All Posts", href="/posts", cls="text-slate-600 hover:text-slate-800"),
            cls="text-center py-16"
        )
        return root_layout(Titled("Tags", empty_state), current_path)

    tag_items = [PostView.render_tag_chip(tag, tag_counts.get(tag, 0)) for tag in tags]

    # Group tags by first letter for better organization
    alphabet = {}
    for tag in tags:
        first_letter = tag[0].upper()
        if first_letter not in alphabet:
            alphabet[first_letter] = []
        alphabet[first_letter].append(tag)

    # Create alphabetical sections
    sections = []
    for letter, letter_tags in sorted(alphabet.items()):
        tag_chips = [PostView.render_tag_chip(tag, tag_counts.get(tag, 0)) for tag in sorted(letter_tags)]
        sections.append(
            Div(
                H2(letter, cls="text-2xl font-bold text-slate-800 mb-4"),
                Ul(*tag_chips, cls="flex flex-wrap gap-3 list-none mb-8"),
                cls="mb-8"
            )
        )

    content = Div(
        H1("All Tags", cls="text-3xl font-bold text-slate-800 mb-8"),
        *sections,
        cls="w-full"
    )

    return root_layout(Titled("Tags", content), current_path)

# For backward compatibility with existing code
def get_posts():
    return PostRepository.get_posts()

def get_all_tags():
    return PostRepository.get_all_tags()
