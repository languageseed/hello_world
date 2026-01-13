<script lang="ts">
  import type { PageData } from './$types';
  import { base } from '$app/paths';
  import Button from '$lib/components/ui/button.svelte';
  import Card from '$lib/components/ui/card.svelte';
  import CardContent from '$lib/components/ui/card-content.svelte';
  import { ArrowLeft, Calendar, User, ArrowRight, Clock } from 'lucide-svelte';
  import MarkdownContent from '$lib/components/MarkdownContent.svelte';

  export let data: PageData;
  const { post, otherPosts } = data;
</script>

<div class="max-w-7xl mx-auto px-6 py-12">
  <!-- Back Button -->
  <a href="{base}/" class="inline-flex items-center gap-2 text-foreground/70 hover:text-primary transition-colors mb-8">
    <ArrowLeft class="w-4 h-4" />
    <span class="text-sm font-medium">Back to All Posts</span>
  </a>

  <!-- Post Content with Sidebar -->
  <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
    <!-- Main Post Content (Left - 2 columns) -->
    <div class="lg:col-span-2">
      <!-- Post Header -->
      <header class="mb-8">
        <h1 class="font-display text-3xl md:text-4xl font-bold mb-4 text-foreground">{post.title}</h1>
        <div class="flex flex-wrap items-center gap-4 text-foreground/60 text-sm">
          <span class="flex items-center gap-1.5">
            <User class="w-4 h-4" />
            {post.author}
          </span>
          <span class="flex items-center gap-1.5">
            <Calendar class="w-4 h-4" />
            {post.date}
          </span>
          {#if post.readingTime}
            <span class="flex items-center gap-1.5">
              <Clock class="w-4 h-4" />
              {post.readingTime}
            </span>
          {/if}
        </div>
      </header>

      <!-- Post Content -->
      <article class="bg-card border border-border rounded-xl p-6 md:p-8">
        <MarkdownContent content={post.content} />
      </article>
    </div>

    <!-- Sidebar with Other Posts (Right - 1 column) -->
    <div class="lg:col-span-1">
      <div class="sticky top-20">
        <h2 class="font-display text-xl font-bold mb-4 text-foreground">More Posts</h2>
        <div class="space-y-4">
          {#each otherPosts as otherPost}
            <a href="{base}/posts/{otherPost.slug}" class="block group" data-sveltekit-reload>
              <div class="card-interactive p-4">
                <h3 class="font-display text-base font-semibold mb-2 text-foreground group-hover:text-primary transition-colors">
                  {otherPost.title}
                </h3>
                
                <div class="flex items-center gap-3 text-foreground/50 text-xs mb-3">
                  <span class="flex items-center gap-1">
                    <User class="w-3 h-3" />
                    {otherPost.author}
                  </span>
                  <span class="flex items-center gap-1">
                    <Calendar class="w-3 h-3" />
                    {otherPost.date}
                  </span>
                </div>
                
                <p class="text-foreground/70 text-sm leading-relaxed line-clamp-2 mb-3">
                  {otherPost.excerpt}
                </p>
                
                <span class="text-primary text-sm font-medium inline-flex items-center gap-1 group-hover:gap-2 transition-all">
                  Read more
                  <ArrowRight class="w-4 h-4" />
                </span>
              </div>
            </a>
          {/each}
        </div>
      </div>
    </div>
  </div>
</div>
