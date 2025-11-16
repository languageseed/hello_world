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
    // Split path and encode only filename segments (not base path)
    const segments = fullPath.split('/').filter(s => s);
    // Encode segments but preserve base path structure
    // Only encode segments that contain spaces or special chars (typically filenames)
    const encoded = segments.map((seg, index) => {
      // Don't encode base path segments (first 1-2 segments)
      // Only encode if segment contains spaces or special characters
      if (seg.includes(' ') || seg.includes('%') || seg.match(/[^a-zA-Z0-9._-]/)) {
        return encodeURIComponent(seg);
      }
      return seg;
    });
    return '/' + encoded.join('/');
  })();

  let loadError = false;

  onMount(() => {
    console.log('AudioPlayer mounting:', { src, audioSrc, base });
    sound = new Howl({
      src: [audioSrc],
      html5: false, // Use Web Audio API to avoid HTML5 pool exhaustion
      preload: true, // Preload the audio file
      onload: () => {
        console.log('Audio loaded successfully:', audioSrc);
        if (sound) {
          duration = sound.duration() || 0;
          console.log('Duration set to:', duration);
        }
      },
      onplay: (id) => {
        console.log('Audio playing:', id);
        // Pause any other currently playing audio
        const currentId = get(currentPlayingId);
        if (currentId && currentId !== playerId) {
          // Another audio is playing - it will pause itself when it detects the change
          console.log('Another audio is playing, it will pause automatically');
        }
        // Set this as the currently playing audio
        currentPlayingId.set(playerId);
        playing = true;
        updateProgress();
      },
      onplayerror: (id, error) => {
        console.warn('Play error (may need unlock):', error, { id, audioSrc });
        // Handle browser audio unlock - wait for unlock event then retry
        if (sound) {
          sound.once('unlock', () => {
            console.log('Audio unlocked, retrying play');
            const soundId = sound?.play();
            if (soundId) {
              console.log('Play successful after unlock:', soundId);
            }
          });
        }
      },
      onpause: () => {
        console.log('Audio paused');
        // Clear the current playing ID if this was the active player
        const currentId = get(currentPlayingId);
        if (currentId === playerId) {
          currentPlayingId.set(null);
        }
        playing = false;
      },
      onend: () => {
        console.log('Audio ended');
        playing = false;
        progress = [0];
        currentTime = 0;
      },
      onloaderror: (id, error) => {
        console.error(`Failed to load audio: ${audioSrc}`, error, { id, src, base });
        loadError = true;
      },
      onerror: (id, error) => {
        console.error(`Audio error: ${audioSrc}`, error, { id, src, base });
        loadError = true;
      }
    });
    
    // Explicitly load the audio
    sound.load();
  });

  // Subscribe to currentPlayingId changes to pause if another audio starts
  const unsubscribe = currentPlayingId.subscribe((currentId) => {
    if (currentId !== playerId && playing && sound) {
      console.log('Another audio started, pausing this one');
      sound.pause();
      playing = false;
    }
  });

  onDestroy(() => {
    unsubscribe();
    // Clear the current playing ID if this was the active player
    const currentId = get(currentPlayingId);
    if (currentId === playerId) {
      currentPlayingId.set(null);
    }
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
    console.log('togglePlay called', { sound: !!sound, playing, duration, state: sound?.state() });
    if (!sound) {
      console.error('Sound not initialized');
      return;
    }
    
    // Check current playing state using Howler's method
    const isCurrentlyPlaying = sound.playing();
    console.log('Current playing state:', isCurrentlyPlaying);
    
    if (isCurrentlyPlaying) {
      console.log('Pausing audio');
      sound.pause();
      playing = false;
    } else {
      console.log('Attempting to play audio:', audioSrc);
      console.log('Sound state:', sound.state());
      
      // Ensure audio is loaded
      if (sound.state() === 'unloaded') {
        console.log('Audio not loaded, loading now...');
        sound.load();
        sound.once('load', () => {
          console.log('Audio loaded, playing now');
          const soundId = sound.play();
          console.log('Play after load, soundId:', soundId);
        });
        return;
      }
      
      // Try to play
      const soundId = sound.play();
      console.log('Play called, soundId:', soundId, 'state:', sound.state());
      
      if (soundId === undefined) {
        console.warn('Play returned undefined');
        // Check if we need to wait for unlock
        if (sound.state() === 'loading') {
          console.log('Audio still loading, waiting...');
          sound.once('load', () => {
            const retryId = sound.play();
            console.log('Retry play after load, soundId:', retryId);
          });
        }
      } else {
        // Play was successful, but onplay callback will set playing state
        console.log('Play initiated successfully with ID:', soundId);
      }
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

