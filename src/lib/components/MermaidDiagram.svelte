<script lang="ts">
  import { onMount } from 'svelte';
  import mermaid from 'mermaid';

  interface MermaidDiagramProps {
    code: string;
  }

  let { code }: MermaidDiagramProps = $props();
  let container: HTMLDivElement;

  onMount(async () => {
    if (!container) return;
    
    mermaid.initialize({
      startOnLoad: false,
      theme: 'default',
      securityLevel: 'loose'
    });

    try {
      const id = `mermaid-${Math.random().toString(36).substr(2, 9)}`;
      const { svg } = await mermaid.render(id, code);
      container.innerHTML = svg;
    } catch (error) {
      console.error('Mermaid rendering error:', error);
      container.innerHTML = `<p class="text-red-500">Error rendering diagram: ${error}</p>`;
    }
  });
</script>

<div bind:this={container} class="mermaid-container my-6"></div>

<style>
  .mermaid-container {
    display: flex;
    justify-content: center;
    overflow-x: auto;
  }
  
  .mermaid-container svg {
    max-width: 100%;
    height: auto;
  }
</style>

