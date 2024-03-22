from ninja import NinjaAPI
from app.api import router as app_router

api = NinjaAPI()

api.add_router("/", app_router)


@api.get("/health", auth=None)
def health(request):
    return {"status": "ok"}
