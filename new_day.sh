#!/bin/bash

day_of_month=$(date +"%d")
lang="python"

if [ ! -z $1 ]; then
  lang=$1
fi

if [ ! -z $2 ]; then
  day_of_month=$2
fi

parent_dir=$lang
day_dir="$parent_dir/day_$day_of_month"
file_path="$day_dir/day_$day_of_month"

if [ ! -d $lang ]; then
  mkdir $lang
fi

if [ ! -d "$lang/day_$day_of_month" ]; then
  mkdir -p "$day_dir"
fi

if [ $lang == "python" ]; then
  echo "Creating $file_path.py from $lang/day_template.py..."
  cp $lang/day_template.py "$file_path.py"
  sed -i '' "s/num/$day_of_month/g" "$lang/day_$day_of_month/day_$day_of_month.py"
elif [ $lang == "raku" ]; then
  echo "Creating $file_path.raku"
  touch "$file_path.raku"
fi

echo "Creating $file_path.test & $file_path.input..."
touch "$file_path.test"
touch "$file_path.input"

echo
echo "--- Output ---"
ls $day_dir
