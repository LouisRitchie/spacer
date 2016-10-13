#! /usr/bin/python

import sys

file1 = open(sys.argv[1], 'r+')
counter = 0
output = ""
lastLine = ""

for line in file1:
  if line.isspace():
    continue
  if '}' in line and counter >= 0:
    counter -= 1
  output += "  " * counter + line.replace("\n", "").replace("  ", "") + "\n"
  if '{' in line:
    counter += 1

if output[-1] != "\n":
  output += "\n"

file1.truncate(0)
file1.seek(0)
file1.write(output)
file1.close
