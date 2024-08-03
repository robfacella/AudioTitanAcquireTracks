#!/bin/bash

# Change to Target Directory in this case I cloned the Repo into my working Dir
cd ..
# Don't use ls where a GLOB will suffice *
#ls -lah *.mkv

# For Filename in *.mkv
for f in *.mkv; do
  # Print filename
  echo "File -- $f"
  # ffprobe that File
  #ffprobe "$f"
  # Probe the File for an ITERABLE list (csv)
  #ffprobe -v quiet -show_entries stream=index,codec_name,height -of csv "$f"
  for line in $(ffprobe -v quiet -show_entries stream=index,codec_name,height -of csv "$f"); do
    echo "$line" >> "$f"".probe"
    ## if audio
  done
  #ffmpeg -i "$f"
  # Now to extract the tracks...
done
#ls -lah 2024-07-28\ 14-20-12.mkv
#ffprobe 2024-07-28\ 14-20-12.mkv
