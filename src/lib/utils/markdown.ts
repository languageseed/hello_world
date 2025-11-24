import { marked } from 'marked';

export interface AudioTag {
  src: string;
  title: string;
  description?: string;
  position: number; // Position in the content
}

export interface CarouselData {
  images: Array<{ src: string; alt: string; caption?: string }>;
  position: number;
}

export function processMarkdown(content: string): {
  html: string;
  audioTags: AudioTag[];
  carousels: CarouselData[];
} {
  const audioTags: AudioTag[] = [];
  const carousels: CarouselData[] = [];
  
  // Extract carousel tags first
  // Format: <carousel>image1.png|Alt text|Caption;image2.png|Alt text 2|Caption 2</carousel>
  const carouselRegex = /<carousel>([\s\S]*?)<\/carousel>/g;
  let carouselMatch;
  let processedContent = content;
  let carouselIndex = 0;
  
  const carouselMatches: Array<{ match: RegExpMatchArray; index: number }> = [];
  
  while ((carouselMatch = carouselRegex.exec(content)) !== null) {
    carouselMatches.push({ match: carouselMatch, index: carouselMatch.index });
  }
  
  // Process carousels in reverse order
  carouselMatches.reverse().forEach(({ match, index }) => {
    const carouselContent = match[1].trim();
    const imageEntries = carouselContent.split(';').map(entry => entry.trim()).filter(Boolean);
    
    const images = imageEntries.map(entry => {
      const parts = entry.split('|').map(p => p.trim());
      return {
        src: parts[0].replace('../images/', '/images/'),
        alt: parts[1] || '',
        caption: parts[2]
      };
    });
    
    carousels.unshift({
      images,
      position: index
    });
    
    // Replace with placeholder
    processedContent = processedContent.substring(0, index) + 
      `\n\n<!--CAROUSEL_${carouselMatches.length - 1 - carouselIndex}-->\n\n` + 
      processedContent.substring(index + match[0].length);
    
    carouselIndex++;
  });
  
  // Extract audio tags before processing markdown
  // But exclude audio tags inside code blocks (```code blocks or indented code)
  const audioRegex = /<audio src="([^"]+)"[^>]*data-title="([^"]*)"[^>]*><\/audio>/g;
  let match;
  let audioIndex = 0;
  
  // Find all audio tags and their positions, but exclude those in code blocks
  const matches: Array<{ match: RegExpMatchArray; index: number }> = [];
  
  // Check if a position is inside a code block
  const isInCodeBlock = (pos: number, content: string): boolean => {
    const beforePos = content.substring(0, pos);
    // Check for markdown code blocks (```)
    const codeBlockMatches = beforePos.match(/```/g);
    if (codeBlockMatches && codeBlockMatches.length % 2 !== 0) {
      return true; // Inside a code block
    }
    // Check for indented code blocks (4+ spaces at start of line)
    const lines = beforePos.split('\n');
    const currentLine = lines[lines.length - 1];
    if (currentLine.match(/^    /)) {
      return true; // Inside indented code block
    }
    return false;
  };
  
  while ((match = audioRegex.exec(processedContent)) !== null) {
    // Only add if not inside a code block
    if (!isInCodeBlock(match.index, processedContent)) {
      matches.push({ match, index: match.index });
    }
  }
  
  // Process in reverse order to maintain indices when replacing text
  matches.reverse().forEach(({ match, index }) => {
    const src = match[1].replace('../audio/', '/audio/');
    const title = match[2] || `Track ${audioIndex + 1}`;
    
    // Use the ORIGINAL match index for the marker, not audioIndex
    const markerIndex = matches.length - 1 - audioIndex;
    
    audioTags.unshift({ 
      src, 
      title,
      position: index 
    });
    
    // Replace with placeholder that will survive markdown processing
    processedContent = processedContent.substring(0, index) + 
      `\n\n<!--AUDIO_${markerIndex}-->\n\n` + 
      processedContent.substring(index + match[0].length);
    
    audioIndex++;
  });
  
  // Process markdown
  marked.setOptions({
    breaks: true,
    gfm: true
  });
  
  let html = marked.parse(processedContent);
  
  // Replace placeholders with markers that we can find in the rendered HTML
  audioTags.forEach((tag, index) => {
    html = html.replace(
      new RegExp(`<!--AUDIO_${index}-->`, 'g'),
      `<div data-audio-marker="${index}" style="display:none;"></div>`
    );
  });
  
  carousels.forEach((carousel, index) => {
    html = html.replace(
      new RegExp(`<!--CAROUSEL_${index}-->`, 'g'),
      `<div data-carousel-marker="${index}" style="display:none;"></div>`
    );
  });
  
  return { html, audioTags, carousels };
}

