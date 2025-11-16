<script lang="ts">
  import { cn } from '$lib/utils/cn';

  $: className = $$props.class || '';
</script>

<p class={cn('text-sm text-muted-foreground', className)}>
  <slot />
</p>

