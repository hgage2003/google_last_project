#!/usr/bin/env python3

import os
import datetime
import reports
import emails

pdf_name = '/tmp/processed.pdf'
in_dir = os.path.expanduser('~/supplier-data/descriptions')

#returns formatted string for pdf
def get_fruit_from_dir(in_dir):
  # list of name/weight pairs for each fruit
  out_list = []
  # list of .txt files
  filenames = [f for f in os.listdir(in_dir) if f.endswith('.txt')]
  for name in filenames:
    full_name = os.path.join(in_dir, name)
    with open(full_name) as desc_file:
      # first line - name
      name = desc_file.readline().rstrip()
      # second line - weight
      weight = desc_file.readline().rstrip()
      # skip rest of file
      desc_file.close()
      # fill list with current fruit
      out_list.append("name: {}<br/>weight: {}".format(
          name, weight))
  # return one string of friuts, divided by empty lines
  return "<br/><br/>".join(out_list)

def main():
  #make pdf
  title = "Processed Update on {}".format(
          datetime.date.today().strftime("%B %d, %Y"))
  fruits = get_fruit_from_dir(in_dir)
  reports.generate_report(pdf_name, title, fruits)

  #send email
  sender = 'automation@example.com'
  receiver = '{}@example.com'.format(os.environ['USER'])
  subject = 'Upload Completed - Online Fruit Store'
  body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

  message = emails.generate_email(sender, receiver, subject, body, pdf_name)
  emails.send_email(message)

if __name__ == "__main__":
  main()
