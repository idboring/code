#!/bin/bash
find -type f ! -name *_orign.jpg -print | xargs rm -f
mkdir output
find -type f  -name *.jpg -print0 | xargs -n 1 -0 -i mv {} ./output
cd output
rename _orign \0 *.jpg
du -b *.jpg | gawk '{ print $2 "," $1 }' ORS="\r\n" > index.txt
zip out.zip *
date '+%Y%m%d%H%M%S' | xargs -i mv *.zip PICTURE_1509251030040009{}.zip