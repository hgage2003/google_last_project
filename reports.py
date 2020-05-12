#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# create pdf at filename with title, empty line and additional_info
def generate_report(filename, title, additional_info):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  empty_line = Spacer(1,20)
  body = Paragraph(additional_info, styles["BodyText"])
  report.build([report_title, empty_line, body])
