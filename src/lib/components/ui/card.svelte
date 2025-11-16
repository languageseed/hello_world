<script lang="ts">
  import { cn } from '$lib/utils/cn';

  $: className = $$props.class || '';
</script>

<div class={cn('rounded-md border bg-card text-card-foreground shadow-sm', className)}>
  <slot />
</div>

