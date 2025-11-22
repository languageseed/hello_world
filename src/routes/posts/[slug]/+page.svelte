<script lang="ts">
  import type { PageData } from './$types';
  import { base } from '$app/paths';
  import Button from '$lib/components/ui/button.svelte';
  import Card from '$lib/components/ui/card.svelte';
  import CardContent from '$lib/components/ui/card-content.svelte';
  import { ArrowLeft, Calendar, User, ArrowRight } from 'lucide-svelte';
  import MarkdownContent from '$lib/components/MarkdownContent.svelte';

  export let data: PageData;
  const { post, otherPosts } = data;
</script>

<div class="max-w-7xl mx-auto px-6 py-12">
  <!-- Back Button -->
  <a href="{base}/">
    <Button variant="ghost" class="mb-6">
      <ArrowLeft class="w-4 h-4 mr-2" />
      Back to All Posts
    </Button>
  </a>

  <!-- Post Content with Sidebar -->
  <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
    <!-- Main Post Content (Left - 2 columns) -->
    <div class="lg:col-span-2">
      <!-- Post Header -->
      <header class="mb-8">
        <h1 class="font-display text-3xl font-bold mb-4">{post.title}</h1>
        <div class="flex items-center gap-4 text-gray-600">
          <span class="flex items-center gap-1">
            <User class="w-4 h-4" />
            {post.author}
          </span>
          <span class="flex items-center gap-1">
            <Calendar class="w-4 h-4" />
            {post.date}
          </span>
          {#if post.readingTime}
            <span>{post.readingTime}</span>
          {/if}
        </div>
      </header>

      <!-- Post Content -->
      <article class="bg-white border border-gray-200 rounded-md p-8 shadow-sm">
        <MarkdownContent content={post.content} />
      </article>
    </div>

    <!-- Sidebar with Other Posts (Right - 1 column) -->
    <div class="lg:col-span-1">
      <div class="sticky top-6">
        <h2 class="font-display text-2xl font-bold mb-4">More Posts</h2>
        <div class="space-y-4">
          {#each otherPosts as otherPost}
            <a href="{base}/posts/{otherPost.slug}" class="block group" data-sveltekit-reload>
              <Card class="h-full hover:shadow-lg transition-all duration-200">
                <CardContent class="p-6">
                  <h3 class="font-display text-lg font-semibold mb-2 group-hover:text-gray-900 transition-colors">
                    {otherPost.title}
                  </h3>
                  
                  <div class="flex items-center gap-4 text-gray-600 text-xs mb-3">
                    <span class="flex items-center gap-1">
                      <User class="w-3 h-3" />
                      {otherPost.author}
                    </span>
                    <span class="flex items-center gap-1">
                      <Calendar class="w-3 h-3" />
                      {otherPost.date}
                    </span>
                  </div>
                  
                  <p class="text-gray-600 text-sm leading-relaxed line-clamp-2 mb-3">
                    {otherPost.excerpt}
                  </p>
                  
                  <span class="text-gray-900 text-sm font-medium inline-flex items-center gap-1 group-hover:gap-2 transition-all">
                    Read more
                    <ArrowRight class="w-4 h-4" />
                  </span>
                </CardContent>
              </Card>
            </a>
          {/each}
        </div>
      </div>
    </div>
  </div>
</div>

