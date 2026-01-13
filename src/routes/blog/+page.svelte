<script lang="ts">
  import type { PageData } from './$types';
  import { base } from '$app/paths';
  import MarkdownContent from '$lib/components/MarkdownContent.svelte';
  import { Calendar, User, ArrowRight, BookOpen, Tag } from 'lucide-svelte';

  export let data: PageData;
  
  // All posts sorted by date
  $: allPosts = data.posts;
</script>

<svelte:head>
  <title>Blog - Language Seed</title>
  <meta name="description" content="Articles, tutorials, and notes on AI development" />
</svelte:head>

<div class="max-w-4xl mx-auto px-6 py-12">
  <!-- Header -->
  <div class="text-center mb-12">
    <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 border border-primary/20 mb-6">
      <BookOpen class="w-4 h-4 text-primary" />
      <span class="text-sm font-medium text-primary">Blog</span>
    </div>
    <h1 class="font-display text-4xl md:text-5xl font-bold mb-4">
      All Posts
    </h1>
    <p class="text-lg text-foreground/70 max-w-2xl mx-auto">
      Notes, articles, and tutorials on building AI systems.
    </p>
  </div>

  <!-- Posts List -->
  <div class="space-y-8">
    {#each allPosts as post, index}
      <a href="{base}/posts/{post.slug}" class="block group">
        <article class="card-interactive p-6 md:p-8">
          <div class="flex flex-col md:flex-row gap-6">
            <!-- Post Info -->
            <div class="flex-1">
              <h2 class="font-display text-xl md:text-2xl font-bold mb-3 group-hover:text-primary transition-colors">
                {post.title}
              </h2>
              
              <div class="flex flex-wrap items-center gap-4 text-muted-foreground text-sm mb-4">
                <span class="flex items-center gap-1.5">
                  <User class="w-4 h-4" />
                  {post.author}
                </span>
                <span class="flex items-center gap-1.5">
                  <Calendar class="w-4 h-4" />
                  {post.date}
                </span>
                {#if post.category}
                  <span class="flex items-center gap-1.5">
                    <Tag class="w-4 h-4" />
                    {post.category}
                  </span>
                {/if}
              </div>
              
              <p class="text-muted-foreground leading-relaxed line-clamp-3 mb-4">
                {post.excerpt}
              </p>
              
              <!-- Tags -->
              {#if post.tags && post.tags.length > 0}
                <div class="flex flex-wrap gap-2 mb-4">
                  {#each post.tags.slice(0, 5) as tag}
                    <span class="px-2 py-0.5 text-xs rounded-full bg-secondary text-secondary-foreground">
                      {tag}
                    </span>
                  {/each}
                </div>
              {/if}
              
              <span class="text-primary text-sm font-medium inline-flex items-center gap-1 group-hover:gap-2 transition-all">
                Read article
                <ArrowRight class="w-4 h-4" />
              </span>
            </div>
          </div>
        </article>
      </a>
      
      {#if index < allPosts.length - 1}
        <div class="border-b border-border/50" />
      {/if}
    {/each}
  </div>
</div>
