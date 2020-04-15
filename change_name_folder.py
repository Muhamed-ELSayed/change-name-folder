#!/usr/bin/env python3
import re
import os
import sys
import csv
import subprocess as sp




def search_folder_pattern(path, pattern):
  """
  Here we search in the path taken from the user with the pattern
  """
  result = []
  _list = []

  # Check if path is exist or no
  if os.path.exists(path):
    for path in os.walk(path):
      for _dir in path:
        if type(_dir) == str:
          result = re.findall(r"^(.*)({}.*)$".format(pattern.lower()), _dir)
          if not result == []:
            _list.append(result)
  else:
    return "We can't find your path please try again."
    
  return _list

def rename_folder(new_value):
  """
  Here we will receive list folder that's start with pattern,
  and we go to change directories
  """
  folders = search_folder_pattern(path, pattern)

  if len(folders) > 0:
    for folder in folders:
      for f in range(len(folder)):
        if os.path.exists(folder[f][0]):
          os.chdir(folder[f][0])
          os.rename(folder[f][1], new_value)
        
        else:
          return "Path not found we get a proplem please check your name folder."

  else:
    return "No folder found"

  
  return "We will update this script to export file CSV that contains observation of all paths that are changed"

  


def main():
  print(rename_folder(input("Please enter a new name.\n")))
  

if __name__ == "__main__":
  ptcon = "y"
  pacon = "y"

  while(ptcon.lower() == "y"):
    path  = input("Please Enter your path:\n")
    if not "/" or "'\'" in path:
      print("Path should be include '/' or '\'.\n")
    else:
      ptcon = "n"
  
  while(pacon.lower() == "y"):
    pattern = input("Please enter name of folder you need change it: \n")
    if pattern == "":
      print("Pattern shouldn't be empty string. \n")
    else:
      pacon = "n"

  main()
