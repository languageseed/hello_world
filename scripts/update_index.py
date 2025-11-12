#!/usr/bin/env python3
"""
Index Updater for Hello World Blog
Automatically updates index.html with all posts from the posts/ directory
"""

import os
import re
from datetime import datetime
from pathlib import Path

# Get the project root directory
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent

def extract_post_info(html_file):
    """Extract post information from generated HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'<title>(.*?) - Hello World Blog</title>', content)
    title = title_match.group(1) if title_match else "Untitled"
    
    # Extract author
    author_match = re.search(r'By (.*?)</span>', content)
    author = author_match.group(1) if author_match else "Unknown Author"
    
    # Extract date
    date_match = re.search(r'<span class="date">(.*?)</span>', content)
    date = date_match.group(1) if date_match else datetime.now().strftime('%Y-%m-%d')
    
    # Extract first paragraph for excerpt (from markdown content)
    excerpt_match = re.search(r'const markdownContent = `.*?# .*?\n\n(.*?)\n', content, re.DOTALL)
    if excerpt_match:
        excerpt = excerpt_match.group(1).strip()
        # Clean up markdown
        excerpt = re.sub(r'\*\*(.*?)\*\*', r'\1', excerpt)  # Remove bold
        excerpt = re.sub(r'\*(.*?)\*', r'\1', excerpt)      # Remove italic
        excerpt = re.sub(r'`(.*?)`', r'\1', excerpt)        # Remove code
        # Limit length
        if len(excerpt) > 200:
            excerpt = excerpt[:200] + "..."
    else:
        excerpt = "Read this blog post to learn more."
    
    return {
        'title': title,
        'author': author,
        'date': date,
        'excerpt': excerpt
    }

def generate_post_card(filename, info):
    """Generate HTML card for a post"""
    return f'''            <div class="post-card" onclick="window.location.href='posts/{filename}'">
                <div class="post-card-header">
                    <h3>{info['title']}</h3>
                    <div class="post-card-meta">
                        By {info['author']} • {info['date']}
                    </div>
                </div>
                <div class="post-card-body">
                    <p class="post-card-excerpt">
                        {info['excerpt']}
                    </p>
                    <a href="posts/{filename}" class="post-card-link">Read More →</a>
                </div>
            </div>'''

def list_posts():
    """List all posts in the posts directory"""
    if not os.path.exists('posts'):
        print("No posts directory found!")
        return
    
    posts = [f for f in os.listdir('posts') if f.endswith('.html')]
    
    if not posts:
        print("No posts found in posts/ directory")
        return
    
    print("\n📚 Available Posts:\n")
    for i, post in enumerate(posts, 1):
        info = extract_post_info(f'posts/{post}')
        print(f"{i}. {post}")
        print(f"   Title: {info['title']}")
        print(f"   Author: {info['author']}")
        print(f"   Date: {info['date']}")
        print()

def generate_all_cards():
    """Generate HTML cards for all posts"""
    posts_dir = PROJECT_ROOT / 'posts'
    if not posts_dir.exists():
        print("No posts directory found!")
        return None
    
    posts = [f for f in os.listdir(posts_dir) if f.endswith('.html')]
    
    if not posts:
        print("No posts found!")
        return None
    
    print("\n📝 Post Cards HTML (copy to index.html):\n")
    print("<!-- Replace the posts-grid content with this -->\n")
    
    cards = []
    for post in sorted(posts, reverse=True):  # Newest first
        info = extract_post_info(posts_dir / post)
        card = generate_post_card(post, info)
        cards.append(card)
        print(card)
        print()
    
    return cards

def update_index_file(auto=False):
    """Automatically update index.html with all posts"""
    posts_dir = PROJECT_ROOT / 'posts'
    index_file = PROJECT_ROOT / 'index.html'
    
    if not posts_dir.exists():
        print("❌ Error: posts/ directory not found!")
        return False
    
    if not index_file.exists():
        print("❌ Error: index.html not found!")
        return False
    
    # Get all posts
    posts = [f for f in os.listdir(posts_dir) if f.endswith('.html')]
    
    if not posts:
        print("⚠️  No posts found in posts/ directory")
        return False
    
    # Generate cards for all posts
    cards_html = []
    for post in sorted(posts, reverse=True):  # Newest first
        info = extract_post_info(posts_dir / post)
        card = generate_post_card(post, info)
        cards_html.append(card)
    
    # Read index.html
    with open(index_file, 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    # Find the posts-grid section and replace it
    # Pattern to match the posts-grid div and its contents
    pattern = r'(<div class="posts-grid">)(.*?)(</div>\s*<div class="quick-start">)'
    
    new_posts_section = '\n' + '\n\n'.join(cards_html) + '\n\n            <!-- Auto-generated by update_index.py -->\n        '
    
    replacement = r'\1' + new_posts_section + r'\3'
    
    updated_content = re.sub(pattern, replacement, index_content, flags=re.DOTALL)
    
    if updated_content == index_content:
        print("⚠️  Warning: Could not find posts-grid section in index.html")
        return False
    
    # Write updated index.html
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    if not auto:
        print(f"✅ Updated index.html with {len(posts)} post(s)!")
        print(f"   Posts: {', '.join(posts)}")
    
    return True

def main():
    """Main function"""
    import sys
    
    # Check if running with --auto flag
    if len(sys.argv) > 1 and sys.argv[1] == '--auto':
        # Silent auto-update mode (called from generate_post.py)
        return update_index_file(auto=True)
    
    print("🌱 Hello World Blog - Index Updater\n")
    print("This tool helps you manage posts in your index.html\n")
    
    while True:
        print("\nOptions:")
        print("1. List all posts")
        print("2. Generate cards for all posts (preview)")
        print("3. Update index.html automatically")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == '1':
            list_posts()
        elif choice == '2':
            generate_all_cards()
        elif choice == '3':
            update_index_file()
        elif choice == '4':
            print("\nGoodbye! 👋")
            break
        else:
            print("\nInvalid option. Please choose 1-4.")

if __name__ == '__main__':
    main()

