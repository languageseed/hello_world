---
title: "Work Suite: Six Lightweight, AI-Friendly Productivity Tools"
author: Language Seed
date: "2025-11-27"
excerpt: "A collection of zero-dependency productivity apps that produce simple, text-based artifacts. No npm, no build tools, no databases—just open in a browser and start working."
---

# Work Suite: Six Lightweight, AI-Friendly Productivity Tools

**Try it now:** [https://languageseed.github.io/work_suite/](https://languageseed.github.io/work_suite/)

I'm excited to share [**Work Suite**](https://github.com/languageseed/work_suite), a collection of six productivity tools that I've consolidated from separate projects into one unified suite. These apps represent a different approach to productivity software—one that prioritizes simplicity, portability, and compatibility with AI assistants.

## The Problem with Traditional Tools

Modern productivity software has become increasingly complex:
- Heavy dependencies and build systems
- Proprietary binary formats (.docx, .pptx, .xlsx)
- Cloud-dependent architectures
- Formats that are difficult for AI to parse and generate

Work Suite takes a different approach: **simple text formats, zero dependencies, and complete portability**.

## The Six Apps

### 📝 Slate — Keyboard-First Notes
A fast, keyboard-driven notes app with a tile UI for power users. 100% keyboard navigable with instant search, tags, and a command palette (`⌘K`). All notes saved as JSON with plain text content.

### ✅ Done — Kanban Task Board
A Trello-style board for organizing tasks across columns. Drag-and-drop cards, color-coded labels, due dates, and 5 color themes. Save and load boards as `.done` JSON files.

### 🛤️ Journey — Timeline Creator
Create visual timelines for projects, histories, or roadmaps. Vertical and horizontal layouts with event icons. Choose from 6 visual themes and export to standalone HTML.

### 🐠 Merman — Markdown & Mermaid Viewer
A split-pane editor for Markdown documents with live diagram rendering. Full Mermaid diagram support (flowcharts, sequences, etc.) with auto-wrapping of pasted syntax. Dark and light themes available.

### 📊 Metric — Spreadsheet & Charts
A lightweight spreadsheet with formulas (`SUM`, `AVG`, `MIN`, `MAX`, `COUNT`, `ROUND`, `SQRT`, `POW`) and data visualization (bar, line, pie, doughnut charts). 50 rows × 26 columns with quick stats panel.

### 👆 Pointer — Markdown Slide Presenter
Create presentations from Markdown with 8 slide layouts (Title, Content, Two-Column, Quote, Code, Section, etc.) and 8 visual themes. Fullscreen presentation mode with keyboard navigation.

## Why This Approach Matters

**AI-Compatible Formats**  
All apps use text-based formats (JSON, Markdown, CSV) that are easy for LLMs to read and generate. This means you can ask an AI assistant to create content, then paste it directly into these tools—or export data from the tools and ask an AI to transform it.

**Zero Overhead**  
No npm, no build tools, no databases. Each app is a single HTML file you can run anywhere. Just open in a browser and start creating.

**Portable & Interoperable**  
Export to JSON, Markdown, CSV, or HTML for use anywhere. All data formats are simple, well-structured, and documented.

**Offline-First**  
Works without an internet connection after initial load. All data saves to localStorage automatically.

## Using With AI Assistants

Work Suite tools are designed to work seamlessly with AI assistants like ChatGPT, Claude, or Copilot:

**Generate Content**  
Ask an AI: "Create a 5-slide presentation about renewable energy in Markdown"  
→ Copy the AI's response and paste into **Pointer**

**Transform Data**  
Export timeline from **Journey** as JSON  
→ Send to AI: "Convert this timeline to a presentation outline"  
→ Import AI's response into **Pointer**

**Analyze & Summarize**  
Export spreadsheet from **Metric** as CSV  
→ Ask AI: "Summarize the key trends in this data"

**Bulk Create**  
Ask an AI: "Create 10 task cards for a website redesign project in JSON format"  
→ Import the structured response into **Done**

The simple text formats mean no manual reformatting—just copy and paste between your AI assistant and Work Suite.

## Technical Philosophy

| Traditional Tools | Work Suite Approach |
|------------------|---------------------|
| Complex binary formats | Simple text formats (Markdown, JSON, CSV) |
| Heavy dependencies | Single HTML files, zero setup |
| Proprietary ecosystems | Open, portable, self-contained |
| Difficult for AI to process | Easy for AI assistants to read and generate |

Each app is built with:
- **No dependencies at runtime** — all libraries loaded via CDN
- **LocalStorage persistence** — work is auto-saved in browser
- **Responsive design** — works on desktop and mobile
- **Modern CSS** — CSS variables, Grid, Flexbox
- **Vanilla JavaScript** — no frameworks, easy to understand and modify

## Getting Started

1. Visit [https://languageseed.github.io/work_suite/](https://languageseed.github.io/work_suite/)
2. Choose an app
3. Start creating

No installation. No server. No build step. Just open and work.

## File Formats

Each app uses simple, documented formats:

- **Slate:** `.slate` (JSON notes data)
- **Done:** `.done` (JSON board data)
- **Journey:** `.journey` (JSON timeline data)
- **Merman:** `.md` (Markdown)
- **Metric:** `.metric` or `.csv` (JSON/CSV)
- **Pointer:** `.pointer` (JSON presentation data)

All formats are human-readable and compatible with AI assistants for easy transformation and generation.

## Open Source

Work Suite is [open source on GitHub](https://github.com/languageseed/work_suite) under the MIT License. Use freely in personal and commercial projects. Each app is self-contained, making it easy to understand, modify, or contribute improvements.

---

> **Built on the shoulders of giants**: Work Suite uses Marked.js (Markdown parsing), Prism.js (syntax highlighting), Mermaid.js (diagram rendering), Chart.js (data visualization), and Google Fonts.

**Work Suite** — Simple tools for a complex world. 🧰

