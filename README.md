# AudioTitanAcquireTracks
Extract All Audio Tracks from a Video File with Multiple Audio Streams

# Usage (from a Shell within Project Dir (containing video files [default targets MKV] )
# Clone a Copy of this Project
git clone https://github.com/robfacella/AudioTitanAcquireTracks.git

# Run the Analyze Script to Generate Extraction Directories with probe file for Track Targeting 
bash AnalyzeTitan.sh

# Run the Python Extraction Script
# Defaults to Tracks 2 and 3 -- (ffmpeg leaves the Video on Track 0, OBS starts Track Counting at 1, so it lines up with what OBS's GUI would show you)
# my MKV output from OBS is : 
# Track 1 all, 
# Track 2 microphone, 
# Track 3 desktop; 
# hence pulling tracks 2 and 3; 
python3 TitanExtract.py3
