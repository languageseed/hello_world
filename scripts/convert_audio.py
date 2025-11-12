#!/usr/bin/env python3
"""
Audio Converter for Hello World Blog
Converts all audio files to MP3 320k stereo (HQ) and removes originals
"""

import os
import sys
import subprocess
from pathlib import Path

# Get the project root directory
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
AUDIO_DIR = PROJECT_ROOT / 'audio'

# Supported input formats
SUPPORTED_FORMATS = [
    '.wav', '.flac', '.aac', '.ogg', '.webm', '.m4a', 
    '.wma', '.aiff', '.aif', '.opus', '.oga', '.mp3'
]

# FFmpeg settings for HQ MP3
BITRATE = '320k'
CHANNELS = '2'  # Stereo
SAMPLE_RATE = '48000'  # 48kHz

def check_ffmpeg():
    """Check if FFmpeg is installed"""
    try:
        result = subprocess.run(
            ['ffmpeg', '-version'],
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False

def get_audio_files(directory):
    """Find all audio files in directory and subdirectories"""
    audio_files = []
    
    for root, dirs, files in os.walk(directory):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix.lower() in SUPPORTED_FORMATS:
                # Skip if it's already a 320k MP3 (check if _hq marker exists)
                if file_path.suffix.lower() == '.mp3' and not file.endswith('_hq.mp3'):
                    # Will re-encode to ensure 320k quality
                    pass
                audio_files.append(file_path)
    
    return audio_files

def convert_to_hq_mp3(input_file, dry_run=False):
    """Convert audio file to HQ MP3 (320k stereo)"""
    
    # Generate output filename
    output_file = input_file.with_suffix('.mp3')
    
    # If input is already .mp3, add _hq suffix to avoid overwriting during conversion
    temp_output = output_file
    if input_file.suffix.lower() == '.mp3':
        temp_output = input_file.with_name(input_file.stem + '_hq.mp3')
    
    print(f"\n{'[DRY RUN] ' if dry_run else ''}Converting: {input_file.name}")
    print(f"  → {temp_output.name} (320k stereo)")
    
    if dry_run:
        return True
    
    # FFmpeg command for HQ MP3 conversion
    command = [
        'ffmpeg',
        '-i', str(input_file),           # Input file
        '-vn',                            # No video
        '-ar', SAMPLE_RATE,               # Sample rate 48kHz
        '-ac', CHANNELS,                  # Stereo (2 channels)
        '-b:a', BITRATE,                  # 320k bitrate
        '-f', 'mp3',                      # MP3 format
        '-y',                             # Overwrite output file
        str(temp_output)                  # Output file
    ]
    
    try:
        # Run FFmpeg conversion
        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"  ❌ Error converting {input_file.name}")
            print(f"  Error: {result.stderr}")
            return False
        
        # Check if output file was created and has content
        if not temp_output.exists() or temp_output.stat().st_size == 0:
            print(f"  ❌ Conversion failed: output file is empty")
            return False
        
        # If we converted an MP3 to _hq.mp3, handle the swap
        if input_file.suffix.lower() == '.mp3' and temp_output != output_file:
            # Remove original
            input_file.unlink()
            # Rename _hq.mp3 to original name
            temp_output.rename(output_file)
            print(f"  ✅ Upgraded to HQ: {output_file.name}")
        else:
            # Remove original non-MP3 file
            input_file.unlink()
            print(f"  ✅ Converted: {output_file.name}")
            print(f"  🗑️  Removed: {input_file.name}")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

def get_file_size_mb(file_path):
    """Get file size in MB"""
    return file_path.stat().st_size / (1024 * 1024)

def main():
    """Main conversion function"""
    print("🎵 Audio Converter - HQ MP3 (320k Stereo)")
    print("=" * 50)
    
    # Check for flags
    dry_run = '--dry-run' in sys.argv
    force = '--force' in sys.argv
    
    if dry_run:
        print("\n⚠️  DRY RUN MODE - No files will be modified\n")
    
    # Check if FFmpeg is installed
    if not check_ffmpeg():
        print("\n❌ Error: FFmpeg is not installed!")
        print("\nInstall FFmpeg:")
        print("  macOS:   brew install ffmpeg")
        print("  Ubuntu:  sudo apt install ffmpeg")
        print("  Windows: https://ffmpeg.org/download.html")
        sys.exit(1)
    
    print("✅ FFmpeg found\n")
    
    # Check if audio directory exists
    if not AUDIO_DIR.exists():
        print(f"❌ Error: Audio directory not found: {AUDIO_DIR}")
        sys.exit(1)
    
    # Find all audio files
    print(f"📁 Scanning: {AUDIO_DIR}\n")
    audio_files = get_audio_files(AUDIO_DIR)
    
    if not audio_files:
        print("No audio files found!")
        sys.exit(0)
    
    # Filter out README files
    audio_files = [f for f in audio_files if f.name != 'README.md']
    
    # Display found files
    print(f"Found {len(audio_files)} audio file(s):\n")
    
    total_size_before = 0
    for i, file in enumerate(audio_files, 1):
        size_mb = get_file_size_mb(file)
        total_size_before += size_mb
        print(f"  {i}. {file.name}")
        print(f"     Size: {size_mb:.2f} MB")
        print(f"     Format: {file.suffix.upper()}")
    
    print(f"\nTotal size: {total_size_before:.2f} MB")
    
    # Confirm conversion
    if not dry_run and not force:
        print("\n⚠️  This will:")
        print("  1. Convert all files to MP3 320k stereo")
        print("  2. Delete original files after successful conversion")
        print("  3. Cannot be undone!")
        
        response = input("\nContinue? [y/N]: ").strip().lower()
        if response != 'y':
            print("\nCancelled.")
            sys.exit(0)
    
    # Convert files
    print("\n" + "=" * 50)
    print("Converting files...")
    print("=" * 50)
    
    successful = 0
    failed = 0
    
    for audio_file in audio_files:
        if convert_to_hq_mp3(audio_file, dry_run):
            successful += 1
        else:
            failed += 1
    
    # Summary
    print("\n" + "=" * 50)
    print("Conversion Summary")
    print("=" * 50)
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")
    
    if not dry_run and successful > 0:
        # Calculate new total size
        remaining_files = get_audio_files(AUDIO_DIR)
        total_size_after = sum(get_file_size_mb(f) for f in remaining_files)
        
        print(f"\nStorage:")
        print(f"  Before: {total_size_before:.2f} MB")
        print(f"  After:  {total_size_after:.2f} MB")
        
        if total_size_after < total_size_before:
            saved = total_size_before - total_size_after
            percent = (saved / total_size_before) * 100
            print(f"  Saved:  {saved:.2f} MB ({percent:.1f}%)")
        elif total_size_after > total_size_before:
            added = total_size_after - total_size_before
            percent = (added / total_size_before) * 100
            print(f"  Added:  {added:.2f} MB ({percent:.1f}%) - HQ audio!")
    
    if dry_run:
        print("\n💡 Run without --dry-run to actually convert files")
    else:
        print("\n🎉 Done!")

if __name__ == '__main__':
    if '--help' in sys.argv or '-h' in sys.argv:
        print("Audio Converter - Convert all audio to HQ MP3")
        print("\nUsage:")
        print("  python scripts/convert_audio.py              # Interactive mode")
        print("  python scripts/convert_audio.py --dry-run    # Preview what will happen")
        print("  python scripts/convert_audio.py --force      # Skip confirmation")
        print("\nSettings:")
        print("  Bitrate: 320k")
        print("  Channels: Stereo (2)")
        print("  Sample Rate: 48kHz")
        print("\nSupported formats:")
        print("  WAV, FLAC, AAC, OGG, WebM, M4A, WMA, AIFF, OPUS, MP3")
        sys.exit(0)
    
    main()

