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
        excerpt: body.slice(0, 200).replace(/\n/g, ' ') + '...',
        content: body,
        readingTime: stats.text
      };
    })
    .sort((a, b) => {
      // Sort by file name which includes date
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

