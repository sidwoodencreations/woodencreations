import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

from service.common.logger import SingletonLogger


class SMTPHelper:
    def __init__(self, smtp_server="smtp.gmail.com", smtp_port=587):
        self.logger = SingletonLogger()
        self.sender_email = "sidwoodencreations@gmail.com"
        self.app_password = os.getenv("SMTP_PASSWORD")
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, recipient_emails, subject, body, is_html=False):

        if not isinstance(recipient_emails, list) or not recipient_emails:
            self.logger.debug("Error: recipient_emails must be a non-empty list")
            return False

        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = ', '.join(recipient_emails)
        msg['Subject'] = subject

        if is_html:
            msg.attach(MIMEText(body, 'html'))
        else:
            msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.app_password)
                server.sendmail(self.sender_email, recipient_emails, msg.as_string())
            self.logger.debug(f"Email sent successfully to {', '.join(recipient_emails)}")
            return True
        except Exception as e:
            self.logger.debug(f"Error sending email: {e}")
            return False
