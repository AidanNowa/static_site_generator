# Fantasy Football Analytics TUI

A terminal-based analytics dashboard for Yahoo Fantasy Football, built to give dynasty league managers deeper insight into weekly player performance than the default Yahoo interface provides.

## The Problem

In a dynasty league — where you keep your entire roster from year to year — decisions are more complex than a standard redraft. You need to evaluate players not just for this week, but for future seasons. The default Yahoo dashboard doesn't surface the data in a way that makes those decisions easy.

## What It Does

- Pulls weekly player performance and projection data from the Yahoo Fantasy API
- Renders an interactive terminal dashboard using the Textual framework
- Lets you filter by position group (QB, RB, WR, TE, K) to compare matchups
- Displays actual points scored vs. projection margins in real-time bar charts
- Supports both long and wide pandas DataFrame formats for custom data exploration

## Tech Stack

- **Python** — core logic and data transformation
- **Textual** — terminal UI framework
- **plotext** — in-terminal charting
- **pandas** — data wrangling and reshaping

## What I Learned

This was my first end-to-end personal project. I worked through connecting to an external API, structuring data transformations cleanly with pandas, and building a responsive interactive UI in the terminal — a constraint that forced creative solutions for layout and event handling.

[View on GitHub](https://github.com/AidanNowa/fantasy_football_analytics)

[Back to Home](/)
