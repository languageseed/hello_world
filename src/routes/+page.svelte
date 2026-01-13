<script lang="ts">
  import type { PageData } from './$types';
  import { base } from '$app/paths';
  import MarkdownContent from '$lib/components/MarkdownContent.svelte';
  import {
    FileText,
    BarChart2,
    Image as ImageIcon,
    Music,
    Code,
    Palette,
    Smartphone,
    Rocket,
    Sparkles,
    Calendar,
    User,
    ArrowRight,
    Zap,
    Layers,
    Terminal,
    BookOpen
  } from 'lucide-svelte';

  export let data: PageData;
  
  // Split posts into featured and others
  $: featuredPost = data.posts[0];
  $: otherPosts = data.posts.slice(1, 4);
  
  const stats = [
    { value: '950K', label: 'Lines of Code', icon: Code },
    { value: '55+', label: 'Containers', icon: Layers },
    { value: '8', label: 'AI Projects', icon: Zap },
  ];
  
  const features = [
    { icon: FileText, title: 'Markdown Support', description: 'Write in simple Markdown with full GFM support.' },
    { icon: BarChart2, title: 'Mermaid Diagrams', description: 'Create flowcharts, sequence diagrams, and more.' },
    { icon: ImageIcon, title: 'Image Support', description: 'Automatic responsive sizing and beautiful styling.' },
    { icon: Music, title: 'Audio Players', description: 'Howler.js-powered players with full controls.' },
    { icon: Code, title: 'Code Highlighting', description: 'Syntax highlighting for multiple languages.' },
    { icon: Palette, title: 'Beautiful Design', description: 'Modern design with shadcn components.' },
    { icon: Smartphone, title: 'Responsive', description: 'Looks great on desktop, tablet, and mobile.' },
    { icon: Rocket, title: 'Static & Fast', description: 'Pre-rendered for blazing fast load times.' },
  ];
</script>

<svelte:head>
  <title>Hello World - Language Seed Blog</title>
  <meta name="description" content="Notes to self, articles and content to share. Building AI systems and sharing knowledge." />
</svelte:head>

<!-- Hero Section -->
<section class="relative overflow-hidden">
  <!-- Background effects -->
  <div class="absolute inset-0 bg-gradient-mesh" />
  <div class="absolute inset-0 bg-grid opacity-30" />
  
  <div class="relative max-w-7xl mx-auto px-6 py-20 md:py-32">
    <div class="max-w-4xl mx-auto text-center stagger-children">
      <!-- Badge -->
      <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 border border-primary/20 mb-8">
        <span class="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
        <span class="text-sm font-medium text-primary">Building AI Systems</span>
      </div>
      
      <!-- Headline -->
      <h1 class="font-display text-4xl md:text-6xl lg:text-7xl font-bold mb-6 text-balance">
        Welcome to
        <span class="gradient-text-cyan"> Hello World</span>
      </h1>
      
      <!-- Subheadline -->
      <p class="text-lg md:text-xl text-foreground/90 max-w-2xl mx-auto mb-10 text-balance">
        Notes to self, articles and content to share with others. 
        Documenting the journey of building production AI infrastructure.
      </p>
      
      <!-- Stats -->
      <div class="flex flex-wrap justify-center gap-8 md:gap-12 mb-10">
        {#each stats as stat}
          <div class="text-center group">
            <div class="flex items-center justify-center gap-2 mb-1">
              <svelte:component this={stat.icon} class="w-5 h-5 text-primary" />
              <span class="text-3xl md:text-4xl font-mono font-bold text-foreground group-hover:text-primary transition-colors">
                {stat.value}
              </span>
            </div>
            <span class="text-sm text-foreground/70">{stat.label}</span>
          </div>
        {/each}
      </div>
      
      <!-- CTA Buttons -->
      <div class="flex flex-wrap justify-center gap-4">
        <a href="#posts" class="btn-primary">
          <BookOpen class="w-4 h-4" />
          Read Blog
        </a>
        <a href="{base}/merman" class="btn-secondary">
          <Terminal class="w-4 h-4" />
          Scratchpad
        </a>
      </div>
    </div>
  </div>
  
  <!-- Gradient fade at bottom -->
  <div class="absolute bottom-0 left-0 right-0 h-24 bg-gradient-to-t from-background to-transparent" />
</section>

<!-- Latest Posts Section -->
<section id="posts" class="max-w-7xl mx-auto px-6 py-16">
  <div class="section-header">
    <div class="icon">
      <BookOpen class="w-5 h-5" />
    </div>
    <h2>Latest Posts</h2>
  </div>
  
  <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
    <!-- Featured Post (Left - 2 columns) -->
    {#if featuredPost && data.featuredPostContent}
      <div class="lg:col-span-2">
        <article class="card-interactive h-full">
          <div class="border-b border-border pb-4 mb-6">
            <h3 class="text-2xl md:text-3xl font-display font-bold mb-3">
              <a href="{base}/posts/{featuredPost.slug}" class="hover:text-primary transition-colors">
                {featuredPost.title}
              </a>
            </h3>
            <div class="flex items-center gap-4 text-muted-foreground text-sm">
              <span class="flex items-center gap-1.5">
                <User class="w-4 h-4" />
                {featuredPost.author}
              </span>
              <span class="flex items-center gap-1.5">
                <Calendar class="w-4 h-4" />
                {featuredPost.date}
              </span>
            </div>
          </div>
          
          <div class="prose prose-sm max-w-none">
            <MarkdownContent content={data.featuredPostContent} />
          </div>
        </article>
      </div>

      <!-- Other Posts (Right - 1 column) -->
      <div class="lg:col-span-1 space-y-6">
        {#each otherPosts as post}
          <a href="{base}/posts/{post.slug}" class="block group">
            <article class="card-interactive">
              <h4 class="font-display text-lg font-semibold mb-2 group-hover:text-primary transition-colors">
                {post.title}
              </h4>
              
              <div class="flex items-center gap-4 text-muted-foreground text-xs mb-3">
                <span class="flex items-center gap-1">
                  <User class="w-3 h-3" />
                  {post.author}
                </span>
                <span class="flex items-center gap-1">
                  <Calendar class="w-3 h-3" />
                  {post.date}
                </span>
              </div>
              
              <p class="text-muted-foreground text-sm leading-relaxed line-clamp-2 mb-4">
                {post.excerpt}
              </p>
              
              <span class="text-primary text-sm font-medium inline-flex items-center gap-1 group-hover:gap-2 transition-all">
                Read more
                <ArrowRight class="w-4 h-4" />
              </span>
            </article>
          </a>
        {/each}
      </div>
    {/if}
  </div>
</section>

<!-- Quick Start Guide -->
<section class="max-w-7xl mx-auto px-6 py-16">
  <div class="card-modern p-8 md:p-10">
    <div class="section-header mb-6">
      <div class="icon">
        <Rocket class="w-5 h-5" />
      </div>
      <h2>Quick Start Guide</h2>
    </div>
    
    <div class="grid md:grid-cols-2 gap-8">
      <div>
        <ol class="space-y-4">
          <li class="flex gap-4">
            <span class="flex-shrink-0 w-8 h-8 rounded-lg bg-primary/10 text-primary font-mono font-bold flex items-center justify-center">1</span>
            <div>
              <p class="font-medium">Create a markdown file</p>
              <code class="text-sm text-muted-foreground">content/my-post.md</code>
            </div>
          </li>
          <li class="flex gap-4">
            <span class="flex-shrink-0 w-8 h-8 rounded-lg bg-primary/10 text-primary font-mono font-bold flex items-center justify-center">2</span>
            <div>
              <p class="font-medium">Add frontmatter</p>
              <code class="text-sm text-muted-foreground">title, author, date</code>
            </div>
          </li>
          <li class="flex gap-4">
            <span class="flex-shrink-0 w-8 h-8 rounded-lg bg-primary/10 text-primary font-mono font-bold flex items-center justify-center">3</span>
            <div>
              <p class="font-medium">Write your content</p>
              <code class="text-sm text-muted-foreground">Markdown + Mermaid</code>
            </div>
          </li>
        </ol>
      </div>
      
      <div>
        <ol class="space-y-4" start="4">
          <li class="flex gap-4">
            <span class="flex-shrink-0 w-8 h-8 rounded-lg bg-primary/10 text-primary font-mono font-bold flex items-center justify-center">4</span>
            <div>
              <p class="font-medium">Build the site</p>
              <code class="text-sm text-muted-foreground">npm run build</code>
            </div>
          </li>
          <li class="flex gap-4">
            <span class="flex-shrink-0 w-8 h-8 rounded-lg bg-primary/10 text-primary font-mono font-bold flex items-center justify-center">5</span>
            <div>
              <p class="font-medium">Preview locally</p>
              <code class="text-sm text-muted-foreground">npm run preview</code>
            </div>
          </li>
          <li class="flex gap-4">
            <span class="flex-shrink-0 w-8 h-8 rounded-lg bg-primary/10 text-primary font-mono font-bold flex items-center justify-center">6</span>
            <div>
              <p class="font-medium">Deploy</p>
              <code class="text-sm text-muted-foreground">Push to GitHub Pages</code>
            </div>
          </li>
        </ol>
      </div>
    </div>
  </div>
</section>

<!-- Features -->
<section class="max-w-7xl mx-auto px-6 py-16">
  <div class="section-header">
    <div class="icon">
      <Sparkles class="w-5 h-5" />
    </div>
    <h2>Features</h2>
  </div>
  
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 stagger-children">
    {#each features as feature}
      <div class="card-interactive group">
        <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-primary/20 to-primary/5 
                    flex items-center justify-center mb-4
                    group-hover:from-primary/30 group-hover:to-primary/10 transition-all">
          <svelte:component this={feature.icon} class="w-6 h-6 text-primary" />
        </div>
        <h3 class="font-display font-semibold mb-2">{feature.title}</h3>
        <p class="text-sm text-muted-foreground leading-relaxed">
          {feature.description}
        </p>
      </div>
    {/each}
  </div>
</section>
