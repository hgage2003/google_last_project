#!/usr/bin/env python3

from PIL import Image
import os

in_dir = os.path.expanduser('~/supplier-data/images')

images = os.listdir(in_dir)

for i in images:
  file_name = os.path.join(in_dir, i)
  try:
    im = Image.open(file_name)
  except IOError:
    continue

  new_name, _ = os.path.splitext(file_name)
  new_name = new_name + '.jpeg'

  im.convert("RGB").resize((600,400)).save(new_name, "JPEG")
