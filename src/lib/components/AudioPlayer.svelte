<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  import { Howl } from 'howler';
  import { base } from '$app/paths';
  import Button from './ui/button.svelte';
  import Slider from './ui/slider.svelte';
  import Card from './ui/card.svelte';
  import CardHeader from './ui/card-header.svelte';
  import CardTitle from './ui/card-title.svelte';
  import CardContent from './ui/card-content.svelte';
  import { Play, Pause, Volume2, VolumeX } from 'lucide-svelte';

  interface AudioPlayerProps {
    src: string;
    title: string;
    description?: string;
  }

  export let src: string;
  export let title: string;
  export let description: string = '';

  let sound: Howl | null = null;
  let playing = false;
  let progress: number[] = [0];
  let duration = 0;
  let currentTime = 0;
  let volume: number[] = [100];
  let muted = false;

  // Resolve audio path with base path and properly encode URL segments
  $: audioSrc = (() => {
    // Build the full path
    const fullPath = src.startsWith('/') ? `${base}${src}` : `${base}/${src}`;
    // Split path and encode each segment (handles spaces in filenames)
    const segments = fullPath.split('/').filter(s => s);
    // Encode each segment to handle spaces and special characters
    const encoded = segments.map(seg => encodeURIComponent(seg));
    return '/' + encoded.join('/');
  })();

  let loadError = false;

  onMount(() => {
    sound = new Howl({
      src: [audioSrc],
      html5: true,
      onload: () => {
        duration = sound?.duration() || 0;
      },
      onplay: () => {
        playing = true;
        updateProgress();
      },
      onpause: () => {
        playing = false;
      },
      onend: () => {
        playing = false;
        progress = [0];
        currentTime = 0;
      },
      onloaderror: (id, error) => {
        console.warn(`Failed to load audio: ${audioSrc}`, error);
        loadError = true;
      },
      onerror: (id, error) => {
        console.warn(`Audio error: ${audioSrc}`, error);
        loadError = true;
      }
    });
  });

  onDestroy(() => {
    sound?.unload();
  });

  function updateProgress() {
    if (!sound || !playing) return;
    
    const seek = sound.seek() as number;
    currentTime = seek;
    progress = [(seek / duration) * 100];
    
    if (playing) {
      requestAnimationFrame(updateProgress);
    }
  }

  function togglePlay() {
    if (!sound) return;
    
    if (playing) {
      sound.pause();
    } else {
      sound.play();
    }
  }

  function handleSeek(value: number[]) {
    if (!sound) return;
    const seekTime = (value[0] / 100) * duration;
    sound.seek(seekTime);
    currentTime = seekTime;
    progress = value;
  }

  function toggleMute() {
    if (!sound) return;
    muted = !muted;
    sound.volume(muted ? 0 : volume[0] / 100);
  }

  function formatTime(seconds: number): string {
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  }
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

