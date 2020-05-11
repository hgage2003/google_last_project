#!/usr/bin/env python3

import os
import requests
import json

url = 'http://34.71.9.157/fruits/'
in_dir = os.path.expanduser('~/supplier-data/descriptions')

def read_files_to_list(path):
  out_list = []
  for f_name in os.listdir(in_dir):
    #only iterate through .txt files
    name, ext = os.path.splitext(f_name)

    print(name + ext)

    if not ext == '.txt':
      continue
  
    file_path = os.path.join(in_dir, f_name)
    fruit_dict = {}
    with open(file_path) as f:
      fruit_dict['name'] = f.readline().rstrip()
      fruit_dict['weight'] = int(f.readline().rstrip().split(' ')[0])
      fruit_dict['description'] = f.readline().rstrip()
      fruit_dict['image_name'] = name + '.jpeg'

    out_list.append(fruit_dict)
  return out_list

fruits_list = read_files_to_list(in_dir)
for fruit in fruits_list:
    #fruit_json = json.dumps(fruit)
    #print(fruit_json)
    response = requests.post(url, data=fruit)
    response.raise_for_status()

