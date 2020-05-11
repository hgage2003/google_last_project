#!/usr/bin/env python3

import os
import requests

in_dir = os.path.expanduser('~/supplier-data/images')
url = "http://localhost/upload/"

for image_file in os.listdir(in_dir):
  _, ext = os.path.splitext(image_file)
  if not ext == '.jpeg':
      continue
  file_name = os.path.join(in_dir, image_file)
  with open(file_name, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
