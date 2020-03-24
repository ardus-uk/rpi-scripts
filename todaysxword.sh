#!/bin/bash
# Grab the cryptic crossword from the Guardian newspaper on a weekday
DATE8=$(date +"%Y%m%d")
if [ $DOW -le 5 ]
then
	TODAYSXWORD="https://crosswords-static.guim.co.uk/gdn.cryptic.$DATE8.pdf"
	OUTFILE="./xwords/gdn.cryptic.$DATE8.pdf"
	if [ ! -f "$OUTFILE" ]
	then
		wget $TODAYSXWORD -O $OUTFILE
		lp $OUTFILE
	fi
fi


