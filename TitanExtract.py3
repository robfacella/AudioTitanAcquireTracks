#!/bin/python3
import os

# Default to folder Above
targetDir = '..'
print ( "Extracting tracks from Files" )
# Up a dir
os.chdir ( targetDir )
# Set Main working Driectory regardless of how Target Dir is Set
mainDir = ( os.getcwd() )

def ExtractSauce(path):
  # Move into Extraction Folder with PROBE file
  os.chdir(path)
  #
with os.scandir() as listDir:
  for entry in listDir:
    # Only run through Directories which end in the substring "EXTRACT"
    if entry.is_dir() and entry.name.endswith("EXTRACT"):
      # Enter Subfolder and Extract Tracks
      ExtractSauce ( entry.name )
      # print ( os.getcwd() )
      # Return to Working Directory before continuing iteration
      os.chdir ( mainDir )
