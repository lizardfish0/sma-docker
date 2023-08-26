from litestar import post, Request

from server.src.models.radarr import RadarrWebhook


@post(path="/radarr")
async def process_radarr_webhook(request: Request, data: RadarrWebhook) -> None:
    if data.eventType == "Test":
        request.logger.info(f"Received test event from radarr, skipping.")
