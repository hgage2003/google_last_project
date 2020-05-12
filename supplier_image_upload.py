#!/usr/bin/env python3

import os
import requests

in_dir = os.path.expanduser('~/supplier-data/images')
url = "http://localhost/upload/"

jpeg_files = [f for f in os.listdir(in_dir) if f.endswith('.jpeg')]
for f in jpeg_files:
  file_name = os.path.join(in_dir, f)
  with open(file_name, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
