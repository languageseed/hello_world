<script lang="ts">
  import type { PageData } from './$types';
  import { base } from '$app/paths';
  import { Folder, Calendar, User, ArrowRight, BookOpen } from 'lucide-svelte';

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
  <title>Hello World - Language Seed</title>
  <meta name="description" content="AI projects portfolio - Building AI infrastructure for my home lab" />
</svelte:head>

<!-- Hero Section -->
<section class="relative overflow-hidden">
  <!-- Background effects -->
  <div class="absolute inset-0 bg-gradient-mesh" />
  
  <div class="relative max-w-7xl mx-auto px-6 py-12 md:py-20">
    <div class="flex flex-col md:flex-row items-center gap-8 md:gap-12">
      <!-- Hero Image -->
      <div class="flex-shrink-0 w-full md:w-1/2 flex justify-center">
        <img 
          src="{base}/images/helloworld-hero.jpg" 
          alt="Hello World mascot" 
          class="w-full max-w-md rounded-2xl shadow-2xl shadow-primary/20"
        />
      </div>
      
      <!-- Text Content -->
      <div class="flex-1 text-center md:text-left">
        <!-- Badge -->
        <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 border border-primary/20 mb-6">
          <span class="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
          <span class="text-sm font-medium text-primary">Building AI Systems</span>
        </div>
        
        <!-- Headline -->
        <h1 class="font-display text-4xl md:text-5xl lg:text-6xl font-bold mb-6 text-balance">
          Welcome to
          <span class="gradient-text-cyan"> Hello World</span>
        </h1>
        
        <!-- Subheadline -->
        <p class="text-lg md:text-xl text-foreground/90 max-w-xl text-balance mb-8">
          A collection of AI infrastructure, agents, and tools built for my home lab environment.
        </p>
        
        <!-- CTA -->
        <a 
          href="{base}/blog" 
          class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-secondary text-secondary-foreground font-semibold border border-border hover:bg-secondary/80 transition-all"
        >
          <BookOpen class="w-4 h-4" />
          Read Blog
        </a>
      </div>
    </div>
  </div>
  
  <!-- Gradient fade at bottom -->
  <div class="absolute bottom-0 left-0 right-0 h-24 bg-gradient-to-t from-background to-transparent" />
</section>

<!-- Portfolio Grid -->
<section class="max-w-7xl mx-auto px-6 py-12">
  <div class="section-header mb-8">
    <div class="icon">
      <Folder class="w-5 h-5" />
    </div>
    <h2>Projects</h2>
  </div>

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
            <h3 class="font-display text-xl font-bold mb-2 group-hover:text-primary transition-colors line-clamp-2">
              {post.title}
            </h3>
            
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
</section>
