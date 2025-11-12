# 🎵 Audio Converter Guide

## Automatic HQ MP3 Conversion Script

This script automatically converts ALL audio files in your `audio/` directory to high-quality MP3 format (320k stereo) and removes the original files.

## ✨ Features

- ✅ **Automatic conversion** - Batch process all audio files
- ✅ **HQ output** - 320k bitrate, stereo, 48kHz sample rate
- ✅ **Auto-cleanup** - Removes original files after conversion
- ✅ **Safe operation** - Dry-run mode to preview changes
- ✅ **Smart handling** - Processes subdirectories automatically
- ✅ **Multiple formats** - WAV, FLAC, AAC, OGG, WebM, M4A, AIFF, OPUS, MP3

## 📋 Requirements

### Install FFmpeg

The script requires FFmpeg to be installed:

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows:**
1. Download from https://ffmpeg.org/download.html
2. Add to PATH
3. Or use WSL/Linux subsystem

**Verify installation:**
```bash
ffmpeg -version
```

## 🚀 Usage

### Basic Usage (Interactive)

```bash
python scripts/convert_audio.py
```

**What happens:**
1. Script scans `audio/` directory
2. Shows all files that will be converted
3. Asks for confirmation
4. Converts to 320k MP3 stereo
5. Removes original files
6. Shows summary

### Dry Run (Preview Mode)

Preview what will be converted WITHOUT making changes:

```bash
python scripts/convert_audio.py --dry-run
```

**Perfect for:**
- Seeing what files will be processed
- Checking file sizes
- Testing before actual conversion

### Force Mode (No Confirmation)

Skip the confirmation prompt:

```bash
python scripts/convert_audio.py --force
```

**Use for:**
- Automated workflows
- When you're sure about conversion
- Batch processing scripts

### Help

```bash
python scripts/convert_audio.py --help
```

## 📊 Output Quality

### Settings

| Setting | Value | Why |
|---------|-------|-----|
| **Bitrate** | 320k | Maximum MP3 quality |
| **Channels** | Stereo (2) | Full stereo imaging |
| **Sample Rate** | 48kHz | Professional quality |
| **Format** | MP3 | Universal compatibility |

### Quality Comparison

| Source | Output | Quality | File Size |
|--------|--------|---------|-----------|
| WAV (uncompressed) | MP3 320k | Excellent | ~90% smaller |
| FLAC (lossless) | MP3 320k | Excellent | ~70% smaller |
| MP3 128k | MP3 320k | Upgraded | ~2.5x larger |
| AAC 256k | MP3 320k | Excellent | Similar |

## 🎯 Complete Examples

### Example 1: Convert All Audio Files

```bash
# 1. Add your audio files
cp ~/Music/*.wav audio/
cp ~/Podcasts/*.m4a audio/

# 2. Preview conversion
python scripts/convert_audio.py --dry-run

# Output:
# Found 5 audio file(s):
#   1. intro-music.wav - 45.2 MB
#   2. episode-1.m4a - 28.5 MB
#   3. background.flac - 62.1 MB
#   4. outro.aac - 12.3 MB
#   5. sample.ogg - 8.9 MB

# 3. Convert
python scripts/convert_audio.py

# 4. Confirm when prompted
# Continue? [y/N]: y

# Output:
# Converting: intro-music.wav
#   → intro-music.mp3 (320k stereo)
#   ✅ Converted: intro-music.mp3
#   🗑️  Removed: intro-music.wav
# ...
# ✅ Successful: 5
# Storage:
#   Before: 157.0 MB
#   After:  68.3 MB
#   Saved:  88.7 MB (56.5%)
```

### Example 2: Upgrade Existing MP3s

```bash
# Even existing MP3s get upgraded to 320k!
python scripts/convert_audio.py

# Output:
# Found 3 audio file(s):
#   1. podcast.mp3 - 15.2 MB (will be upgraded to 320k)
#   2. music.mp3 - 8.5 MB (will be upgraded to 320k)
#   3. speech.mp3 - 5.1 MB (will be upgraded to 320k)
```

### Example 3: Process Subdirectories

The script automatically processes all subdirectories:

```
audio/
├── 2025/
│   ├── november/
│   │   ├── file1.wav  ← Converted
│   │   └── file2.flac ← Converted
│   └── december/
│       └── file3.aac  ← Converted
├── music/
│   └── track.m4a      ← Converted
└── podcast.ogg        ← Converted
```

```bash
python scripts/convert_audio.py --force
# All files in all subdirectories are processed!
```

## 🎬 Step-by-Step Workflow

### Workflow 1: Adding New Audio

```bash
# 1. Record or download audio
# (You have: recording.wav - 100 MB)

# 2. Add to audio folder
cp recording.wav audio/

# 3. Convert to HQ MP3
python scripts/convert_audio.py --force

# Result:
# audio/recording.mp3 (35 MB, 320k stereo)
# Original recording.wav deleted
# Saved: 65 MB!
```

### Workflow 2: Batch Processing

```bash
# 1. Copy all your audio files
cp ~/Music/Album/*.flac audio/album/
# (10 FLAC files, total 450 MB)

# 2. Preview conversion
python scripts/convert_audio.py --dry-run

# 3. Convert all
python scripts/convert_audio.py

# Result:
# 10 MP3 files @ 320k, total ~160 MB
# Saved: ~290 MB (64%)
```

### Workflow 3: Podcast Optimization

```bash
# 1. Export podcast from DAW
# (episode.wav - 250 MB, 48kHz stereo)

# 2. Add to audio folder
cp episode.wav audio/podcasts/

# 3. Convert
python scripts/convert_audio.py --force

# 4. Reference in blog post
echo '<audio src="../audio/podcasts/episode.mp3" data-title="Episode 1"></audio>' >> content/podcast-post.md

# 5. Generate post
python scripts/generate_post.py content/podcast-post.md

# Result:
# Professional quality podcast @ 320k
# File size: ~90 MB (64% smaller)
# Ready for web streaming!
```

## 📈 Output Details

### What Gets Converted

**Supported input formats:**
- WAV (uncompressed)
- FLAC (lossless)
- AAC (.aac, .m4a)
- OGG Vorbis (.ogg, .oga)
- WebM (.webm)
- WMA (Windows Media)
- AIFF (Apple)
- OPUS (.opus)
- MP3 (will be upgraded to 320k)

**Output format:**
- MP3 at 320 kbps
- Stereo (2 channels)
- 48kHz sample rate

### What Gets Preserved

- ✅ **Filename** - Same name, just .mp3 extension
- ✅ **Directory structure** - Files stay in same folders
- ✅ **Metadata** - Title, artist, album tags (when possible)
- ✅ **Quality** - Maximum MP3 quality (320k)

### What Gets Removed

- 🗑️ **Original files** - After successful conversion
- 🗑️ **Low-quality versions** - Upgraded to 320k
- 🗑️ **Large file sizes** - Compressed to MP3

## ⚠️ Important Notes

### Safety Features

1. **Dry run mode** - Preview before converting
2. **Confirmation prompt** - Asks before making changes
3. **Error handling** - Stops if conversion fails
4. **Size verification** - Checks output file isn't empty

### Things to Know

1. **Irreversible** - Original files are deleted after conversion
2. **Make backups** - If you need to keep originals
3. **Quality ceiling** - Can't improve quality of low-bitrate sources
4. **File size** - 320k MP3 will be larger than 128k MP3

### Best Practices

```bash
# ✅ DO: Test with dry-run first
python scripts/convert_audio.py --dry-run

# ✅ DO: Backup important originals
cp -r audio/ audio_backup/

# ✅ DO: Check output quality
# Listen to converted files before deleting backups

# ❌ DON'T: Run without checking
# Always verify what will be converted

# ❌ DON'T: Convert already-compressed files expecting quality gain
# 128k MP3 → 320k MP3 won't magically sound better
# (but it ensures consistency)
```

## 🔍 Troubleshooting

### FFmpeg Not Found

**Error:**
```
❌ Error: FFmpeg is not installed!
```

**Solution:**
```bash
# macOS
brew install ffmpeg

# Ubuntu
sudo apt install ffmpeg

# Verify
ffmpeg -version
```

### Conversion Failed

**Error:**
```
❌ Error converting file.wav
```

**Solutions:**
1. Check file isn't corrupted
2. Verify it's actually an audio file
3. Check disk space
4. Try converting manually:
   ```bash
   ffmpeg -i file.wav -b:a 320k output.mp3
   ```

### Permission Denied

**Error:**
```
Permission denied: audio/file.wav
```

**Solution:**
```bash
# Make files writable
chmod -R u+w audio/

# Or run with appropriate permissions
sudo python scripts/convert_audio.py
```

### Out of Disk Space

**Error:**
```
No space left on device
```

**Solution:**
1. Free up space
2. Convert in batches
3. Use external drive
4. Delete backups after verification

## 💡 Advanced Tips

### Selective Conversion

Convert only specific file types:

```bash
# Temporarily move files you don't want converted
mkdir temp_storage
mv audio/*.mp3 temp_storage/

# Convert remaining files
python scripts/convert_audio.py --force

# Move back
mv temp_storage/*.mp3 audio/
rmdir temp_storage
```

### Keep Originals

If you want to keep original files:

```bash
# 1. Make copies
cp -r audio/ audio_originals/

# 2. Convert the copies
python scripts/convert_audio.py --force

# Now you have both!
```

### Batch Processing Multiple Directories

```bash
# Process audio directory
cd /Users/ben/Documents/Language_Seed_AI_Hello_World
python scripts/convert_audio.py --force

# The script automatically handles all subdirectories!
```

## 📊 Performance

### Conversion Speed

Typical speeds (depends on CPU):
- **WAV to MP3**: ~10-20x realtime (1 min audio = 3-6 sec conversion)
- **FLAC to MP3**: ~8-15x realtime
- **AAC to MP3**: ~5-10x realtime

### File Size Reduction

Average savings:
- **WAV**: 90-95% smaller
- **FLAC**: 60-80% smaller
- **AAC**: Similar or slightly larger
- **Low bitrate MP3**: Larger (quality upgrade)

## 🎯 Summary

### Quick Reference

```bash
# Preview
python scripts/convert_audio.py --dry-run

# Convert (interactive)
python scripts/convert_audio.py

# Convert (auto)
python scripts/convert_audio.py --force

# Help
python scripts/convert_audio.py --help
```

### What You Get

- 🎵 **320k MP3** - Maximum quality
- 🎧 **Stereo** - Full stereo imaging  
- 📊 **48kHz** - Professional sample rate
- 🌐 **Universal** - Works everywhere
- 💾 **Smaller files** - Easier to host
- ⚡ **Fast loading** - Better user experience

---

**Happy converting!** 🎵

Convert all your audio to HQ MP3 with one command! ✨

