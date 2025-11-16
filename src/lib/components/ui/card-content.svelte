<script lang="ts">
  import { cn } from '$lib/utils/cn';

  $: className = $$props.class || '';
</script>

<div class={cn('p-6 pt-0 rounded-b-md', className)}>
  <slot />
</div>

