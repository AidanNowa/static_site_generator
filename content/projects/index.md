# Projects

A collection of personal and academic projects spanning data engineering, robotics, machine learning, and systems programming.

## Fantasy Football Analytics

A terminal-based analytics dashboard for Yahoo Fantasy Football, built to give dynasty league managers deeper insight into weekly player performance than the default Yahoo interface provides. The dashboard pulls live data from the Yahoo Fantasy API, renders interactive bar charts comparing actual points vs. projections, and lets you filter by position group to evaluate matchups. Built with Python, Textual, plotext, and pandas — my first end-to-end personal project connecting an external API to a fully interactive terminal UI.

[View project](/projects/fantasy_football/) | [GitHub](https://github.com/AidanNowa/fantasy_football_analytics)

## TAGBOT — Autonomous Tag-Playing Robot

An autonomous robot that plays the game of tag with real people outdoors, built for EC545 (Embedded and Real-Time Systems) at Boston University. Running on a Yahboom ROSMASTER X3 (Jetson Nano, RGB-D camera, 2D LiDAR), TAGBOT uses a custom ROS color detection node to find targets and a finite state machine controller with three states — Search, Chase, and Avoid — to navigate, close distance, and steer clear of obstacles. Color-based detection outperformed YOLO-style detectors at ground level. Formally verified with UPPAAL. Built with ROS1, Python, and C++.

[View project](/projects/tagbot/) | [GitHub](https://github.com/AidanNowa/EC545_TAGBOT)

## RAG CLI

A command-line retrieval-augmented generation tool that grounds a language model's answers in a specific document corpus rather than its training data. Point it at a set of documents, query them conversationally, and get answers backed by retrieved context instead of hallucinated memory. Building this from scratch to understand the full RAG pipeline: chunking strategies, embedding models, vector similarity search, prompt construction, and context window management. Actively in development in Python.

[View project](/projects/RAG/) | [GitHub](https://github.com/AidanNowa/RAG)

## Static Site Generator

A custom Markdown-to-HTML static site generator written in Python with no external dependencies — and the engine powering this website. It handles full Markdown parsing (headings, bold, italic, inline code, code blocks, blockquotes, lists, links, images), recursive directory traversal, static asset copying, and configurable base path deployment for GitHub Pages. The parser converts Markdown into a tree of custom HTMLNode objects and walks the tree to produce the final markup. Built as part of the Boot.dev curriculum, with several bugs tracked down and fixed along the way.

[View project](/projects/static_site_generator/) | [GitHub](https://github.com/AidanNowa/static_site_generator)
