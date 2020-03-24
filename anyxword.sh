#!/bin/bash
# Grab the cryptic crossword from the Guardian newspaper for a day of our choosing
echo -n "Enter date in form yyyymmdd > "
read DATE8
PDATE8="P_"$DATE8
DOW=$(date --date=${PDATE8#?_} "+%u")
echo $DOW
# No crossword on a Sunday (actually, not even a newspaper!)
if [ ! $DOW -eq 7 ]
then
	CHOSENXWORD="https://crosswords-static.guim.co.uk/gdn.cryptic.$DATE8.pdf"
	OUTFILE="./xwords/gdn.cryptic.$DATE8.pdf"
	if [ ! -f "$OUTFILE" ]
	then
		wget $CHOSENXWORD -O $OUTFILE
		lp $OUTFILE
	fi
fi
