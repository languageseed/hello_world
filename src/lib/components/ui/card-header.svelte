<script lang="ts">
  import { cn } from '$lib/utils/cn';

  $: className = $$props.class || '';
</script>

<div class={cn('flex flex-col space-y-1.5 p-6 rounded-t-md', className)}>
  <slot />
</div>

