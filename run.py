#!/usr/bin/env python3

import os
import requests
import json

url = 'http://34.71.9.157/fruits/'
txt_dir = os.path.expanduser('~/supplier-data/descriptions')
img_dir = os.path.expanduser('~/supplier-data/images')

# iterate through .txt files in dir and
# return a list of dictionaries
def make_requests(txt_path, img_path):
  result = []

  #only iterate through .txt files
  txt_files = [f for f in os.listdir(txt_path) if f.endswith('.txt')]
  #need this to check if corresponding image presents
  img_files = [f for f in os.listdir(img_path) if f.endswith('.jpeg')]
  
  for filename in txt_files:
    full_path = os.path.join(txt_path, filename)

    fruit = {}
    with open(full_path) as f:
      fruit['name'] = f.readline().rstrip()
      # convert from string '100 lbs' to int 100
      fruit['weight'] = int(f.readline().rstrip().split(' ')[0])
      fruit['description'] = f.readline().rstrip()
      f.close()

      image_name, _ = os.path.splitext(filename)
      image_name += '.jpeg'
      if image_name in img_files:
        fruit['image_name'] = image_name

    result.append(fruit)
  return result

def main():
  fruits_list = make_requests(txt_dir, img_dir)
 
  for fruit in fruits_list:
    response = requests.post(url, json=fruit)
    response.raise_for_status()

if __name__ == '__main__':
  main()
