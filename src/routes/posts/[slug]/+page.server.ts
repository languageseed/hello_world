import { getPost, getPosts } from '$lib/utils/posts';
import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
  const post = getPost(params.slug);
  
  if (!post) {
    throw error(404, 'Post not found');
  }
  
  // Get all posts for the sidebar
  const allPosts = getPosts();
  
  // Filter out the current post and get up to 5 other posts
  const otherPosts = allPosts.filter(p => p.slug !== params.slug).slice(0, 5);
  
  return { post, otherPosts };
};

export async function entries() {
  const posts = getPosts();
  return posts.map((post) => ({ slug: post.slug }));
}
