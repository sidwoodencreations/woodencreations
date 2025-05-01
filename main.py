import asyncio
import os

import tornado.ioloop
import tornado.web

from service.http_handlers.ContactHttpHandler import ContactHttpHandler
from service.http_handlers.HealthHttpHandler import HealthHttpHandler
from service.http_handlers.StaticPageHttpHandler import AngularStaticFileHandler
from service.common.logger import SingletonLogger

logger = SingletonLogger()
SERVICE_PORT = 8888


def make_app():
    default_path = os.path.join("dist", "wood", "browser")
    paths = [
        (r"/health", HealthHttpHandler),
        (r"/contact", ContactHttpHandler),
        (r"/(.*)", AngularStaticFileHandler, {
            "path": default_path,
            "default_filename": "index.html",
            "angular_index": "index.html"
        })
    ]
    logger.info("Registering paths")
    for path in paths:
        logger.info(f"{path[0]}: {path[1].__name__}")

    app = tornado.web.Application(paths)
    app.add_handlers(r".*", paths)
    return app

async def main():
    app = make_app()
    app.listen(SERVICE_PORT)
    logger.info(f"starting server on {SERVICE_PORT}")
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
