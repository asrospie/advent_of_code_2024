#!/bin/bash

kotlinc $1 -include-runtime -d $2
java -jar $2
rm $2
