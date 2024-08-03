#!/bin/bash
workDir=".."
thisDir=$(pwd)

cd $workDir

mkdir -p "$thisDir""/TestingTracks"

cp $(ls *.mkv | tail -6) $thisDir"/TestingTracks"
