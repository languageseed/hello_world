<script lang="ts">
  import { page } from '$app/stores';
  import Button from '$lib/components/ui/button.svelte';
  import { base } from '$app/paths';
  import { Home } from 'lucide-svelte';
</script>

<div class="min-h-screen flex items-center justify-center px-6">
  <div class="text-center">
    <h1 class="text-6xl font-bold text-gray-900 mb-4">{$page.status}</h1>
    <p class="text-xl text-gray-600 mb-8">{$page.error?.message || 'Page not found'}</p>
    <a href="{base}/">
      <Button variant="default" size="lg">
        <Home class="w-5 h-5 mr-2" />
        Back to Home
      </Button>
    </a>
  </div>
</div>

