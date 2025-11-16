import { marked } from 'marked';

export interface AudioTag {
  src: string;
  title: string;
  description?: string;
  position: number; // Position in the content
}

export function processMarkdown(content: string): {
  html: string;
  audioTags: AudioTag[];
} {
  const audioTags: AudioTag[] = [];
  
  // Extract audio tags before processing markdown
  const audioRegex = /<audio src="([^"]+)"[^>]*data-title="([^"]*)"[^>]*><\/audio>/g;
  let match;
  let processedContent = content;
  let audioIndex = 0;
  
  // Find all audio tags and their positions
  const matches: Array<{ match: RegExpMatchArray; index: number }> = [];
  let searchIndex = 0;
  
  while ((match = audioRegex.exec(content)) !== null) {
    matches.push({ match, index: match.index });
  }
  
  // Process in reverse order to maintain indices
  matches.reverse().forEach(({ match, index }) => {
    const src = match[1].replace('../audio/', '/audio/');
    const title = match[2] || `Track ${audioIndex + 1}`;
    
    audioTags.unshift({ 
      src, 
      title,
      position: index 
    });
    
    // Replace with placeholder that will survive markdown processing
    processedContent = processedContent.substring(0, index) + 
      `\n\n<!--AUDIO_${audioIndex}-->\n\n` + 
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
  
  return { html, audioTags };
}

