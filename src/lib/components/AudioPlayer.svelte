<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  import { base } from '$app/paths';
  import Button from './ui/button.svelte';
  import Slider from './ui/slider.svelte';
  import Card from './ui/card.svelte';
  import CardHeader from './ui/card-header.svelte';
  import CardTitle from './ui/card-title.svelte';
  import CardContent from './ui/card-content.svelte';
  import { Play, Pause, Volume2, VolumeX } from 'lucide-svelte';
  import { currentPlayingId } from '$lib/stores/audioStore';
  import { get } from 'svelte/store';

  interface AudioPlayerProps {
    src: string;
    title: string;
    description?: string;
  }

  export let src: string;
  export let title: string;
  export let description: string = '';

  // Generate unique ID for this player instance
  const playerId = `audio-${Math.random().toString(36).substr(2, 9)}`;

  let audioElement: HTMLAudioElement;
  let playing = false;
  let progress: number[] = [0];
  let duration = 0;
  let currentTime = 0;
  let volume: number[] = [100];
  let muted = false;
  let loadError = false;

  // Resolve audio path with base path and properly encode URL segments
  $: audioSrc = (() => {
    // Always use /hello_world as base path for GitHub Pages
    const basePath = '/hello_world';
    const fullPath = src.startsWith('/') ? `${basePath}${src}` : `${basePath}/${src}`;
    const segments = fullPath.split('/').filter(s => s);
    const encoded = segments.map((seg) => {
      if (seg.includes(' ') || seg.includes('%') || seg.match(/[^a-zA-Z0-9._-]/)) {
        return encodeURIComponent(seg);
      }
      return seg;
    });
    const result = '/' + encoded.join('/');
    return result;
  })();

  function updateProgress() {
    if (!audioElement || !playing) return;
    
    currentTime = audioElement.currentTime;
    if (duration > 0) {
      progress = [(currentTime / duration) * 100];
    }
    
    if (playing && !audioElement.paused) {
      requestAnimationFrame(updateProgress);
    }
  }

  function togglePlay() {
    if (!audioElement) return;
    
    const currentId = get(currentPlayingId);
    
    // If another audio is playing, pause it
    if (currentId && currentId !== playerId) {
      currentPlayingId.set(null);
    }
    
    if (playing) {
      audioElement.pause();
      playing = false;
      currentPlayingId.set(null);
    } else {
      // Set this as the currently playing audio
      currentPlayingId.set(playerId);
      audioElement.play().then(() => {
        playing = true;
        updateProgress();
      }).catch((error) => {
        console.error('Play failed:', error);
        loadError = true;
        currentPlayingId.set(null);
      });
    }
  }

  function handleSeek(value: number[]) {
    if (!audioElement || duration === 0) return;
    const seekTime = (value[0] / 100) * duration;
    audioElement.currentTime = seekTime;
    currentTime = seekTime;
    progress = value;
  }

  function toggleMute() {
    if (!audioElement) return;
    muted = !muted;
    audioElement.muted = muted;
    if (!muted) {
      audioElement.volume = volume[0] / 100;
    }
  }

  function formatTime(seconds: number): string {
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  }

  // Subscribe to currentPlayingId changes to pause if another audio starts
  const unsubscribe = currentPlayingId.subscribe((currentId) => {
    if (currentId !== playerId && playing && audioElement) {
      audioElement.pause();
      playing = false;
    }
  });

  // Update audio src when audioSrc changes
  $: if (audioElement && audioSrc) {
    console.log('Setting audio src:', audioSrc);
    audioElement.src = audioSrc;
    loadError = false;
  }

  onMount(() => {
    if (audioElement) {
      // Set src explicitly
      audioElement.src = audioSrc;
      console.log('Audio element mounted with src:', audioSrc, 'base:', base);
      
      audioElement.addEventListener('loadedmetadata', () => {
        duration = audioElement.duration || 0;
        console.log('Audio metadata loaded:', { duration, audioSrc, actualSrc: audioElement.src });
      });

      audioElement.addEventListener('timeupdate', () => {
        if (playing) {
          currentTime = audioElement.currentTime;
          if (duration > 0) {
            progress = [(currentTime / duration) * 100];
          }
        }
      });

      audioElement.addEventListener('ended', () => {
        playing = false;
        progress = [0];
        currentTime = 0;
        currentPlayingId.set(null);
      });

      audioElement.addEventListener('error', (e) => {
        console.error('Audio error:', e, 'src:', audioElement.src, 'audioSrc:', audioSrc, 'base:', base);
        loadError = true;
      });

      audioElement.addEventListener('pause', () => {
        playing = false;
        const currentId = get(currentPlayingId);
        if (currentId === playerId) {
          currentPlayingId.set(null);
        }
      });

      audioElement.addEventListener('play', () => {
        playing = true;
        updateProgress();
      });

      // Set initial volume
      audioElement.volume = volume[0] / 100;
    }
  });

  onDestroy(() => {
    unsubscribe();
    const currentId = get(currentPlayingId);
    if (currentId === playerId) {
      currentPlayingId.set(null);
    }
    if (audioElement) {
      audioElement.pause();
      audioElement.src = '';
    }
  });
</script>

<Card class="mb-6">
  <CardHeader>
    <CardTitle class="flex items-center gap-2">
      <span>{title}</span>
    </CardTitle>
    {#if description}
      <p class="text-sm text-gray-600 mt-2">{description}</p>
    {/if}
  </CardHeader>
  <CardContent>
    {#if loadError}
      <p class="text-sm text-gray-600 italic">This audio file is not available.</p>
    {:else}
      <!-- Hidden audio element -->
      <audio
        bind:this={audioElement}
        src={audioSrc}
        preload="metadata"
        style="display: none;"
        on:error={(e) => {
          console.error('Audio element error:', e, 'src:', audioSrc, 'base:', base);
          loadError = true;
        }}
      ></audio>
      
      <div class="flex items-center gap-4">
        <Button variant="default" size="icon" on:click={togglePlay}>
          {#if playing}
            <Pause class="w-5 h-5" />
          {:else}
            <Play class="w-5 h-5" />
          {/if}
        </Button>
        
        <div class="flex-1">
          <Slider
            value={progress}
            min={0}
            max={100}
            step={0.1}
            onValueChange={handleSeek}
            class="mb-2"
          />
          <div class="flex justify-between text-xs text-gray-600">
            <span>{formatTime(currentTime)}</span>
            <span>{formatTime(duration)}</span>
          </div>
        </div>
        
        <Button variant="ghost" size="icon" on:click={toggleMute}>
          {#if muted}
            <VolumeX class="w-5 h-5" />
          {:else}
            <Volume2 class="w-5 h-5" />
          {/if}
        </Button>
      </div>
    {/if}
  </CardContent>
</Card>
