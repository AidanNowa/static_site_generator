# Static Site Generator

A custom static site generator written in Python — and the engine powering this website.

## What It Does

Takes a directory of Markdown files and a single HTML template and produces a complete static site. It handles:

- Full Markdown parsing: headings, bold, italic, inline code, code blocks, blockquotes, ordered and unordered lists, links, and images
- Recursive directory traversal — drop a Markdown file anywhere in the content tree and it generates the corresponding HTML page
- Static asset copying (CSS, images) from a source directory to the output
- Configurable base path for deployment to subdirectory URLs (e.g. GitHub Pages)

## How It Works

The parser converts Markdown text into a tree of custom `HTMLNode` objects (`LeafNode` for inline elements, `ParentNode` for block-level containers), then walks the tree calling `.to_html()` to produce the final markup. Each Markdown block type — paragraph, heading, code, quote, list — has its own conversion function.

## Tech Stack

- **Python** — everything, no dependencies
- Shell scripts for building and running a local dev server

## What I Learned

This project was part of the Boot.dev curriculum and gave me a solid grounding in recursive tree structures, parsing strategies, and the value of a thorough test suite. I also tracked down and fixed several bugs in the process — including a regex that incorrectly matched image syntax as links, and void HTML tags (`img`, `br`) being rendered with closing tags.

[View on GitHub](https://github.com/AidanNowa/static_site_generator)

[Back to Home](/)
