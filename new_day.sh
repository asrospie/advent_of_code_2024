#!/bin/bash

day_of_month=$(date +"%d")

if [ "$1" == "python" ]; then
  if [ ! -d "python" ]; then
    mkdir python
  fi

  if [ ! -d "python/day_$day_of_month" ]; then
    mkdir -p "python/day_$day_of_month"
  fi

  cp python/day_template.py "python/day_$day_of_month/day_$day_of_month.py"
  sed -i '' "s/num/$day_of_month/g" "python/day_$day_of_month/day_$day_of_month.py"
  touch "python/day_$day_of_month/day_$day_of_month.test"
  touch "python/day_$day_of_month/day_$day_of_month.input"
fi
