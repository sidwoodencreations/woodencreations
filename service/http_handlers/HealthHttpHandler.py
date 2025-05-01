import tornado

from service.common.base_handler import BaseHandler


class HealthHttpHandler(BaseHandler):
  def get(self):
    self.write("App is healthy")
