import matter from 'gray-matter';
import { readdirSync, readFileSync } from 'fs';
import readingTime from 'reading-time';

export interface Post {
  slug: string;
  title: string;
  author: string;
  date: string;
  excerpt?: string;
  content: string;
  readingTime?: string;
  category?: string;
  tags?: string[];
}

/**
 * Extract a clean text excerpt from markdown content.
 * Strips images, headers, blockquotes, links, and other markdown syntax.
 */
function extractExcerpt(markdown: string, maxLength: number = 160): string {
  let text = markdown
    // Remove images: ![alt](url)
    .replace(/!\[[^\]]*\]\([^)]*\)/g, '')
    // Remove links but keep text: [text](url) -> text
    .replace(/\[([^\]]*)\]\([^)]*\)/g, '$1')
    // Remove headers: # ## ### etc
    .replace(/^#{1,6}\s+/gm, '')
    // Remove blockquotes: > text
    .replace(/^>\s+/gm, '')
    // Remove bold/italic: **text** or *text* or __text__ or _text_
    .replace(/(\*\*|__)(.*?)\1/g, '$2')
    .replace(/(\*|_)(.*?)\1/g, '$2')
    // Remove inline code: `code`
    .replace(/`([^`]*)`/g, '$1')
    // Remove code blocks: ```...```
    .replace(/```[\s\S]*?```/g, '')
    // Remove horizontal rules: --- or ***
    .replace(/^[-*]{3,}\s*$/gm, '')
    // Remove HTML tags
    .replace(/<[^>]*>/g, '')
    // Remove emoji shortcodes like :emoji:
    .replace(/:[a-z_]+:/g, '')
    // Collapse multiple spaces/newlines
    .replace(/\s+/g, ' ')
    .trim();
  
  // Find the first meaningful sentence or paragraph
  if (text.length > maxLength) {
    // Try to cut at a sentence boundary
    const cutoff = text.slice(0, maxLength);
    const lastPeriod = cutoff.lastIndexOf('. ');
    const lastQuestion = cutoff.lastIndexOf('? ');
    const lastExclaim = cutoff.lastIndexOf('! ');
    const lastSentence = Math.max(lastPeriod, lastQuestion, lastExclaim);
    
    if (lastSentence > maxLength * 0.5) {
      text = text.slice(0, lastSentence + 1);
    } else {
      // Fall back to word boundary
      const lastSpace = cutoff.lastIndexOf(' ');
      text = text.slice(0, lastSpace > 0 ? lastSpace : maxLength) + '...';
    }
  }
  
  return text;
}

export function getPosts(): Post[] {
  const files = readdirSync('content');
  
  const posts = files
    .filter((f) => f.endsWith('.md'))
    .map((file) => {
      const content = readFileSync(`content/${file}`, 'utf-8');
      const { data, content: body } = matter(content);
      
      const stats = readingTime(body);
      
      // Format date if it's a Date object
      let dateStr = '';
      if (data.date) {
        if (data.date instanceof Date) {
          dateStr = data.date.toLocaleDateString('en-US', { 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric' 
          });
        } else {
          dateStr = String(data.date);
        }
      }
      
      return {
        slug: file.replace('.md', ''),
        title: data.title || 'Untitled',
        author: data.author || 'Unknown',
        date: dateStr,
        excerpt: extractExcerpt(body),
        content: body,
        readingTime: stats.text,
        category: data.category || undefined,
        tags: data.tags || []
      };
    })
    .sort((a, b) => {
      // Sort by actual date from frontmatter (newest first)
      // Extract date from slug if it starts with YYYY-MM-DD format
      const dateRegex = /^(\d{4}-\d{2}-\d{2})/;
      const aDateMatch = a.slug.match(dateRegex);
      const bDateMatch = b.slug.match(dateRegex);
      
      // If both have dates in slug, use those for comparison
      if (aDateMatch && bDateMatch) {
        return bDateMatch[1].localeCompare(aDateMatch[1]);
      }
      
      // If only one has a date, prioritize the one with a date
      if (aDateMatch) return -1;
      if (bDateMatch) return 1;
      
      // If neither has a date in slug, fall back to alphabetical by slug
      return b.slug.localeCompare(a.slug);
    });
  
  return posts;
}

export function getPost(slug: string): Post | null {
  try {
    const content = readFileSync(`content/${slug}.md`, 'utf-8');
    const { data, content: body } = matter(content);
    const stats = readingTime(body);
    
    // Format date if it's a Date object
    let dateStr = '';
    if (data.date) {
      if (data.date instanceof Date) {
        dateStr = data.date.toLocaleDateString('en-US', { 
          year: 'numeric', 
          month: 'long', 
          day: 'numeric' 
        });
      } else {
        dateStr = String(data.date);
      }
    }
    
    return {
      slug,
      title: data.title || 'Untitled',
      author: data.author || 'Unknown',
      date: dateStr,
      content: body,
      readingTime: stats.text
    };
  } catch (err) {
    console.error(`Error loading post ${slug}:`, err);
    return null;
  }
}

