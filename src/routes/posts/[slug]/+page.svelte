<script lang="ts">
  import type { PageData } from './$types';
  import { base } from '$app/paths';
  import Button from '$lib/components/ui/button.svelte';
  import { ArrowLeft, Calendar, User } from 'lucide-svelte';
  import MarkdownContent from '$lib/components/MarkdownContent.svelte';

  export let data: PageData;
  const { post } = data;
</script>

<div class="max-w-4xl mx-auto px-6 py-12">
  <!-- Back Button -->
  <a href="{base}/">
    <Button variant="ghost" class="mb-6">
      <ArrowLeft class="w-4 h-4 mr-2" />
      Back to All Posts
    </Button>
  </a>

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

