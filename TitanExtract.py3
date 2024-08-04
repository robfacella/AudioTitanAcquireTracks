#!/bin/python3
import os

# Default to folder Above
targetDir = '..'
print ( "Extracting tracks from Files" )
# Up a dir
os.chdir ( targetDir )
# Set Main working Driectory regardless of how Target Dir is Set
mainDir = ( os.getcwd() )

def ReadPROBE():
  f = open("probe", "r")
  probe = ( f.readlines() )
  f.close()
  return probe
def ExtractFromTo(fromThis, toThis):
  print ("Extracting from " + fromThis + " to " + toThis + " ... ")
  
def AudioTracks(probe):
  filename = ( (os.getcwd().strip('EXTRACT')).split('/')[-1] )
  for line in probe:
    # Remove newLine char '\n'
    line = line.strip()
    # Split the CSV
    fields = line.split(',')
    # fields [0] is STREAM, [1] is trackNumber, [2] is codex, [3] if available is video height
    # if an audio codex
    if fields[2] == 'aac':
      #print (fields)
     # Skip Track 1, which is combined MIC and Desktop in my case
     if fields[1] != '1' :
      extractTo = ( filename + 'TRACK' + fields[1] + '.mp3' )
      ExtractFromTo ( filename, extractTo )
def ExtractSauce(path):
  # Move into Extraction Folder with PROBE file
  os.chdir(path)
  #
  probe = ReadPROBE()
  AudioTracks(probe)

with os.scandir() as listDir:
  for entry in listDir:
    # Only run through Directories which end in the substring "EXTRACT"
    if entry.is_dir() and entry.name.endswith("EXTRACT"):
      # Enter Subfolder and Extract Tracks
      ExtractSauce ( entry.name )
      # print ( os.getcwd() )
      # Return to Working Directory before continuing iteration
      os.chdir ( mainDir )
