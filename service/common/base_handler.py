import tornado

from service.common.logger import SingletonLogger


class BaseHandler(tornado.web.RequestHandler):
  logger = None

  def set_default_headers(self):
    self.set_header("Access-Control-Allow-Origin", "*")
    self.set_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, PATCH, OPTIONS")
    self.set_header("Access-Control-Allow-Headers", "Content-Type, Authorization, Accept, X-Requested-With")


  def options(self):
    self.set_status(204)
    self.finish()

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
