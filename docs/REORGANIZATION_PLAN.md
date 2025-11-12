# 🗂️ Repository Reorganization Plan

## Current Structure (Messy)
```
Root/
├── 2025-11-12-getting-started.md    ← Post source
├── example-post.md                   ← Post source
├── test-mermaid.md                   ← Post source
├── README.md                         ← Doc
├── DEPLOYMENT.md                     ← Doc
├── QUICK_START.md                    ← Doc
├── POST_WORKFLOW.md                  ← Doc
├── generate_post.py                  ← Script
├── update_index.py                   ← Script
├── template.html                     ← Template
├── index.html                        ← Main page
├── .gitignore                        ← Config
├── posts/                            ← Generated HTML
├── images/                           ← Media
└── assets/                           ← Assets
```

**Problems:**
- Markdown posts mixed with docs
- Scripts in root
- Hard to find things
- Looks unprofessional

## Proposed Structure (Clean)
```
Root/
├── 📄 index.html                     ← Main blog page (ROOT)
├── 📖 README.md                      ← Main readme (ROOT)
├── 🔧 .gitignore                     ← Config (ROOT)
│
├── 📝 content/                       ← All markdown posts here
│   ├── 2025-11-12-getting-started.md
│   ├── example-post.md
│   └── test-mermaid.md
│
├── 📄 posts/                         ← Generated HTML (no change)
│   ├── 2025-11-12-getting-started.html
│   ├── example-post.html
│   └── test-mermaid.html
│
├── 🖼️ images/                        ← Images (no change)
│   └── README.md
│
├── 🎨 assets/                        ← CSS, JS, other assets
│   └── (future custom files)
│
├── 🛠️ scripts/                       ← All scripts here
│   ├── generate_post.py
│   └── update_index.py
│
├── 📐 templates/                     ← Templates here
│   └── template.html
│
└── 📚 docs/                          ← All documentation
    ├── DEPLOYMENT.md
    ├── QUICK_START.md
    └── POST_WORKFLOW.md
```

**Benefits:**
- ✅ Clean root (only 3 files!)
- ✅ Logical grouping
- ✅ Easy to navigate
- ✅ Professional structure
- ✅ Scalable for growth

## Migration Steps

1. Create new directories
2. Move files to new locations
3. Update scripts to handle new paths
4. Test locally
5. Commit and push

## New Workflow After Reorganization

```bash
# Create new post in content/
nano content/2025-11-13-my-post.md

# Generate (script auto-finds it)
python scripts/generate_post.py content/2025-11-13-my-post.md

# Or from anywhere
python scripts/generate_post.py content/my-post.md

# Preview
open posts/my-post.html

# Deploy
git add .
git commit -m "Add new post"
git push origin main
```

## Files That Stay in Root
- `index.html` - Main entry point
- `README.md` - First thing people see
- `.gitignore` - Git config

Everything else goes into organized folders!

