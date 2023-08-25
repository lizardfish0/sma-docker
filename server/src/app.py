from litestar import Litestar
from litestar.logging import LoggingConfig
from litestar.middleware.logging import LoggingMiddlewareConfig

from views import process_radarr_webhook

logging_middleware_config = LoggingMiddlewareConfig()
logging_config = LoggingConfig(
    loggers={
        "sma-server": {
            "level": "INFO",
            "handlers": ["queue_listener"],
        }
    }
)
sma_app = Litestar(
    route_handlers=[process_radarr_webhook],
    middleware=[
        logging_middleware_config.middleware
    ],
    logging_config=logging_config,
)
