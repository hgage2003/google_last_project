#!/usr/bin/env python3

import reports
import os
import datetime
import emails

pdf_name = os.path.expanduser('processed.pdf')
in_dir = os.path.expanduser('supplier-data/descriptions')

# returns list of tuples (name, weight) from txt files
def get_fruit_from_dir(in_dir):
  out_list = []
  filenames = os.listdir(in_dir)
  for fname in filenames:
    _, ext = os.path.splitext(fname)
    if not ext == '.txt':
      continue
    full_name = os.path.join(in_dir, fname)
    with open(full_name) as desc_file:
      name = desc_file.readline().rstrip()
      weight = int(desc_file.readline().rstrip().split(' ')[0])
      out_list.append((name, weight))
  return out_list

def main():
  title = "Processed Update on {}".format(
          datetime.date.today().strftime("%B %d, %Y"))
  fruits = get_fruit_from_dir(in_dir)
  reports.generate_report(pdf_name, title, fruits)

  sender = 'automation@example.com'
  receiver = '{}@example.com'.format(os.environ['USER'])
  subject = 'Upload Completed - Online Fruit Store'
  body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email'

  message = emails.generate_email(sender, receiver, subject, body, pdf_name)
  emails.send_email(message)

if __name__ == "__main__":
  main()
