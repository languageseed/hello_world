# 📝 Blog Post Content

This folder contains all your blog post source files in Markdown format.

## Current Posts

- `2025-11-12-getting-started.md` - Getting started guide
- `example-post.md` - Full feature demonstration
- `test-mermaid.md` - Mermaid diagram examples

## Creating a New Post

### 1. Create Markdown File Here

```bash
nano content/2025-11-13-my-new-post.md
```

### 2. Add Frontmatter

```markdown
---
title: My New Post Title
author: language seed
date: 2025-11-13
---

# My New Post

Your content here...
```

### 3. Generate HTML

From project root:
```bash
python scripts/generate_post.py content/2025-11-13-my-new-post.md
```

### 4. Push to GitHub

```bash
git add .
git commit -m "Add new post: My New Post"
git push origin main
```

## Naming Convention

**Recommended format:**
```
YYYY-MM-DD-post-slug.md
```

Examples:
- `2025-11-13-python-tips.md`
- `2025-12-01-year-review.md`
- `2026-01-15-new-project.md`

## File Structure

```markdown
---
title: Required - Post title
author: Required - Your name
date: Required - YYYY-MM-DD format
---

# Main Heading

Content with **markdown** formatting.

## Subheading

More content...
```

## Features You Can Use

- ✅ Markdown formatting
- ✅ Code blocks with syntax highlighting
- ✅ Mermaid diagrams
- ✅ Images (from `../images/` folder)
- ✅ Tables, lists, blockquotes
- ✅ Links and more!

See `example-post.md` for all features!

---

**Note:** These are SOURCE files. The generated HTML goes in the `posts/` folder.

