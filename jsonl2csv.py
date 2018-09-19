#####################################################################
#                                                                   #
# Simple script to parse multiple .jsonl files to a single csv      #
#                                                                   #
# Author: Enrique Delgado                                           #
#                                                                   #
#####################################################################
#
# Just execute this file in the directory containing the jsonl files
#  Please take into account that data might not fit in case jsonl 
#  files do not share the same columns.
#

import glob
import os
import sys
import csv

def main(fname):
  lines=[]

  for filename in glob.glob(os.path.join(os.getcwd(), '*.jsonl')):
    with open(filename) as file:
      for line in file:
        lines.append(eval(line.replace("false","False").replace("true","True")))

  with open(fname, 'wb') as f: 
    w = csv.DictWriter(f, lines[0].keys())
    w.writeheader()
    for reg in lines:
      w.writerow(reg)


if __name__ == "__main__":
  if len(sys.argv) > 2:
    raise SyntaxError("Too many arguments. Please indicate the name of the file only.")
  if len(sys.argv) < 2:
    raise SyntaxError("Insufficient arguments. Please indicate the name of the file.")
  else:
      if os.path.exists(os.path.join(os.getcwd(),sys.argv[1])):
        raise IOError("File "+sys.argv[1]+" already exists.")
      else:
        main(sys.argv[1])
