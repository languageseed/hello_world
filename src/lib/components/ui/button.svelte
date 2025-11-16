<script lang="ts">
  import { cn } from '$lib/utils/cn';

  type ButtonVariant = 'default' | 'destructive' | 'outline' | 'secondary' | 'ghost' | 'link';
  type ButtonSize = 'default' | 'sm' | 'lg' | 'icon';

  export let variant: ButtonVariant = 'default';
  export let size: ButtonSize = 'default';
  $: className = $$props.class || '';

  const variants = {
    default: 'bg-gray-900 text-white hover:bg-gray-800',
    destructive: 'bg-gray-700 text-white hover:bg-gray-600',
    outline: 'border border-gray-300 bg-white hover:bg-gray-50 hover:text-gray-900',
    secondary: 'bg-gray-200 text-gray-900 hover:bg-gray-300',
    ghost: 'hover:bg-gray-100 hover:text-gray-900',
    link: 'text-gray-900 underline-offset-4 hover:underline'
  };

  const sizes = {
    default: 'h-10 px-4 py-2',
    sm: 'h-9 px-3',
    lg: 'h-11 px-8',
    icon: 'h-10 w-10'
  };
</script>

<button
  class={cn(
    'inline-flex items-center justify-center rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50',
    variants[variant],
    sizes[size],
    className
  )}
>
  <slot />
</button>

