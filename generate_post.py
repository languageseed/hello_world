#!/usr/bin/env python3
"""
Blog Post Generator for Hello World Blog
Converts markdown files to HTML using the template.
"""

import os
import sys
import re
from datetime import datetime
from pathlib import Path

def read_file(filepath):
    """Read file contents"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """Write content to file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def extract_frontmatter(markdown_content):
    """
    Extract YAML-style frontmatter from markdown.
    Expected format:
    ---
    title: Your Title
    author: Author Name
    date: 2025-11-12
    ---
    """
    frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(frontmatter_pattern, markdown_content, re.DOTALL)
    
    if match:
        frontmatter_text = match.group(1)
        content = markdown_content[match.end():]
        
        # Parse frontmatter
        metadata = {}
        for line in frontmatter_text.strip().split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip()
        
        return metadata, content
    
    # No frontmatter found, use defaults
    return {}, markdown_content

def escape_markdown_for_js(content):
    """Escape markdown content for JavaScript template literal"""
    # Escape backticks and ${} template literals
    content = content.replace('\\', '\\\\')  # Escape backslashes first
    content = content.replace('`', '\\`')     # Escape backticks
    content = content.replace('${', '\\${')   # Escape template literals
    return content

def generate_post(markdown_file, output_file=None, template_file='template.html'):
    """Generate HTML blog post from markdown file"""
    
    # Read markdown file
    if not os.path.exists(markdown_file):
        print(f"Error: Markdown file '{markdown_file}' not found")
        sys.exit(1)
    
    markdown_content = read_file(markdown_file)
    
    # Extract frontmatter and content
    metadata, content = extract_frontmatter(markdown_content)
    
    # Get metadata with defaults
    title = metadata.get('title', 'Untitled Post')
    author = metadata.get('author', 'Language Seed')
    date = metadata.get('date', datetime.now().strftime('%Y-%m-%d'))
    
    # Read template
    if not os.path.exists(template_file):
        print(f"Error: Template file '{template_file}' not found")
        sys.exit(1)
    
    template = read_file(template_file)
    
    # Escape markdown content for JavaScript
    escaped_content = escape_markdown_for_js(content)
    
    # Replace placeholders
    html = template.replace('{{TITLE}}', title)
    html = html.replace('{{AUTHOR}}', author)
    html = html.replace('{{DATE}}', date)
    html = html.replace('{{CONTENT}}', escaped_content)
    
    # Determine output file
    if output_file is None:
        # Generate from markdown filename
        base_name = Path(markdown_file).stem
        output_file = f'posts/{base_name}.html'
    
    # Ensure posts directory exists
    os.makedirs('posts', exist_ok=True)
    
    # Write output
    write_file(output_file, html)
    print(f"✅ Generated: {output_file}")
    print(f"   Title: {title}")
    print(f"   Author: {author}")
    print(f"   Date: {date}")

def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Usage: python generate_post.py <markdown_file> [output_file]")
        print("\nExample:")
        print("  python generate_post.py my-post.md")
        print("  python generate_post.py my-post.md posts/custom-name.html")
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    generate_post(markdown_file, output_file)

if __name__ == '__main__':
    main()

