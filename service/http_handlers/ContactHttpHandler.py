import json

import tornado

from service.common.base_handler import BaseHandler
from service.common.smtp_helper import SMTPHelper


class ContactHttpHandler(BaseHandler):
  def post(self):
    email = SMTPHelper()
    json_body = json.loads(self.request.body)
    recipients = ["adrianhawkins03@gmail.com", json_body["email"]]
    email.send_email(recipients, "Customer inquery", json_body["query"])
    self.write({
      "Status": "Success",
    })
