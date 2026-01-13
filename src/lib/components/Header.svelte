<script lang="ts">
  import { Github, Sprout, Pencil, Moon, Sun, Menu, X, Folder, BookOpen, User } from 'lucide-svelte';
  import { base } from '$app/paths';
  import { browser } from '$app/environment';
  import { onMount } from 'svelte';
  
  let darkMode = false;
  let mobileMenuOpen = false;
  let scrolled = false;
  
  onMount(() => {
    // Check for saved preference or system preference
    if (browser) {
      const saved = localStorage.getItem('theme');
      if (saved === 'dark' || (!saved && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        darkMode = true;
        document.documentElement.classList.add('dark');
      }
      
      // Handle scroll
      const handleScroll = () => {
        scrolled = window.scrollY > 20;
      };
      window.addEventListener('scroll', handleScroll);
      return () => window.removeEventListener('scroll', handleScroll);
    }
  });
  
  function toggleDarkMode() {
    darkMode = !darkMode;
    if (browser) {
      if (darkMode) {
        document.documentElement.classList.add('dark');
        localStorage.setItem('theme', 'dark');
      } else {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('theme', 'light');
      }
    }
  }
  
  function toggleMobileMenu() {
    mobileMenuOpen = !mobileMenuOpen;
  }
  
  const navLinks = [
    { href: `${base}/`, label: 'Portfolio', icon: Folder },
    { href: `${base}/blog`, label: 'Blog', icon: BookOpen },
    { href: `${base}/about`, label: 'About', icon: User },
  ];
</script>

<header 
  class="sticky top-0 z-50 transition-all duration-300"
  class:scrolled
>
  <div class="absolute inset-0 bg-background/80 backdrop-blur-xl border-b border-border/50" />
  
  <div class="relative max-w-7xl mx-auto px-6">
    <div class="flex items-center justify-between h-16">
      <!-- Logo -->
      <a href="{base}/" class="flex items-center gap-3 group">
        <div class="relative">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-400 to-cyan-600 
                      flex items-center justify-center shadow-lg shadow-cyan-500/25
                      group-hover:shadow-cyan-500/40 transition-all duration-300
                      group-hover:scale-105">
            <Sprout class="w-5 h-5 text-white" />
          </div>
          <!-- Glow effect -->
          <div class="absolute inset-0 rounded-xl bg-cyan-400/20 blur-xl 
                      opacity-0 group-hover:opacity-100 transition-opacity" />
        </div>
        <div class="flex flex-col">
          <span class="font-mono text-lg font-bold tracking-tight text-foreground">hello_world</span>
          <span class="text-xs text-foreground/60 -mt-1 hidden sm:block">by Language Seed</span>
        </div>
      </a>
      
      <!-- Desktop Navigation -->
      <nav class="hidden md:flex items-center gap-1">
        {#each navLinks as link}
          <a 
            href={link.href}
            class="flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium
                   text-foreground/90 hover:text-primary hover:bg-secondary/50
                   transition-all duration-200"
          >
            <svelte:component this={link.icon} class="w-4 h-4" />
            {link.label}
          </a>
        {/each}
      </nav>
      
      <!-- Right side actions -->
      <div class="flex items-center gap-2">
        <!-- GitHub -->
        <a
          href="https://github.com/languageseed/hello_world"
          target="_blank"
          rel="noopener noreferrer"
          class="hidden sm:flex items-center gap-2 px-3 py-2 rounded-lg text-sm
                 text-foreground/80 hover:text-primary hover:bg-secondary/50
                 transition-all duration-200"
        >
          <Github class="w-4 h-4" />
          <span class="hidden lg:inline">GitHub</span>
        </a>
        
        <!-- Theme toggle -->
        <button
          on:click={toggleDarkMode}
          class="w-9 h-9 rounded-lg flex items-center justify-center
                 text-foreground/80 hover:text-primary hover:bg-secondary/50
                 transition-all duration-200"
          aria-label="Toggle dark mode"
        >
          {#if darkMode}
            <Sun class="w-5 h-5" />
          {:else}
            <Moon class="w-5 h-5" />
          {/if}
        </button>
        
        <!-- Mobile menu button -->
        <button
          on:click={toggleMobileMenu}
          class="md:hidden w-9 h-9 rounded-lg flex items-center justify-center
                 text-foreground/80 hover:text-primary hover:bg-secondary/50
                 transition-all duration-200"
          aria-label="Toggle menu"
        >
          {#if mobileMenuOpen}
            <X class="w-5 h-5" />
          {:else}
            <Menu class="w-5 h-5" />
          {/if}
        </button>
      </div>
    </div>
  </div>
  
  <!-- Mobile menu -->
  {#if mobileMenuOpen}
    <div class="md:hidden absolute top-full left-0 right-0 bg-background/95 backdrop-blur-xl 
                border-b border-border shadow-xl animate-fade-in">
      <nav class="max-w-7xl mx-auto px-6 py-4 flex flex-col gap-1">
        {#each navLinks as link}
          <a 
            href={link.href}
            on:click={() => mobileMenuOpen = false}
            class="flex items-center gap-3 px-4 py-3 rounded-lg text-base font-medium
                   text-muted-foreground hover:text-foreground hover:bg-secondary/50
                   transition-all duration-200"
          >
            <svelte:component this={link.icon} class="w-5 h-5" />
            {link.label}
          </a>
        {/each}
        <hr class="my-2 border-border" />
        <a
          href="https://github.com/languageseed/hello_world"
          target="_blank"
          rel="noopener noreferrer"
          class="flex items-center gap-3 px-4 py-3 rounded-lg text-base font-medium
                 text-muted-foreground hover:text-foreground hover:bg-secondary/50
                 transition-all duration-200"
        >
          <Github class="w-5 h-5" />
          View on GitHub
        </a>
      </nav>
    </div>
  {/if}
</header>

<style>
  .scrolled {
    @apply shadow-sm;
  }
</style>
