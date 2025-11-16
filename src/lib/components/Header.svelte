<script lang="ts">
  import { Github, Sprout } from 'lucide-svelte';
  import Button from './ui/button.svelte';
</script>

<header class="bg-gray-900 text-white py-6 px-6 text-center shadow-md">
  <h1 class="font-display text-3xl font-bold mb-2 tracking-tight flex items-center justify-center gap-2">
    <Sprout class="w-8 h-8" />
    Hello World
  </h1>
  <p class="text-sm opacity-90 font-normal max-w-2xl mx-auto">
    Notes to self, articles and content to share with others
  </p>
  <div class="mt-2">
    <a
      href="https://github.com/languageseed/hello_world"
      target="_blank"
      rel="noopener noreferrer"
      class="inline-flex items-center gap-2 px-4 py-2 text-sm bg-white/10 rounded-md transition-all hover:bg-white/20"
    >
      <Github class="w-5 h-5" />
      View on GitHub
    </a>
  </div>
</header>

