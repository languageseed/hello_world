<script lang="ts">
  import { Github, Linkedin, Mail, Heart, Sprout } from 'lucide-svelte';
  import { base } from '$app/paths';
  
  const currentYear = new Date().getFullYear();
  
  const socialLinks = [
    { href: 'https://github.com/languageseed', icon: Github, label: 'GitHub' },
    { href: '#', icon: Linkedin, label: 'LinkedIn' },
    { href: '#', icon: Mail, label: 'Email' },
  ];
  
  const footerLinks = [
    { label: 'Home', href: `${base}/` },
    { label: 'Portfolio', href: `${base}/` },
    { label: 'Blog', href: `${base}/` },
    { label: 'Scratchpad', href: `${base}/merman` },
  ];
</script>

<footer class="relative mt-24 border-t border-border bg-card/50">
  <!-- Gradient accent line -->
  <div class="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-primary/50 to-transparent" />
  
  <div class="max-w-7xl mx-auto px-6 py-12">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
      <!-- Brand -->
      <div class="space-y-4">
        <a href="{base}/" class="flex items-center gap-3 group w-fit">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-400 to-cyan-600 
                      flex items-center justify-center shadow-lg shadow-cyan-500/20">
            <Sprout class="w-5 h-5 text-white" />
          </div>
          <span class="font-mono text-lg font-bold">hello_world</span>
        </a>
        <p class="text-muted-foreground text-sm leading-relaxed max-w-xs">
          Notes to self, articles and content to share with others. 
          Building AI systems and sharing knowledge.
        </p>
      </div>
      
      <!-- Links -->
      <div class="space-y-4">
        <h3 class="font-display font-semibold text-foreground">Navigation</h3>
        <nav class="flex flex-col gap-2">
          {#each footerLinks as link}
            <a 
              href={link.href}
              class="text-muted-foreground hover:text-foreground text-sm transition-colors w-fit"
            >
              {link.label}
            </a>
          {/each}
        </nav>
      </div>
      
      <!-- Social & Tech -->
      <div class="space-y-4">
        <h3 class="font-display font-semibold text-foreground">Connect</h3>
        <div class="flex gap-3">
          {#each socialLinks as social}
            <a
              href={social.href}
              target="_blank"
              rel="noopener noreferrer"
              class="w-10 h-10 rounded-lg bg-secondary/50 flex items-center justify-center
                     text-muted-foreground hover:text-foreground hover:bg-secondary
                     transition-all duration-200"
              aria-label={social.label}
            >
              <svelte:component this={social.icon} class="w-5 h-5" />
            </a>
          {/each}
        </div>
        <div class="flex flex-wrap gap-2 pt-2">
          <span class="tag text-xs">SvelteKit</span>
          <span class="tag text-xs">Tailwind</span>
          <span class="tag text-xs">shadcn</span>
        </div>
      </div>
    </div>
    
    <!-- Bottom bar -->
    <div class="mt-12 pt-8 border-t border-border flex flex-col sm:flex-row items-center justify-between gap-4">
      <p class="text-muted-foreground text-sm">
        © {currentYear} Language Seed. All rights reserved.
      </p>
      <p class="text-muted-foreground text-sm flex items-center gap-1.5">
        Built with <Heart class="w-4 h-4 text-red-500 fill-red-500" /> using SvelteKit
      </p>
    </div>
  </div>
</footer>
