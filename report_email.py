#!/usr/bin/env python3

import reports
import os
import datetime
import emails

pdf_name = '/tmp/processed.pdf'
in_dir = os.path.expanduser('~/supplier-data/descriptions')

#returns formatted string for pdf
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
      weight = desc_file.readline().rstrip()
      out_list.append("name: {}<br/>weight: {}".format(
          name, weight))
  return "<br/><br/>".join(out_list)

def main():
  title = "Processed Update on {}".format(
          datetime.date.today().strftime("%B %d, %Y"))
  fruits = get_fruit_from_dir(in_dir)
  reports.generate_report(pdf_name, title, fruits)

  sender = 'automation@example.com'
  receiver = '{}@example.com'.format(os.environ['USER'])
  subject = 'Upload Completed - Online Fruit Store'
  body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

  message = emails.generate_email(sender, receiver, subject, body, pdf_name)
  emails.send_email(message)

if __name__ == "__main__":
  main()
