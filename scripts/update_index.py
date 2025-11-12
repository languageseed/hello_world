#!/usr/bin/env python3
"""
Index Updater for Hello World Blog
Helps you add new posts to the index.html file
"""

import os
import re
from datetime import datetime

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
    if not os.path.exists('posts'):
        print("No posts directory found!")
        return
    
    posts = [f for f in os.listdir('posts') if f.endswith('.html')]
    
    if not posts:
        print("No posts found!")
        return
    
    print("\n📝 Post Cards HTML (copy to index.html):\n")
    print("<!-- Replace the posts-grid content with this -->\n")
    
    for post in sorted(posts, reverse=True):  # Newest first
        info = extract_post_info(f'posts/{post}')
        card = generate_post_card(post, info)
        print(card)
        print()

def main():
    """Main function"""
    print("🌱 Hello World Blog - Index Updater\n")
    print("This tool helps you manage posts in your index.html\n")
    
    while True:
        print("\nOptions:")
        print("1. List all posts")
        print("2. Generate cards for all posts")
        print("3. Exit")
        
        choice = input("\nChoose an option (1-3): ").strip()
        
        if choice == '1':
            list_posts()
        elif choice == '2':
            generate_all_cards()
        elif choice == '3':
            print("\nGoodbye! 👋")
            break
        else:
            print("\nInvalid option. Please choose 1-3.")

if __name__ == '__main__':
    main()

