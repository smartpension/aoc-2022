#!/bin/bash

folder_prefix="2022-12-"

if [[ ! -z $1 ]]; then
    echo "Date specified ($1)"
    date=$1
    if [[ $date -gt $(date +%-d) ]]; then
        echo "Date in the future.."
        exit 1
    fi
    if [[ $date == "0"* ]]; then
        echo "Date provided wiht leading zero, stripping"
        date=$(echo $1 | sed 's/^0*//')
    fi
else
    date=$(date +%-d)
fi

# Create directory
mkdir ${folder_prefix}${date}
# Download input.txt
curl -s --cookie "session=$AOC_SESSION" https://adventofcode.com/2022/day/$date/input > ${folder_prefix}${date}/input.txt
# Create base files
echo 'with open("input.txt") as input_file:
    input_values = input_file.read().splitlines()
' > ${folder_prefix}${date}/part1.py
cp ${folder_prefix}${date}/part1.py ${folder_prefix}${date}/part2.py 
