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
      
      return {
        slug: file.replace('.md', ''),
        title: data.title || 'Untitled',
        author: data.author || 'Unknown',
        date: data.date || '',
        excerpt: body.slice(0, 200).replace(/\n/g, ' ') + '...',
        content: body,
        readingTime: stats.text
      };
    })
    .sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
  
  return posts;
}

export function getPost(slug: string): Post | null {
  try {
    const content = readFileSync(`content/${slug}.md`, 'utf-8');
    const { data, content: body } = matter(content);
    const stats = readingTime(body);
    
    return {
      slug,
      title: data.title || 'Untitled',
      author: data.author || 'Unknown',
      date: data.date || '',
      content: body,
      readingTime: stats.text
    };
  } catch {
    return null;
  }
}

