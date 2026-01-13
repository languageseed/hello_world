<script lang="ts">
  import type { PageData } from './$types';
  import { base } from '$app/paths';
  import { Folder, Calendar, User, ArrowRight } from 'lucide-svelte';

  export let data: PageData;
  
  // Filter only project posts (category: projects)
  $: projectPosts = data.posts.filter(post => 
    post.category === 'projects' || 
    post.tags?.includes('projects') ||
    post.slug?.includes('valet') ||
    post.slug?.includes('agent') ||
    post.slug?.includes('processor') ||
    post.slug?.includes('gateway') ||
    post.slug?.includes('vacuum') ||
    post.slug?.includes('suite') ||
    post.slug?.includes('comfyui')
  );
</script>

<svelte:head>
  <title>Portfolio - Language Seed</title>
  <meta name="description" content="AI projects portfolio - Valet ecosystem, agents, and infrastructure" />
</svelte:head>

<div class="max-w-7xl mx-auto px-6 py-12">
  <!-- Header -->
  <div class="text-center mb-12">
    <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 border border-primary/20 mb-6">
      <Folder class="w-4 h-4 text-primary" />
      <span class="text-sm font-medium text-primary">Project Portfolio</span>
    </div>
    <h1 class="font-display text-4xl md:text-5xl font-bold mb-4">
      AI Projects
    </h1>
    <p class="text-lg text-foreground/70 max-w-2xl mx-auto">
      A collection of AI infrastructure, agents, and tools built for my home lab environment.
    </p>
  </div>

  <!-- Portfolio Grid -->
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    {#each projectPosts as post}
      <a href="{base}/posts/{post.slug}" class="group block">
        <article class="card-interactive h-full flex flex-col overflow-hidden">
          <!-- Hero Image -->
          {#if post.slug}
            <div class="aspect-video overflow-hidden bg-secondary/50">
              <img 
                src="{base}/images/hero-{post.slug.replace('2026-01-13-', '')}.png" 
                alt={post.title}
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                onerror="this.style.display='none'"
              />
            </div>
          {/if}
          
          <!-- Content -->
          <div class="p-6 flex-1 flex flex-col">
            <h2 class="font-display text-xl font-bold mb-2 group-hover:text-primary transition-colors line-clamp-2">
              {post.title}
            </h2>
            
            <div class="flex items-center gap-3 text-muted-foreground text-xs mb-3">
              <span class="flex items-center gap-1">
                <User class="w-3 h-3" />
                {post.author}
              </span>
              <span class="flex items-center gap-1">
                <Calendar class="w-3 h-3" />
                {post.date}
              </span>
            </div>
            
            <p class="text-muted-foreground text-sm leading-relaxed line-clamp-3 flex-1 mb-4">
              {post.excerpt}
            </p>
            
            <!-- Tags -->
            {#if post.tags && post.tags.length > 0}
              <div class="flex flex-wrap gap-1 mb-4">
                {#each post.tags.slice(0, 4) as tag}
                  <span class="px-2 py-0.5 text-xs rounded-full bg-secondary text-secondary-foreground">
                    {tag}
                  </span>
                {/each}
              </div>
            {/if}
            
            <span class="text-primary text-sm font-medium inline-flex items-center gap-1 group-hover:gap-2 transition-all mt-auto">
              View Project
              <ArrowRight class="w-4 h-4" />
            </span>
          </div>
        </article>
      </a>
    {/each}
  </div>
</div>
