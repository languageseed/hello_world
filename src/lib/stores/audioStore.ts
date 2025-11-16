import { writable } from 'svelte/store';

// Store to track the currently playing audio player ID
export const currentPlayingId = writable<string | null>(null);

