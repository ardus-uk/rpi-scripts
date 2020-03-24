#!/bin/bash
DATE8=$(date +"%Y%m%d")
DOW=$(date +"%u")
#echo $DOW
if [ $DOW -eq 6 ]
then
	#echo $DOW
	TODAYSXWORD="https://crosswords-static.guim.co.uk/gdn.cryptic.$DATE8.pdf"
	OUTFILE="./xwords/gdn.cryptic.$DATE8.pdf"
	if [ ! -f "$OUTFILE" ]
	then
		#echo $TODAYSXWORD
		wget $TODAYSXWORD -O $OUTFILE
		#echo $OUTFILE
		lp $OUTFILE
	fi
fi


