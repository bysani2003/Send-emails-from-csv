import csv
import smtplib
from email.mime.text import MIMEText

# Read the CSV file
with open('recipients.csv', 'r') as f:
  reader = csv.reader(f)
  recipients = list(reader)

# Set up the SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("your_email@gmail.com", "your_password")

# Set up the email message
msg = MIMEText("This is the body of the email")
msg['Subject'] = "This is the subject"
msg['From'] = "your_email@gmail.com"

# Send the email to each recipient
for r in recipients:
  msg['To'] = r[0]
  server.sendmail("your_email@gmail.com", r[0], msg.as_string())

# Close the SMTP server
server.quit()
