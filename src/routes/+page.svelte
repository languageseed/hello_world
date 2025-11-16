<script lang="ts">
  import type { PageData } from './$types';
  import { base } from '$app/paths';
  import PostCard from '$lib/components/PostCard.svelte';
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
    Pencil,
    Rocket,
    Sparkles
  } from 'lucide-svelte';

  export let data: PageData;
  // Accept params prop to suppress warning (SvelteKit passes it)
  export let params: any = {};
</script>

<div class="max-w-7xl mx-auto px-6 py-12">
  <!-- Intro Section -->
  <Card class="bg-gradient-to-br from-gray-900 to-gray-700 text-white mb-12 p-8 shadow-lg">
    <h2 class="font-display text-3xl mb-4">Welcome to the Language Seed Blog!</h2>
    <p class="text-lg leading-relaxed opacity-95">
      This is a simple, beautiful, and powerful blog system built with Markdown and Mermaid support.
      Create stunning blog posts with rich formatting, diagrams, code snippets, and more - all from
      simple markdown files.
    </p>
  </Card>

  <!-- Merman Button -->
  <div class="text-center mb-8">
    <a href="{base}/merman">
      <Button
        variant="default"
        size="lg"
        class="bg-gradient-to-r from-gray-800 to-gray-900 text-white px-8 py-6 text-lg font-bold shadow-lg hover:scale-105 transition-transform"
      >
        <Pencil class="w-5 h-5 mr-2" />
        Open Merman Scratchpad
      </Button>
    </a>
    <p class="mt-3 text-gray-600 text-sm">
      Quick Markdown & Mermaid preview tool - paste, edit, and see results instantly!
    </p>
  </div>

  <!-- Latest Posts -->
  <h2 class="font-display text-4xl mb-6">Latest Posts</h2>
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-12">
    {#each data.posts as post}
      <PostCard post={post} />
    {/each}
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
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">
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
  </div>
</div>

