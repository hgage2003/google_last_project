#!/usr/bin/env python3

import emails
import psutil
import shutil
import socket
import os

# returns True if CPU usage is over 80%
def test_cpu():
  if psutil.cpu_percent(interval=0.1) > 80:
    return True
  return False

#returns True if available virtual memory is less than 500 Mb
def test_memory():
  mem = psutil.virtual_memory()
  if mem.available < 500 * 1024 * 1024: # 500 MB
    return True
  return False

#returns True if available space on '/' is less than 20%
def test_space():
  du = shutil.disk_usage('/')
  percent_free = 100 * du.free / du.total
  if percent_free < 20:
    return True
  return False

#returns True if localhost cannot be resolved to '127.0.0.1'
def test_network():
  try:
    local_ip = socket.gethostbyname('localhost')
    if not local_ip == '127.0.0.1':
      return True
  except:
    return True
  return False

def main():
  checks = [
      (test_cpu, "CPU usage is over 80%")
      ,(test_memory, "Available memory is less than 500MB")
      ,(test_space, "Available disk space is less than 20%")
      ,(test_network, "localhost cannot be resolved to 127.0.0.1")
      ]

  sender = 'automation@example.com'
  receiver = '{}@example.com'.format(os.environ['USER'])
  body = 'Please check your system and resolve the issue as soon as possible'

  for check, error in checks:
    if check():
      subject = 'Error - ' + error
      message = emails.generate_email(sender, receiver, subject, body, None)
      emails.send_email(message)

if __name__ == '__main__':
  main()


