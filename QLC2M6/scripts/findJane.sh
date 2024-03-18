#!/bin/bash

> oldFiles.txt


files=$(grep " jane " ../data/list.txt | cut -d' ' -f3)

cd ~/data

for fle in $(echo $files); do 
   fff=$(realpath $(basename $fle))
   if [ -f  $fff ]; then
        echo $fff >> ~/scripts/oldFiles.txt;
   else
	echo $fff;
   fi
done

cd ~/scripts

