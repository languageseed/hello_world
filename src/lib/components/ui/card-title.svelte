<script lang="ts">
  import { cn } from '$lib/utils/cn';

  $: className = $$props.class || '';
</script>

<h3 class={cn('text-2xl font-semibold leading-none tracking-tight', className)}>
  <slot />
</h3>

