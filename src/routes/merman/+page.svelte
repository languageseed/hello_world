<script lang="ts">
  import { onMount } from 'svelte';
  import { base } from '$app/paths';
  import { marked } from 'marked';
  import mermaid from 'mermaid';
  import Button from '$lib/components/ui/button.svelte';
  import Card from '$lib/components/ui/card.svelte';
  import { Download, Copy, Trash2, Home, Fish } from 'lucide-svelte';

  let markdown = '';
  let previewHtml = '';
  let previewContainer: HTMLDivElement;

  // Load from localStorage on mount
  onMount(() => {
    const saved = localStorage.getItem('merman-content');
    if (saved) {
      markdown = saved;
      updatePreview();
    }

    // Initialize Mermaid
    mermaid.initialize({
      startOnLoad: false,
      theme: 'default',
      securityLevel: 'loose'
    });
  });

  function updatePreview() {
    // Save to localStorage
    localStorage.setItem('merman-content', markdown);

    // Process markdown
    marked.setOptions({
      breaks: true,
      gfm: true
    });

    let html = marked.parse(markdown);
    previewHtml = html;

    // Process Mermaid diagrams after a short delay
    setTimeout(() => {
      if (previewContainer) {
        const mermaidElements = previewContainer.querySelectorAll('pre code.language-mermaid');
        mermaidElements.forEach(async (el) => {
          const code = el.textContent || '';
          if (code.trim()) {
            const id = `mermaid-${Math.random().toString(36).substr(2, 9)}`;
            try {
              const { svg } = await mermaid.render(id, code);
              const container = document.createElement('div');
              container.className = 'mermaid-container my-6';
              container.innerHTML = svg;
              const pre = el.parentElement;
              if (pre) {
                pre.replaceWith(container);
              }
            } catch (error) {
              console.error('Mermaid error:', error);
            }
          }
        });
      }
    }, 100);
  }

  function copyToClipboard() {
    navigator.clipboard.writeText(markdown);
    alert('Copied to clipboard!');
  }

  function downloadMarkdown() {
    const blob = new Blob([markdown], { type: 'text/markdown' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'merman-content.md';
    a.click();
    URL.revokeObjectURL(url);
  }

  function clearContent() {
    if (confirm('Clear all content?')) {
      markdown = '';
      previewHtml = '';
      localStorage.removeItem('merman-content');
    }
  }
</script>

<div class="h-screen flex flex-col">
  <!-- Header -->
  <header class="bg-gray-900 text-white px-6 py-4 flex items-center justify-between">
    <div>
      <h1 class="font-display text-2xl font-bold flex items-center gap-2">
        <Fish class="w-6 h-6" />
        Merman Scratchpad
      </h1>
      <p class="text-sm opacity-90">Quick Markdown & Mermaid preview tool</p>
    </div>
    <div class="flex items-center gap-2">
      <a href="{base}/">
        <Button variant="ghost" size="sm" class="text-white hover:bg-white/10">
          <Home class="w-4 h-4 mr-2" />
          Home
        </Button>
      </a>
      <Button variant="ghost" size="sm" class="text-white hover:bg-white/10" on:click={copyToClipboard}>
        <Copy class="w-4 h-4 mr-2" />
        Copy
      </Button>
      <Button variant="ghost" size="sm" class="text-white hover:bg-white/10" on:click={downloadMarkdown}>
        <Download class="w-4 h-4 mr-2" />
        Download
      </Button>
      <Button variant="ghost" size="sm" class="text-white hover:bg-white/10" on:click={clearContent}>
        <Trash2 class="w-4 h-4 mr-2" />
        Clear
      </Button>
    </div>
  </header>

  <!-- Split Pane -->
  <div class="flex-1 flex overflow-hidden">
    <!-- Editor -->
    <div class="w-1/2 border-r border-gray-200 flex flex-col">
      <div class="bg-gray-100 px-4 py-2 border-b border-gray-200">
        <h2 class="font-semibold text-gray-700">Markdown Editor</h2>
      </div>
      <textarea
        bind:value={markdown}
        on:input={updatePreview}
        class="flex-1 w-full p-4 font-mono text-sm resize-none border-0 focus:outline-none focus:ring-0"
        placeholder="Start typing your Markdown here...

# Example Heading

- List item 1
- List item 2

\`\`\`mermaid
graph TD
    A[Start] --> B[Process]
    B --> C[End]
\`\`\`"
      />
    </div>

    <!-- Preview -->
    <div class="w-1/2 overflow-auto bg-white flex flex-col">
      <div class="bg-gray-100 px-4 py-2 border-b border-gray-200">
        <h2 class="font-semibold text-gray-700">Preview</h2>
      </div>
      <div
        bind:this={previewContainer}
        class="flex-1 p-6 prose prose-lg max-w-none markdown-preview"
      >
        {#if previewHtml}
          {@html previewHtml}
        {:else}
          <p class="text-gray-400 italic">Preview will appear here...</p>
        {/if}
      </div>
    </div>
  </div>
</div>

<style>
  :global(.markdown-preview) {
    @apply text-gray-700;
  }
  
  :global(.markdown-preview h1) {
    @apply font-display text-4xl font-bold mt-8 mb-4;
  }
  
  :global(.markdown-preview h2) {
    @apply font-display text-3xl font-bold mt-6 mb-3;
  }
  
  :global(.markdown-preview h3) {
    @apply font-display text-2xl font-bold mt-4 mb-2;
  }
  
  :global(.markdown-preview p) {
    @apply mb-4 leading-relaxed;
  }
  
  :global(.markdown-preview code) {
    @apply bg-gray-100 px-2 py-1 rounded text-sm font-mono;
  }
  
  :global(.markdown-preview pre) {
    @apply bg-gray-900 text-gray-100 p-4 rounded-md overflow-x-auto mb-4;
  }
  
  :global(.markdown-preview pre code) {
    @apply bg-transparent p-0 text-gray-100;
  }
  
  :global(.markdown-preview img) {
    @apply rounded-md shadow-md my-6 max-w-full;
  }
  
  :global(.markdown-preview a) {
    @apply text-gray-900 hover:underline;
  }
  
  :global(.markdown-preview ul, .markdown-preview ol) {
    @apply mb-4 pl-6;
  }
  
  :global(.markdown-preview li) {
    @apply mb-2;
  }
  
  :global(.mermaid-container) {
    @apply flex justify-center overflow-x-auto my-6;
  }
</style>

