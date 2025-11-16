import { getPost, getPosts } from '$lib/utils/posts';
import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
  const post = getPost(params.slug);
  
  if (!post) {
    throw error(404, 'Post not found');
  }
  
  return { post };
};

export async function entries() {
  const posts = getPosts();
  return posts.map((post) => ({ slug: post.slug }));
}
