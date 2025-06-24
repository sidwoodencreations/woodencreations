import json

import tornado

from service.common.base_handler import BaseHandler
from service.common.smtp_helper import SMTPHelper


class ContactHttpHandler(BaseHandler):
  def post(self):
    email = SMTPHelper()
    json_body = json.loads(self.request.body)
    recipients = [
      "sidwoodencreations@gmail.com",
      "kimalexispeens@gmail.com"
    ]
    query = f"""
    Query:
      {json_body["query"]}
    Phone Number:
      {json_body["phoneNumber"]}
    Email:
      {json_body["email"]}
    """
    email.send_email(recipient_emails=recipients,
                     subject=f"Customer inquery from {json_body['email']}",
                     body=query
                     )
    self.write({
      "Status": "Success",
    })
