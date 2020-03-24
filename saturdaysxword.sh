#!/bin/bash
# Grab the cryptic crossword from the Guardian newspaper on Saturday
DATE8=$(date +"%Y%m%d")
DOW=$(date +"%u")
if [ $DOW -eq 6 ]
then
	TODAYSXWORD="https://crosswords-static.guim.co.uk/gdn.cryptic.$DATE8.pdf"
	OUTFILE="./xwords/gdn.cryptic.$DATE8.pdf"
	if [ ! -f "$OUTFILE" ]
	then
		wget $TODAYSXWORD -O $OUTFILE
		lp $OUTFILE
	fi
fi


