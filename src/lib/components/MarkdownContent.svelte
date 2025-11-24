<script lang="ts">
  import { onMount } from 'svelte';
  import AudioPlayer from './AudioPlayer.svelte';
  import ImageCarousel from './ImageCarousel.svelte';
  import mermaid from 'mermaid';
  import { processMarkdown } from '$lib/utils/markdown';

  export let content: string;
  
  const { html, audioTags, carousels } = processMarkdown(content);
  let container: HTMLDivElement;
  
  // Split HTML by audio and carousel markers and create segments
  const segments: Array<{ type: 'html' | 'audio' | 'carousel'; content?: string; audioIndex?: number; carouselIndex?: number }> = [];
  
  // Find all markers and their positions
  const audioMarkerRegex = /<div data-audio-marker="(\d+)"[^>]*><\/div>/g;
  const carouselMarkerRegex = /<div data-carousel-marker="(\d+)"[^>]*><\/div>/g;
  const markers: Array<{ type: 'audio' | 'carousel'; index: number; position: number; match: string }> = [];
  let match;
  
  while ((match = audioMarkerRegex.exec(html)) !== null) {
    markers.push({
      type: 'audio',
      index: parseInt(match[1]),
      position: match.index,
      match: match[0]
    });
  }
  
  while ((match = carouselMarkerRegex.exec(html)) !== null) {
    markers.push({
      type: 'carousel',
      index: parseInt(match[1]),
      position: match.index,
      match: match[0]
    });
  }
  
  // Sort markers by position
  markers.sort((a, b) => a.position - b.position);
  
  // Split HTML into segments
  let lastIndex = 0;
  markers.forEach(({ type, index, position, match }) => {
    // Add HTML segment before marker
    if (position > lastIndex) {
      segments.push({
        type: 'html',
        content: html.substring(lastIndex, position)
      });
    }
    // Add audio or carousel segment
    if (type === 'audio') {
      segments.push({
        type: 'audio',
        audioIndex: index
      });
    } else if (type === 'carousel') {
      segments.push({
        type: 'carousel',
        carouselIndex: index
      });
    }
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
      {:else if segment.type === 'carousel' && segment.carouselIndex !== undefined}
        {@const carousel = carousels[segment.carouselIndex]}
        {#if carousel}
          <ImageCarousel images={carousel.images} />
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
    @apply font-display text-4xl font-bold mt-8 mb-6 pb-4 border-b border-gray-200;
  }
  
  :global(.markdown-content h2) {
    @apply font-display text-3xl font-bold mt-8 mb-4 pt-6 pb-3 border-b border-gray-200;
  }
  
  :global(.markdown-content h3) {
    @apply font-display text-2xl font-bold mt-6 mb-3 pt-4;
  }
  
  :global(.markdown-content h4) {
    @apply font-display text-xl font-semibold mt-4 mb-2;
  }
  
  :global(.markdown-content p) {
    @apply mb-4 leading-relaxed;
  }
  
  /* Add visual separation for sections */
  :global(.markdown-content h2 + p),
  :global(.markdown-content h3 + p) {
    @apply mt-2;
  }
  
  /* Style blockquotes as light boxes */
  :global(.markdown-content blockquote) {
    @apply border-l-4 border-gray-300 bg-gray-50 pl-4 pr-4 py-3 my-4 italic text-gray-700;
  }
  
  :global(.markdown-content code) {
    @apply bg-gray-100 px-2 py-1 rounded text-sm font-mono border border-gray-200;
  }
  
  /* Code blocks with light background */
  :global(.markdown-content pre) {
    @apply bg-gray-50 border border-gray-200 text-gray-900 p-4 rounded-md overflow-x-auto mb-4;
  }
  
  :global(.markdown-content pre code) {
    @apply bg-transparent p-0 text-gray-900 border-0;
  }
  
  :global(.markdown-content img) {
    @apply rounded-md shadow-sm my-6 max-w-full border border-gray-200 p-3 bg-white;
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
  
  /* Add light box styling for lists */
  :global(.markdown-content ul),
  :global(.markdown-content ol) {
    @apply border-l-2 border-gray-200 pl-6 pr-4 py-2;
  }
  
  /* Style horizontal rules as boundaries */
  :global(.markdown-content hr) {
    @apply my-8 border-0 border-t border-gray-200;
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

