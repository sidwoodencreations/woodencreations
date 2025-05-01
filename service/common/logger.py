import logging
import sys


class SingletonLogger:
  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
      cls._instance._setup_logger()
    return cls._instance

  def _setup_logger(self):
    self.logger = logging.getLogger('SingletonLogger')
    self.logger.setLevel(logging.DEBUG)

    if not self.logger.handlers:
      formatter = logging.Formatter(
        fmt='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
      )
      console_handler = logging.StreamHandler(sys.stdout)
      console_handler.setFormatter(formatter)
      self.logger.addHandler(console_handler)

  def __getattr__(self, name):
    if name in ['debug', 'info', 'warning', 'error', 'critical', 'exception']:
      return getattr(self.logger, name)
    raise AttributeError(f"'SingletonLogger' object has no attribute '{name}'")
