<script lang="ts">
  import type { PageData } from './$types';
  import { base } from '$app/paths';
  import MarkdownContent from '$lib/components/MarkdownContent.svelte';
  import Card from '$lib/components/ui/card.svelte';
  import CardHeader from '$lib/components/ui/card-header.svelte';
  import CardTitle from '$lib/components/ui/card-title.svelte';
  import CardContent from '$lib/components/ui/card-content.svelte';
  import Button from '$lib/components/ui/button.svelte';
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
    ArrowRight
  } from 'lucide-svelte';

  export let data: PageData;
  
  // Split posts into featured and others
  $: featuredPost = data.posts[0];
  $: otherPosts = data.posts.slice(1);
</script>

<div class="max-w-7xl mx-auto px-6 py-12">
  <!-- Intro Section - Updated to white with border -->
  <Card class="bg-white border border-gray-200 text-gray-900 mb-12 p-8 shadow-sm">
    <h2 class="font-display text-3xl mb-4">Welcome to the Language Seed Blog!</h2>
    <p class="text-lg leading-relaxed text-gray-700">
      This is a simple, beautiful, and powerful blog system built with Markdown and Mermaid support.
      Create stunning blog posts with rich formatting, diagrams, code snippets, and more - all from
      simple markdown files.
    </p>
  </Card>

  <!-- Featured Post Content and Latest Posts Section -->
  <div class="mb-16">
    <h2 class="font-display text-4xl mb-8">Latest Posts</h2>
    
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      <!-- Featured Post Content (Left - 2 columns) -->
      {#if featuredPost && data.featuredPostContent}
        <div class="lg:col-span-2">
          <Card class="h-full overflow-hidden">
            <CardHeader class="border-b border-gray-200 pb-4">
              <CardTitle class="text-3xl font-display font-bold mb-3">
                {featuredPost.title}
              </CardTitle>
              <div class="flex items-center gap-4 text-gray-600 text-sm">
                <span class="flex items-center gap-1">
                  <User class="w-4 h-4" />
                  {featuredPost.author}
                </span>
                <span class="flex items-center gap-1">
                  <Calendar class="w-4 h-4" />
                  {featuredPost.date}
                </span>
              </div>
            </CardHeader>
            
            <CardContent class="p-8">
              <MarkdownContent content={data.featuredPostContent} />
            </CardContent>
          </Card>
        </div>

        <!-- Other Posts (Right - 1 column) -->
        <div class="lg:col-span-1 space-y-6">
          {#each otherPosts as post}
            <a href="{base}/posts/{post.slug}" class="block group">
              <Card class="h-full hover:shadow-lg transition-all duration-200">
                <CardContent class="p-6">
                  <h3 class="font-display text-xl font-semibold mb-3 group-hover:text-gray-900 transition-colors">
                    {post.title}
                  </h3>
                  
                  <div class="flex items-center gap-4 text-gray-600 text-sm mb-3">
                    <span class="flex items-center gap-1">
                      <User class="w-3 h-3" />
                      {post.author}
                    </span>
                    <span class="flex items-center gap-1">
                      <Calendar class="w-3 h-3" />
                      {post.date}
                    </span>
                  </div>
                  
                  <p class="text-gray-600 text-sm leading-relaxed line-clamp-3 mb-4">
                    {post.excerpt}
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
      {/if}
    </div>
  </div>

  <!-- Quick Start Guide -->
  <Card class="mb-12 p-8">
    <h2 class="font-display text-3xl mb-6 flex items-center gap-2">
      <Rocket class="w-7 h-7" />
      Quick Start Guide
    </h2>
    <ol class="list-decimal list-inside space-y-3 text-gray-600 leading-relaxed pl-4">
      <li>Create a new markdown file (e.g., <code class="bg-gray-100 px-2 py-1 rounded">my-post.md</code>)</li>
      <li>Add frontmatter with title, author, and date</li>
      <li>Write your content using Markdown syntax</li>
      <li>Run: <code class="bg-gray-100 px-2 py-1 rounded">npm run build</code></li>
      <li>Your blog will be built in the <code class="bg-gray-100 px-2 py-1 rounded">build/</code> folder</li>
      <li>Deploy to GitHub Pages!</li>
    </ol>
  </Card>

  <!-- Features -->
  <h2 class="font-display text-4xl mb-6 flex items-center gap-2">
    <Sparkles class="w-8 h-8" />
    Features
  </h2>
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
    <Card class="hover:shadow-md transition-all hover:-translate-y-1">
      <CardHeader>
        <FileText class="w-8 h-8 text-gray-900 mb-2" />
        <CardTitle>Markdown Support</CardTitle>
      </CardHeader>
      <CardContent>
        <p class="text-sm text-gray-600 leading-relaxed">
          Write in simple Markdown with full GitHub Flavored Markdown support.
        </p>
      </CardContent>
    </Card>

    <Card class="hover:shadow-md transition-all hover:-translate-y-1">
      <CardHeader>
        <BarChart2 class="w-8 h-8 text-gray-900 mb-2" />
        <CardTitle>Mermaid Diagrams</CardTitle>
      </CardHeader>
      <CardContent>
        <p class="text-sm text-gray-600 leading-relaxed">
          Create flowcharts, sequence diagrams, mind maps, and more with Mermaid.
        </p>
      </CardContent>
    </Card>

    <Card class="hover:shadow-md transition-all hover:-translate-y-1">
      <CardHeader>
        <ImageIcon class="w-8 h-8 text-gray-900 mb-2" />
        <CardTitle>Image Support</CardTitle>
      </CardHeader>
      <CardContent>
        <p class="text-sm text-gray-600 leading-relaxed">
          Add images easily with automatic responsive sizing and beautiful styling.
        </p>
      </CardContent>
    </Card>

    <Card class="hover:shadow-md transition-all hover:-translate-y-1">
      <CardHeader>
        <Music class="w-8 h-8 text-gray-900 mb-2" />
        <CardTitle>Audio Players</CardTitle>
      </CardHeader>
      <CardContent>
        <p class="text-sm text-gray-600 leading-relaxed">
          Beautiful Howler.js-powered audio players with play, seek, and volume controls.
        </p>
      </CardContent>
    </Card>

    <Card class="hover:shadow-md transition-all hover:-translate-y-1">
      <CardHeader>
        <Code class="w-8 h-8 text-gray-900 mb-2" />
        <CardTitle>Code Highlighting</CardTitle>
      </CardHeader>
      <CardContent>
        <p class="text-sm text-gray-600 leading-relaxed">
          Share code snippets with syntax highlighting for multiple languages.
        </p>
      </CardContent>
    </Card>

    <Card class="hover:shadow-md transition-all hover:-translate-y-1">
      <CardHeader>
        <Palette class="w-8 h-8 text-gray-900 mb-2" />
        <CardTitle>Beautiful Design</CardTitle>
      </CardHeader>
      <CardContent>
        <p class="text-sm text-gray-600 leading-relaxed">
          Modern, clean design with shadcn components and gorgeous typography.
        </p>
      </CardContent>
    </Card>

    <Card class="hover:shadow-md transition-all hover:-translate-y-1">
      <CardHeader>
        <Smartphone class="w-8 h-8 text-gray-900 mb-2" />
        <CardTitle>Responsive</CardTitle>
      </CardHeader>
      <CardContent>
        <p class="text-sm text-gray-600 leading-relaxed">
          Looks great on all devices - desktop, tablet, and mobile.
        </p>
      </CardContent>
    </Card>
    
    <Card class="hover:shadow-md transition-all hover:-translate-y-1">
      <CardHeader>
        <Rocket class="w-8 h-8 text-gray-900 mb-2" />
        <CardTitle>Static & Fast</CardTitle>
      </CardHeader>
      <CardContent>
        <p class="text-sm text-gray-600 leading-relaxed">
          Pre-rendered static site for blazing fast load times and optimal SEO.
        </p>
      </CardContent>
    </Card>
  </div>
</div>

