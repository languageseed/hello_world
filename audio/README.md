# 🎵 Audio Files

Store your audio files here for use in blog posts.

## Supported Formats

Howler.js automatically handles browser compatibility. Upload in these formats:

- **MP3** (.mp3) - Best compatibility
- **WebM** (.webm) - Modern browsers
- **OGG** (.ogg) - Firefox, Chrome
- **WAV** (.wav) - Uncompressed (large files)
- **AAC** (.aac) - Apple devices
- **FLAC** (.flac) - Lossless audio

**Recommendation:** Use MP3 for best compatibility across all browsers and devices.

## File Size Recommendations

- **Short clips** (< 1 min): < 1 MB
- **Music tracks** (3-5 min): 3-8 MB (128-192 kbps MP3)
- **Podcasts/long form**: Consider external hosting for files > 25 MB

## Using Audio in Your Posts

### Basic Audio Player

In your markdown file, use HTML5 audio tag:

```markdown
<audio src="../audio/my-song.mp3" data-title="My Song Title"></audio>
```

### With Custom Title

```markdown
<audio src="../audio/podcast-ep1.mp3" data-title="Episode 1: Introduction to Blogging"></audio>
```

### Multiple Audio Files

```markdown
## My Favorite Tracks

<audio src="../audio/track1.mp3" data-title="Track 1: Morning Vibes"></audio>

<audio src="../audio/track2.mp3" data-title="Track 2: Afternoon Groove"></audio>

<audio src="../audio/track3.mp3" data-title="Track 3: Evening Chill"></audio>
```

## Features

Your audio players automatically get:

- ✅ **Play/Pause** button
- ✅ **Progress bar** (clickable to seek)
- ✅ **Time display** (current/total)
- ✅ **Volume control** (clickable icon + slider)
- ✅ **Beautiful design** matching your blog theme
- ✅ **Mobile responsive**
- ✅ **Keyboard shortcuts** (space to play/pause)

## Example Post Structure

```markdown
---
title: My Music Collection
author: language seed
date: 2025-11-13
---

# My Music Collection

Here are some tracks I've been working on.

## Track 1: Sunrise

<audio src="../audio/sunrise.mp3" data-title="Sunrise - Original Composition"></audio>

This track was inspired by early morning walks...

## Track 2: City Lights

<audio src="../audio/city-lights.mp3" data-title="City Lights - Electronic Mix"></audio>

An upbeat electronic piece...
```

## Optimizing Audio Files

Before uploading, optimize your audio:

### Using FFmpeg (Command Line)

```bash
# Convert to optimized MP3 (192 kbps)
ffmpeg -i input.wav -codec:a libmp3lame -b:a 192k output.mp3

# Convert to smaller MP3 (128 kbps, good for speech)
ffmpeg -i input.wav -codec:a libmp3lame -b:a 128k output.mp3

# Convert to WebM (modern format)
ffmpeg -i input.wav -codec:a libopus -b:a 128k output.webm
```

### Using Online Tools

- [CloudConvert](https://cloudconvert.com/mp3-converter) - Free online converter
- [Online Audio Converter](https://online-audio-converter.com/) - Simple interface
- [Audacity](https://www.audacityteam.org/) - Free desktop software

## GitHub File Size Limits

- Individual file max: **100 MB**
- Recommended per file: **< 25 MB**
- Repository max: **5 GB**

For larger audio files or full albums, consider:
- External hosting (SoundCloud, Bandcamp)
- Git LFS (Large File Storage)
- CDN storage (Cloudflare R2, AWS S3)

## External Hosting Example

If hosting elsewhere, just update the src:

```markdown
<audio src="https://yourdomain.com/audio/track.mp3" data-title="My Track"></audio>
```

## Tips

1. **Name files clearly**: `2025-11-13-podcast-episode-1.mp3`
2. **Use lowercase**: Easier to reference
3. **No spaces**: Use hyphens instead `my-song.mp3` not `my song.mp3`
4. **Organize by date**: Create subdirectories if needed
5. **Test locally**: Always test before pushing to GitHub

## Audio Player Features

### Keyboard Shortcuts (when player focused)
- **Space**: Play/Pause
- **Arrow Left**: Seek backward
- **Arrow Right**: Seek forward
- **M**: Mute/Unmute

### Mobile Support
- Touch-friendly controls
- Responsive design
- Works on iOS and Android

## Troubleshooting

### Audio won't play
- Check file path is correct (`../audio/filename.mp3`)
- Ensure file is actually in `audio/` folder
- Verify file extension matches actual format
- Check browser console for errors

### Player not showing
- Make sure `<audio>` tag has `src` attribute
- Check that Howler.js loaded (view page source)
- Try hard refresh (Cmd+Shift+R / Ctrl+Shift+R)

### File too large for GitHub
- Compress the audio file
- Use external hosting
- Enable Git LFS for your repository

---

**Happy listening! 🎧**

