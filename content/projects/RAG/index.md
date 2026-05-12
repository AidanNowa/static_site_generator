# RAG CLI (Work in Progress)

A command-line tool for retrieval-augmented generation (RAG) — the pattern of grounding a language model's answers in a specific document corpus rather than its training data alone.

## What It Is

RAG CLI is a Python tool that lets you point it at a set of documents and then query them conversationally. Instead of the model hallucinating answers from memory, it retrieves the most relevant chunks from your documents and uses those as context for each response.

## Why I'm Building It

RAG is one of the most practical techniques in applied ML right now — it's how most production LLM-powered tools actually work. Building one from scratch is the fastest way to understand what's happening under the hood: chunking strategies, embedding models, vector similarity search, prompt construction, and context window management.

## Stack (so far)

- **Python** — CLI interface and pipeline orchestration
- Vector embeddings and similarity search
- Local and API-backed LLM support

## Status

This is actively in development. The core retrieval pipeline is in place and the CLI interface is being built out. Follow the repo for updates.

[View on GitHub](https://github.com/AidanNowa/RAG)

[Back to Home](/)
