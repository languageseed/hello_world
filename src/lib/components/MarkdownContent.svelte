<script lang="ts">
  import { onMount } from 'svelte';
  import AudioPlayer from './AudioPlayer.svelte';
  import mermaid from 'mermaid';
  import { processMarkdown } from '$lib/utils/markdown';

  export let content: string;
  
  const { html, audioTags } = processMarkdown(content);
  let container: HTMLDivElement;
  
  // Split HTML by audio markers and create segments
  const segments: Array<{ type: 'html' | 'audio'; content?: string; audioIndex?: number }> = [];
  
  // Find all audio markers and their positions
  const audioMarkerRegex = /<div data-audio-marker="(\d+)"[^>]*><\/div>/g;
  const markers: Array<{ index: number; position: number; match: string }> = [];
  let match;
  
  while ((match = audioMarkerRegex.exec(html)) !== null) {
    markers.push({
      index: parseInt(match[1]),
      position: match.index,
      match: match[0]
    });
  }
  
  // Sort markers by position
  markers.sort((a, b) => a.position - b.position);
  
  // Split HTML into segments
  let lastIndex = 0;
  markers.forEach(({ index, position, match }) => {
    // Add HTML segment before marker
    if (position > lastIndex) {
      segments.push({
        type: 'html',
        content: html.substring(lastIndex, position)
      });
    }
    // Add audio segment
    segments.push({
      type: 'audio',
      audioIndex: index
    });
    lastIndex = position + match.length;
  });
  
  // Add remaining HTML
  if (lastIndex < html.length) {
    segments.push({
      type: 'html',
      content: html.substring(lastIndex)
    });
  }
  
  // If no markers, just add the whole HTML
  if (segments.length === 0) {
    segments.push({ type: 'html', content: html });
  }

  onMount(async () => {
    // Initialize Mermaid
    mermaid.initialize({
      startOnLoad: false,
      theme: 'default',
      securityLevel: 'loose'
    });

    // Process Mermaid diagrams
    await new Promise((resolve) => setTimeout(resolve, 100));
    if (container) {
      const mermaidElements = container.querySelectorAll('pre code.language-mermaid');
      mermaidElements.forEach(async (el) => {
        const code = el.textContent || '';
        if (code.trim()) {
          const id = `mermaid-${Math.random().toString(36).substr(2, 9)}`;
          try {
            const { svg } = await mermaid.render(id, code);
            const mermaidContainer = document.createElement('div');
            mermaidContainer.className = 'mermaid-container my-6';
            mermaidContainer.innerHTML = svg;
            const pre = el.parentElement;
            if (pre) {
              pre.replaceWith(mermaidContainer);
            }
          } catch (error) {
            console.error('Mermaid error:', error);
          }
        }
      });
    }
  });
</script>

<div class="markdown-wrapper">
  <div bind:this={container} class="markdown-content">
    {#each segments as segment}
      {#if segment.type === 'html' && segment.content}
        {@html segment.content}
      {:else if segment.type === 'audio' && segment.audioIndex !== undefined}
        {@const audioTag = audioTags[segment.audioIndex]}
        {#if audioTag}
          <AudioPlayer src={audioTag.src} title={audioTag.title} />
        {/if}
      {/if}
    {/each}
  </div>
</div>

<style>
  :global(.markdown-content) {
    @apply text-gray-700;
  }
  
  :global(.markdown-content h1) {
    @apply font-display text-4xl font-bold mt-8 mb-4;
  }
  
  :global(.markdown-content h2) {
    @apply font-display text-3xl font-bold mt-6 mb-3;
  }
  
  :global(.markdown-content h3) {
    @apply font-display text-2xl font-bold mt-4 mb-2;
  }
  
  :global(.markdown-content p) {
    @apply mb-4 leading-relaxed;
  }
  
  :global(.markdown-content code) {
    @apply bg-gray-100 px-2 py-1 rounded text-sm font-mono;
  }
  
  :global(.markdown-content pre) {
    @apply bg-gray-900 text-gray-100 p-4 rounded-md overflow-x-auto mb-4;
  }
  
  :global(.markdown-content pre code) {
    @apply bg-transparent p-0 text-gray-100;
  }
  
  :global(.markdown-content img) {
    @apply rounded-md shadow-md my-6 max-w-full;
  }
  
  :global(.markdown-content a) {
    @apply text-gray-900 hover:underline;
  }
  
  :global(.markdown-content ul, .markdown-content ol) {
    @apply mb-4 pl-6;
  }
  
  :global(.markdown-content li) {
    @apply mb-2;
  }
  
  :global(.markdown-wrapper) {
    @apply overflow-x-auto;
  }
  
  :global(.markdown-content table) {
    @apply w-full border-collapse mb-6 mt-4;
    border: 1px solid hsl(var(--border));
    min-width: 100%;
  }
  
  :global(.markdown-content thead) {
    @apply bg-gray-100;
  }
  
  :global(.markdown-content th) {
    @apply px-4 py-3 text-left font-semibold text-gray-900 border-b border-gray-300;
  }
  
  :global(.markdown-content td) {
    @apply px-4 py-3 border-b border-gray-200 text-gray-700;
  }
  
  :global(.markdown-content tbody tr:hover) {
    @apply bg-gray-50;
  }
  
  :global(.markdown-content tbody tr:last-child td) {
    @apply border-b-0;
  }
  
  :global(.mermaid-container) {
    @apply flex justify-center overflow-x-auto my-6;
  }
</style>

