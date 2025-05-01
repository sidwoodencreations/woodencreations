import tornado

from service.common.logger import SingletonLogger


class BaseHandler(tornado.web.RequestHandler):
  logger = None

  def initialize(self) -> None:
    self.logger = SingletonLogger()

  def prepare(self):
    self.logger.debug(f"Endpoint: {self.request.path}")
    self.logger.debug(f"Method: {self.request.method}")
    if self.request.body.decode("utf-8") != "":
      self.logger.debug(f"Body: {self.request.body.decode('utf-8')}")
    if self.request.query_arguments:
      self.logger.debug(f"Query: {self.request.query_arguments}")
    super().prepare()
