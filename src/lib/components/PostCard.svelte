<script lang="ts">
  import Card from './ui/card.svelte';
  import CardHeader from './ui/card-header.svelte';
  import CardTitle from './ui/card-title.svelte';
  import CardDescription from './ui/card-description.svelte';
  import CardContent from './ui/card-content.svelte';
  import Button from './ui/button.svelte';
  import { Calendar, User } from 'lucide-svelte';
  import { base } from '$app/paths';
  import type { Post } from '$lib/utils/posts';

  export let post: Post;
</script>

<a href="{base}/posts/{post.slug}" class="block">
  <Card class="hover:shadow-xl transition-all cursor-pointer group h-full">
    <CardHeader class="bg-gradient-to-br from-gray-700 to-gray-900 text-white p-6">
      <CardTitle class="text-white mb-2">{post.title}</CardTitle>
      <CardDescription class="text-white/90 text-sm flex items-center gap-4">
        <span class="flex items-center gap-1">
          <User class="w-4 h-4" />
          {post.author}
        </span>
        <span class="flex items-center gap-1">
          <Calendar class="w-4 h-4" />
          {post.date}
        </span>
      </CardDescription>
    </CardHeader>
    <CardContent class="p-6">
      <p class="text-gray-600 leading-relaxed mb-5">{post.excerpt}</p>
      <Button variant="default" class="group-hover:scale-105 transition-transform">
        Read More →
      </Button>
    </CardContent>
  </Card>
</a>

