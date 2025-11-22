import { getPosts } from '$lib/utils/posts';
import type { PageServerLoad } from './$types';
import { readFileSync } from 'fs';
import matter from 'gray-matter';

export const load: PageServerLoad = async () => {
  const posts = getPosts();
  
  // Load the full content of the first (latest) post
  let featuredPostContent = '';
  if (posts.length > 0) {
    try {
      const fullPath = `content/${posts[0].slug}.md`;
      const fileContent = readFileSync(fullPath, 'utf-8');
      const { content } = matter(fileContent);
      featuredPostContent = content;
    } catch (error) {
      console.error('Error loading featured post content:', error);
    }
  }
  
  return { 
    posts,
    featuredPostContent 
  };
};

