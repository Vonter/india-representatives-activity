#!/bin/bash

for sabha in {15..17};
do
  mkdir -p "raw/Lok Sabha/${sabha}"

  if ! [ -f "raw/Lok Sabha/${sabha}/index.html" ]; then
    curl "https://prsindia.org/mptrack/${sabha}th-lok-sabha" -o "raw/Lok Sabha/${sabha}/index.html"
    sleep 5
  fi

  for representative in $(cat "raw/Lok Sabha/${sabha}/index.html" | /usr/bin/grep -oP "href=\"\/mptrack.*?\"" | cut -d '"' -f 2 | cut -d "/" -f 4 | sort -u)
  do
    echo "$representative"
    mkdir -p "raw/Lok Sabha/${sabha}/${representative}"

    if ! [ -f "raw/Lok Sabha/${sabha}/${representative}/index.html" ]; then
      curl "https://prsindia.org/mptrack/${sabha}-lok-sabha/${representative}" -o "raw/Lok Sabha/${sabha}/${representative}/index.html"
      sleep 5
    fi
  done
done

for sabha in {15..17};
do
  zip -r "raw/Lok Sabha/${sabha}.zip" "raw/Lok Sabha/${sabha}/"
done
