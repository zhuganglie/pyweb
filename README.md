# FastHTML Blog

This project is a simple blog built using the `fasthtml` library. It allows you to create and display blog posts, organize them by tags, and includes an "About" page.

## Features

- **Blog Posts:** Display a list of blog posts with titles and summaries
- **Post Details:** View individual blog posts with their full content
- **Tagging:** Organize posts by tags and view posts associated with specific tags
- **Tag List:** Display a list of all available tags
- **About Page:** Provide information about the blog or author
- **SEO Optimized:** Includes sitemap.xml generation and social media cards


## Structure

The project consists of the following main components:

- `main.py`: The main application file that defines routes and handles requests
- `blog.py`: Contains functions for retrieving and displaying blog posts and tags
- `about.py`: Contains functions for displaying the "About" page
- `home.py`: Manages the home page functionality
- `layout.py`: Defines the common layout and structure for all pages
- `posts/`: Directory containing blog posts in Markdown format
- `public/`: Static assets including images and stylesheets

## Dependencies

The project requires the following Python packages:

- `python-fasthtml`: Core web framework
- `markdown`: Markdown processing
- `python-frontmatter`: For parsing front matter in Markdown files
- `pyyaml`: YAML processing
- `pytz`: Timezone handling
- `lucide-fasthtml`: Icons integration

Additionally, the following libraries are loaded via CDN:

- `tailwindcss`: Utility-first CSS framework
- `marked.js`: JavaScript Markdown parser
- `highlight.js`: Code syntax highlighting

## Running the Application

To install dependencies:

```bash
pip install -r requirements.txt
```

To run the application:

```bash
python main.py
```

This will start the development server with live reload enabled. The blog will be accessible in your web browser at `http://localhost:8000` (default FastHTML port).
