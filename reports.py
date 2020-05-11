#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

#body is a list of name/weight tuples
def generate_report(filename, title, fruits):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  empty_line = Spacer(1,20)
  story = [report_title, empty_line]

  for fruit in fruits:
    fruit_info = "name: {}<br/>weight: {} lbs".format(fruit[0],fruit[1])
    story.append(Paragraph(fruit_info, styles["BodyText"]))
    story.append(empty_line)
  
  report.build(story)
  
def test_pdf():
  fruits = [('apple',1),('cherry',2),('mercedez-benz',8096)]
  generate_report("./test.pdf", "This is a test PDF for reports.py", fruits)

if __name__ == '__main__':
    test_pdf()
