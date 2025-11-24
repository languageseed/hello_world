<script lang="ts">
  import { onMount } from 'svelte';
  
  export let images: { src: string; alt: string; caption?: string }[] = [];
  
  let currentIndex = 0;
  let autoplay = true;
  let interval: NodeJS.Timeout;
  
  function nextSlide() {
    currentIndex = (currentIndex + 1) % images.length;
  }
  
  function prevSlide() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
  }
  
  function goToSlide(index: number) {
    currentIndex = index;
  }
  
  function toggleAutoplay() {
    autoplay = !autoplay;
  }
  
  onMount(() => {
    if (autoplay) {
      interval = setInterval(nextSlide, 4000);
    }
    
    return () => {
      if (interval) clearInterval(interval);
    };
  });
  
  $: if (autoplay && !interval) {
    interval = setInterval(nextSlide, 4000);
  } else if (!autoplay && interval) {
    clearInterval(interval);
    interval = undefined as any;
  }
</script>

<div class="carousel-container">
  <div class="carousel-wrapper">
    <!-- Main image display -->
    <div class="carousel-slides">
      {#each images as image, index}
        <div 
          class="carousel-slide" 
          class:active={index === currentIndex}
        >
          <img src={image.src} alt={image.alt} />
          {#if image.caption}
            <div class="carousel-caption">{image.caption}</div>
          {/if}
        </div>
      {/each}
    </div>
    
    <!-- Navigation arrows -->
    <button class="carousel-button prev" on:click={prevSlide} aria-label="Previous slide">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="15 18 9 12 15 6"></polyline>
      </svg>
    </button>
    <button class="carousel-button next" on:click={nextSlide} aria-label="Next slide">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="9 18 15 12 9 6"></polyline>
      </svg>
    </button>
  </div>
  
  <!-- Dots navigation -->
  <div class="carousel-dots">
    {#each images as _, index}
      <button 
        class="carousel-dot" 
        class:active={index === currentIndex}
        on:click={() => goToSlide(index)}
        aria-label={`Go to slide ${index + 1}`}
      ></button>
    {/each}
  </div>
  
  <!-- Autoplay toggle -->
  <div class="carousel-controls">
    <button class="autoplay-toggle" on:click={toggleAutoplay}>
      {autoplay ? '⏸' : '▶'} {autoplay ? 'Pause' : 'Play'}
    </button>
  </div>
</div>

<style>
  .carousel-container {
    width: 100%;
    max-width: 900px;
    margin: 2rem auto;
  }
  
  .carousel-wrapper {
    position: relative;
    width: 100%;
    aspect-ratio: 16 / 9;
    overflow: hidden;
    border-radius: 12px;
    background: #1a1a1a;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  }
  
  .carousel-slides {
    position: relative;
    width: 100%;
    height: 100%;
  }
  
  .carousel-slide {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: 0;
    transition: opacity 0.5s ease-in-out;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  
  .carousel-slide.active {
    opacity: 1;
  }
  
  .carousel-slide img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
  }
  
  .carousel-caption {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: rgba(0, 0, 0, 0.7);
    color: white;
    padding: 1rem;
    text-align: center;
    font-size: 0.9rem;
  }
  
  .carousel-button {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(0, 0, 0, 0.5);
    color: white;
    border: none;
    width: 48px;
    height: 48px;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.2s;
    z-index: 10;
  }
  
  .carousel-button:hover {
    background: rgba(0, 0, 0, 0.8);
  }
  
  .carousel-button.prev {
    left: 1rem;
  }
  
  .carousel-button.next {
    right: 1rem;
  }
  
  .carousel-dots {
    display: flex;
    justify-content: center;
    gap: 0.5rem;
    margin-top: 1rem;
  }
  
  .carousel-dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: #ccc;
    border: none;
    cursor: pointer;
    transition: background 0.2s;
  }
  
  .carousel-dot.active {
    background: #333;
  }
  
  .carousel-dot:hover {
    background: #666;
  }
  
  .carousel-controls {
    display: flex;
    justify-content: center;
    margin-top: 1rem;
  }
  
  .autoplay-toggle {
    padding: 0.5rem 1rem;
    background: #f0f0f0;
    border: 1px solid #ccc;
    border-radius: 6px;
    cursor: pointer;
    font-size: 0.9rem;
    transition: background 0.2s;
  }
  
  .autoplay-toggle:hover {
    background: #e0e0e0;
  }
  
  @media (max-width: 640px) {
    .carousel-button {
      width: 36px;
      height: 36px;
    }
    
    .carousel-button.prev {
      left: 0.5rem;
    }
    
    .carousel-button.next {
      right: 0.5rem;
    }
    
    .carousel-caption {
      font-size: 0.8rem;
      padding: 0.75rem;
    }
  }
</style>

