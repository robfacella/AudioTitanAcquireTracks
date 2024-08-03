#!/bin/bash
workDir=".."
thisDir=$(pwd)

cd $workDir
ls *.mkv | tail -6

echo $thisDir"/TestingTracks"
