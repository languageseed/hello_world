<script lang="ts">
  import { cn } from '$lib/utils/cn';

  export let value: number[] = [0];
  export let min: number = 0;
  export let max: number = 100;
  export let step: number = 1;
  export let onValueChange: ((value: number[]) => void) | undefined = undefined;
  $: className = $$props.class || '';

  function handleInput(e: Event) {
    const target = e.target as HTMLInputElement;
    const newValue = [Number(target.value)];
    value = newValue;
    onValueChange?.(newValue);
  }
</script>

<input
  type="range"
  min={min}
  max={max}
  step={step}
  value={value[0]}
  oninput={handleInput}
  class={cn('w-full h-2 bg-muted rounded-md appearance-none cursor-pointer', className)}
/>

