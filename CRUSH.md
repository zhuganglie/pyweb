# Crush - project-specific norms and conventions

This file contains norms and conventions for this project. When you make changes to this codebase, you should follow these norms.

## Commands

- To run the app: `python main.py`
- To install dependencies: `pip install -r requirements.txt`
- To lint: `ruff check .`
- To format: `ruff format .`

## File-specific guidance

- New pages should be added to `main.py`. 
- The home page is in `home.py`. Other pages are in their own files, e.g. `about.py`, `blog.py`.
- Static assets are in `public/`.
- Blog posts are in `posts/` as markdown files with frontmatter.
- `sitemap.py` generates the sitemap and should be run after adding new pages.
- The `memory-bank` directory is for notes and should not be modified.

## Code style

- **Formatting**: Use `ruff format .` to format code.
- **Linting**: Use `ruff check .` to lint code.
- **Imports**: Use `isort` conventions for sorting imports. The main `fasthtml` import is `from fasthtml.common import *`. Other imports are from `fasthtml.components`, `fasthtml.core`, `fasthtml.js`, `fasthtml.svg`, and `fasthtml.xtend`.
- **Pages**: Should be defined as functions that return `fasthtml` components.
- **Testing**: There are no automated tests in this project. Please test your changes manually.
