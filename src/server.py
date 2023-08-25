from litestar import Litestar, post

from src.models import RadarrWebhook


@post(path="/radarr")
async def process_radarr_webhook(data: RadarrWebhook) -> None:
    print(data)

app = Litestar(route_handlers=[process_radarr_webhook])
