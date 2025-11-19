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
            truncated_excerpt = excerpt[:max_length]
            # Try to break at the last space
            last_space_index = truncated_excerpt.rfind(' ')
            if last_space_index != -1:
                # If a space is found, truncate there
                excerpt = truncated_excerpt[:last_space_index] + '...'
            else:
                # If no space is found (e.g. very long word), just cut and add ellipsis
                excerpt = truncated_excerpt + '...'
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
        error_messages = []
        
        # Check posts directory
        if not os.path.exists(POSTS_DIR):
            error_messages.append(f"Posts directory '{POSTS_DIR}' does not exist")
            return posts

        # Check directory permissions
        if not os.access(POSTS_DIR, os.R_OK):
            error_messages.append(f"Cannot read from posts directory '{POSTS_DIR}': Permission denied")
            return posts

        for filename in os.listdir(POSTS_DIR):
            if not filename.endswith(".md"):
                continue

            filepath = os.path.join(POSTS_DIR, filename)
            try:
                if not os.access(filepath, os.R_OK):
                    error_messages.append(f"Cannot read file '{filename}': Permission denied")
                    continue

                with open(filepath, 'r', encoding='utf-8') as f:
                    try:
                        try:
                            post = frontmatter.load(f)
                            print(f"Successfully loaded post: {filename}")
                        except Exception as e:
                            print(f"Error parsing frontmatter in {filename}: {str(e)}")
                            raise
                    except Exception as e:
                        error_messages.append(f"Invalid frontmatter in '{filename}': {str(e)}")
                        continue

                    # Process post metadata
                    post['slug'] = filename[:-3]
                    post['tags'] = post.get('tags', [])

                    # Handle date parsing
                    date = post.get('date', None)
                    if date:
                        try:
                            post['date'] = datetime.fromisoformat(str(date))
                        except (ValueError, TypeError) as e:
                            error_messages.append(f"Invalid date format in '{filename}': {str(e)}")
                            post['date'] = datetime.min

                    # Skip draft posts
                    if post.get('draft') == True:
                        continue

                    # Add computed fields
                    try:
                        post['excerpt'] = post.get('excerpt') or PostMetrics.generate_excerpt(post.content)
                        post['read_time'] = PostMetrics.calculate_read_time(post.content)
                    except Exception as e:
                        error_messages.append(f"Error computing post metrics for '{filename}': {str(e)}")
                        continue

                    posts.append(post)
            except Exception as e:
                error_messages.append(f"Error processing '{filename}': {str(e)}")

        # Log all errors if any occurred
        if error_messages:
            print("\nPost loading errors:")
            for error in error_messages:
                print(f"- {error}")

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
    @lru_cache(maxsize=1)
    def get_all_tags():
        """Get a unique set of all tags used in posts."""
        tags = set()
        for post in PostRepository.get_posts():
            tags.update(post['tags'])
        return sorted(tags)

    @staticmethod
    @lru_cache(maxsize=1)
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
                f"#{tag}",
                href=f"/tags/{tag}",
                cls="text-sm font-medium text-primary-600 dark:text-primary-400 hover:text-primary-700 dark:hover:text-primary-300 transition-colors mr-3"
            ) for tag in post['tags']
        ]

        date_str = post.get('date', '').strftime('%B %d, %Y') if post.get('date') else ''
        read_time = post.get('read_time', 0)

        return Li(
            Article(
                Div(
                    Div(
                        Span(date_str, cls="text-sm font-medium text-slate-500 dark:text-slate-400"),
                        Span("•", cls="mx-2 text-slate-300 dark:text-slate-600"),
                        Span(f"{read_time} min read", cls="text-sm font-medium text-slate-500 dark:text-slate-400"),
                        cls="flex items-center mb-3"
                    ),
                    A(
                        H2(post['title'], cls="text-2xl font-bold text-slate-900 dark:text-white mb-3 group-hover:text-primary-600 dark:group-hover:text-primary-400 transition-colors leading-tight"),
                        href=f"/posts/{post['slug']}",
                        cls="no-underline block"
                    ),
                    P(post['excerpt'], cls="text-slate-600 dark:text-slate-300 leading-relaxed mb-4 line-clamp-3"),
                    Div(*tags, cls="flex flex-wrap mt-auto"),
                    cls="flex flex-col h-full p-8"
                ),
                cls="h-full bg-white dark:bg-slate-800 rounded-2xl shadow-sm hover:shadow-xl border border-slate-100 dark:border-slate-700 transition-all duration-300 group hover:-translate-y-1"
            ),
            cls="h-full"
        )

    @staticmethod
    def render_tag_chip(tag, count=None):
        """Generate a tag chip for the tags page."""
        tag_text = f"{tag}"
        count_badge = Span(str(count), cls="ml-2 px-2 py-0.5 text-xs font-bold bg-white dark:bg-slate-800 text-primary-600 dark:text-primary-400 rounded-full") if count is not None else ""
        
        return Li(
            A(
                Span(tag_text),
                count_badge,
                href=f"/tags/{quote(tag)}",
                cls="inline-flex items-center px-5 py-3 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl text-slate-700 dark:text-slate-300 hover:border-primary-500 dark:hover:border-primary-500 hover:text-primary-600 dark:hover:text-primary-400 hover:shadow-md transition-all duration-300 group"
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
            date_str = post.get('date', '').strftime('%B %d, %Y') if post.get('date') else ''
            related_items.append(
                Li(
                    A(
                        Div(
                            P(date_str, cls="text-xs font-medium text-slate-500 dark:text-slate-400 mb-2 uppercase tracking-wider"),
                            H4(post['title'], cls="text-lg font-bold text-slate-900 dark:text-white group-hover:text-primary-600 dark:group-hover:text-primary-400 transition-colors leading-snug"),
                            cls="p-6 h-full flex flex-col"
                        ),
                        href=f"/posts/{post['slug']}",
                        cls="block h-full bg-white dark:bg-slate-800 rounded-xl border border-slate-100 dark:border-slate-700 hover:border-primary-200 dark:hover:border-primary-800 hover:shadow-lg transition-all duration-300 group"
                    ),
                    cls="h-full"
                )
            )

        return Section(
            H3("Read Next", cls="text-2xl font-bold mb-8 text-slate-900 dark:text-white"),
            Ul(*related_items, cls="grid grid-cols-1 md:grid-cols-3 gap-6"),
            cls="mt-24 pt-16 border-t border-slate-200 dark:border-slate-800"
        )

# Page generator functions that use the repository and view classes
def get_blog_index(current_path=None, page: int = 1):
    """Generate the main blog index page with pagination."""
    all_posts = PostRepository.get_posts()
    
    # Pagination settings
    posts_per_page = 9  # Changed to 9 for 3x3 grid
    total_posts = len(all_posts)
    total_pages = math.ceil(total_posts / posts_per_page)
    
    # Ensure valid page number
    if page < 1: page = 1
    if page > total_pages: page = total_pages
    
    # Slice posts for current page
    start_idx = (page - 1) * posts_per_page
    end_idx = start_idx + posts_per_page
    current_posts = all_posts[start_idx:end_idx]

    if not current_posts:
        empty_state = Div(
            Lucide("file-text", size="48", cls="text-slate-300 dark:text-slate-600 mb-4 transition-colors"),
            H2("No Posts Yet", cls="text-2xl font-bold text-slate-700 dark:text-slate-300 mb-2 transition-colors"),
            P("Check back soon for new content.", cls="text-slate-500 dark:text-slate-400 transition-colors"),
            cls="text-center py-24"
        )
        return root_layout(empty_state, current_path)

    post_items = [PostView.render_post_card(post) for post in current_posts]

    header = Div(
        H1("All Articles", cls="text-4xl md:text-5xl font-extrabold text-slate-900 dark:text-white mb-4 tracking-tight"),
        P(f"Exploring {total_posts} article{'' if total_posts == 1 else 's'} on political science and society.", cls="text-xl text-slate-600 dark:text-slate-400"),
        cls="mb-16 text-center max-w-3xl mx-auto"
    )

    # Pagination Controls
    pagination_controls = []
    if total_pages > 1:
        if page > 1:
            pagination_controls.append(
                A("← Previous", href=f"/posts?page={page-1}",
                  cls="px-6 py-3 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-full hover:border-primary-500 dark:hover:border-primary-500 text-slate-600 dark:text-slate-300 font-medium transition-all hover:-translate-y-0.5 shadow-sm hover:shadow-md")
            )

        pagination_controls.append(
            Span(f"Page {page} of {total_pages}", cls="text-slate-500 dark:text-slate-400 font-medium")
        )

        if page < total_pages:
            pagination_controls.append(
                A("Next →", href=f"/posts?page={page+1}",
                  cls="px-6 py-3 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-full hover:border-primary-500 dark:hover:border-primary-500 text-slate-600 dark:text-slate-300 font-medium transition-all hover:-translate-y-0.5 shadow-sm hover:shadow-md")
            )

    content = Div(
        header,
        Ul(*post_items, cls="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"),
        Div(*pagination_controls, cls="flex justify-center items-center gap-6 mt-16 pt-12 border-t border-slate-200 dark:border-slate-800") if pagination_controls else "",
        cls="w-full max-w-7xl mx-auto"
    )

    return root_layout(Titled("Blog", content), current_path if current_path else "/")

def get_post(slug, current_path=None):
    """Generate a single post page."""
    post = PostRepository.get_post_by_slug(slug)

    if not post:
        not_found = Div(
            Lucide("alert-circle", size="48", cls="text-amber-500 dark:text-amber-400 mb-4 transition-colors"),
            H1("Post Not Found", cls="text-3xl font-bold mb-4 dark:text-slate-100 transition-colors"),
            P("The post you're looking for doesn't exist or has been removed.", cls="mb-6 dark:text-slate-300 transition-colors"),
            A("Back to All Posts", href="/posts", cls="bg-slate-800 dark:bg-slate-700 hover:bg-slate-700 dark:hover:bg-slate-600 text-white py-2 px-4 rounded focus:outline-none focus:ring-2 focus:ring-indigo-500 transition-colors"),
            cls="text-center py-16"
        )
        return root_layout(Titled("Post not found", not_found), current_path)

    tags = [
        A(
            f"#{tag}",
            href=f"/tags/{tag}",
            cls="text-sm font-medium text-primary-600 dark:text-primary-400 hover:text-primary-700 dark:hover:text-primary-300 transition-colors mr-4"
        ) for tag in post['tags']
    ]

    date_str = post.get('date', '').strftime('%B %d, %Y') if post.get('date') else ''
    read_time = post.get('read_time', 0)

    # Post header with metadata
    header = Div(
        Div(
            Span(date_str, cls="font-medium"),
            Span("•", cls="mx-2 opacity-50"),
            Span(f"{read_time} min read", cls="font-medium"),
            cls="flex items-center justify-center text-slate-500 dark:text-slate-400 mb-6 uppercase tracking-wider text-sm"
        ),
        H1(post['title'], cls="text-4xl md:text-5xl lg:text-6xl font-extrabold mb-6 text-slate-900 dark:text-white leading-tight text-center"),
        P(post['subtitle'], cls="text-xl md:text-2xl text-slate-600 dark:text-slate-300 mb-8 text-center leading-relaxed max-w-3xl mx-auto") if post.get('subtitle') else "",
        Div(*tags, cls="flex flex-wrap justify-center mb-12"),
        cls="mb-12 pb-12 border-b border-slate-200 dark:border-slate-800"
    )

    # Post content
    content = Div(
        header,
        Div(post.content, cls="marked prose prose-lg prose-slate dark:prose-invert max-w-3xl mx-auto"),
        PostView.render_related_posts(slug),
        Div(
            P("Share this article:", cls="text-sm font-bold text-slate-900 dark:text-white mb-4 uppercase tracking-wider"),
            Div(
                A(Lucide("twitter", size="20"), href=f"https://twitter.com/intent/tweet?text={quote(post['title'])}&url={quote(f'https://yzc.vercel.app/posts/{slug}')}", target="_blank", cls="p-3 bg-slate-100 dark:bg-slate-800 rounded-full hover:bg-blue-50 dark:hover:bg-blue-900/30 hover:text-blue-500 dark:hover:text-blue-400 transition-colors", **{"aria-label": "Share on Twitter"}),
                A(Lucide("linkedin", size="20"), href=f"https://www.linkedin.com/sharing/share-offsite/?url={quote(f'https://yzc.vercel.app/posts/{slug}')}", target="_blank", cls="p-3 bg-slate-100 dark:bg-slate-800 rounded-full hover:bg-blue-50 dark:hover:bg-blue-900/30 hover:text-blue-700 dark:hover:text-blue-400 transition-colors", **{"aria-label": "Share on LinkedIn"}),
                A(Lucide("mail", size="20"), href=f"mailto:?subject={quote(post['title'])}&body={quote(f'Check out this article: https://yzc.vercel.app/posts/{slug}')}", cls="p-3 bg-slate-100 dark:bg-slate-800 rounded-full hover:bg-slate-200 dark:hover:bg-slate-700 transition-colors", **{"aria-label": "Share via Email"}),
                cls="flex gap-4"
            ),
            cls="mt-16 pt-8 border-t border-slate-200 dark:border-slate-800 flex flex-col items-center"
        ),
        cls="w-full"
    )

    return root_layout(content, current_path)

def get_posts_by_tag(tag, current_path=None):
    """Generate a page showing all posts with a specific tag."""
    tag = unquote(tag)
    tagged_posts = PostRepository.get_posts_by_tag(tag)

    if not tagged_posts:
        empty_state = Div(
            Lucide("tag", size="48", cls="text-slate-300 dark:text-slate-600 mb-4 transition-colors"),
            H2(f"No Posts Tagged '{tag}'", cls="text-2xl font-bold text-slate-700 dark:text-slate-300 mb-2 transition-colors"),
            P("This tag has no posts yet, or it may have been removed.", cls="text-slate-500 dark:text-slate-400 mb-6 transition-colors"),
            A("View All Tags", href="/tags", cls="text-primary-600 dark:text-primary-400 hover:text-primary-700 dark:hover:text-primary-300 font-medium transition-colors"),
            cls="text-center py-24"
        )
        return root_layout(Titled(f"Tag: {tag}", empty_state), current_path )

    post_items = [PostView.render_post_card(post) for post in tagged_posts]

    header = Div(
        Span("Tag", cls="inline-block py-1 px-3 rounded-full bg-primary-100 dark:bg-primary-900/30 text-primary-700 dark:text-primary-300 text-sm font-semibold mb-4 tracking-wide uppercase"),
        H1(f"#{tag}", cls="text-4xl md:text-5xl font-extrabold text-slate-900 dark:text-white mb-4 tracking-tight"),
        P(f"{len(tagged_posts)} article{'' if len(tagged_posts) == 1 else 's'} found", cls="text-xl text-slate-600 dark:text-slate-400"),
        cls="mb-16 text-center"
    )

    content = Div(
        header,
        Ul(*post_items, cls="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"),
        cls="w-full max-w-7xl mx-auto"
    )

    return root_layout(Titled(f"Tag: {tag}", content), current_path )

def get_tag_list(current_path=None):
    """Generate a page listing all tags."""
    tags = PostRepository.get_all_tags()
    tag_counts = PostRepository.get_tag_counts()

    if not tags:
        empty_state = Div(
            Lucide("tags", size="48", cls="text-slate-300 dark:text-slate-600 mb-4 transition-colors"),
            H2("No Tags Yet", cls="text-2xl font-bold text-slate-700 dark:text-slate-300 mb-2 transition-colors"),
            P("Tags will appear here once posts are added.", cls="text-slate-500 dark:text-slate-400 mb-6 transition-colors"),
            A("View All Posts", href="/posts", cls="text-primary-600 dark:text-primary-400 hover:text-primary-700 dark:hover:text-primary-300 font-medium transition-colors"),
            cls="text-center py-24"
        )
        return root_layout(Titled("Tags", empty_state), current_path)

    tag_items = [PostView.render_tag_chip(tag, tag_counts.get(tag, 0)) for tag in sorted(tags)]

    content = Div(
        Div(
            H1("Explore Topics", cls="text-4xl md:text-5xl font-extrabold text-slate-900 dark:text-white mb-4 tracking-tight"),
            P("Browse articles by subject matter.", cls="text-xl text-slate-600 dark:text-slate-400"),
            cls="mb-16 text-center"
        ),
        Ul(*tag_items, cls="flex flex-wrap justify-center gap-4 list-none max-w-4xl mx-auto"),
        cls="w-full"
    )
    return root_layout(Titled("Tags", content), current_path)

def get_posts():
    """Get all posts, exposed at module level."""
    return PostRepository.get_posts()

def get_all_tags():
    """Get all tags, exposed at module level."""
    return PostRepository.get_all_tags()


