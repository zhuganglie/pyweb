# FastHTML Blog

This project is a simple blog built using the `fasthtml` library. It allows you to create and display blog posts, organize them by tags, and includes an "About" page.

## Features

-   **Blog Posts:** Display a list of blog posts with titles and summaries.
-   **Post Details:** View individual blog posts with their full content.
-   **Tagging:** Organize posts by tags and view posts associated with specific tags.
-   **Tag List:** Display a list of all available tags.
-   **About Page:** Provide information about the blog or author.

## Structure

The project consists of the following main components:

-   `main.py`: The main application file that defines routes and handles requests.
-   `blog.py`: Contains functions for retrieving and displaying blog posts and tags.
-   `about.py`: Contains functions for displaying the "About" page.
-   `layout.py`: Defines the common layout and structure for all pages.

## Dependencies

The project uses the following libraries:

-   `fasthtml`: A library for building web applications with Python.
-   `tailwindcss`: A utility-first CSS framework for styling the pages.
-   `marked`: A JavaScript library for parsing Markdown content.
-   `highlight.js`: A JavaScript library for syntax highlighting code blocks.

## Running the Application

To run the application, execute the following command:

```bash

python main.py

```

This will start the development server, and you can access the blog in your web browser at `http://localhost:5001`.
