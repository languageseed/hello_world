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

# Get the project root directory (parent of scripts/)
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent

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

def generate_post(markdown_file, output_file=None, template_file=None):
    """Generate HTML blog post from markdown file"""
    
    # Convert to Path object and resolve
    markdown_path = Path(markdown_file)
    if not markdown_path.is_absolute():
        # Try relative to current directory first
        if markdown_path.exists():
            markdown_path = markdown_path.resolve()
        else:
            # Try relative to project root
            alt_path = PROJECT_ROOT / markdown_path
            if alt_path.exists():
                markdown_path = alt_path
            else:
                print(f"Error: Markdown file '{markdown_file}' not found")
                sys.exit(1)
    
    if not markdown_path.exists():
        print(f"Error: Markdown file '{markdown_file}' not found")
        sys.exit(1)
    
    markdown_content = read_file(markdown_path)
    
    # Extract frontmatter and content
    metadata, content = extract_frontmatter(markdown_content)
    
    # Get metadata with defaults
    title = metadata.get('title', 'Untitled Post')
    author = metadata.get('author', 'Language Seed')
    date = metadata.get('date', datetime.now().strftime('%Y-%m-%d'))
    
    # Find template file
    if template_file is None:
        template_file = PROJECT_ROOT / 'templates' / 'template.html'
    else:
        template_file = Path(template_file)
    
    if not template_file.exists():
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
        base_name = markdown_path.stem
        output_file = PROJECT_ROOT / 'posts' / f'{base_name}.html'
    else:
        output_file = Path(output_file)
        if not output_file.is_absolute():
            output_file = PROJECT_ROOT / output_file
    
    # Ensure posts directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Write output
    write_file(output_file, html)
    # Make output path relative to project root for display
    try:
        display_path = output_file.relative_to(PROJECT_ROOT)
    except ValueError:
        display_path = output_file
    
    print(f"✅ Generated: {display_path}")
    print(f"   Title: {title}")
    print(f"   Author: {author}")
    print(f"   Date: {date}")
    
    return True

def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Usage: python scripts/generate_post.py <markdown_file> [output_file]")
        print("\nExamples:")
        print("  python scripts/generate_post.py content/my-post.md")
        print("  python scripts/generate_post.py content/my-post.md posts/custom-name.html")
        print("\nFrom scripts directory:")
        print("  python generate_post.py ../content/my-post.md")
        print("\nOptions:")
        print("  --no-index    Skip auto-updating index.html")
        sys.exit(1)
    
    # Check for flags
    auto_update_index = True
    args = sys.argv[1:]
    
    if '--no-index' in args:
        auto_update_index = False
        args.remove('--no-index')
    
    markdown_file = args[0]
    output_file = args[1] if len(args) > 1 else None
    
    # Generate the post
    success = generate_post(markdown_file, output_file)
    
    if success and auto_update_index:
        # Auto-update index.html
        print("\n📋 Updating index.html...")
        import subprocess
        try:
            result = subprocess.run(
                [sys.executable, str(SCRIPT_DIR / 'update_index.py'), '--auto'],
                cwd=PROJECT_ROOT,
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print("✅ Index updated successfully!")
            else:
                print("⚠️  Index update failed (you can update manually with: python scripts/update_index.py)")
        except Exception as e:
            print(f"⚠️  Could not auto-update index: {e}")
            print("   Run manually: python scripts/update_index.py")

if __name__ == '__main__':
    main()

