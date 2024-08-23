import asyncio

import uvicorn
from fastapi import FastAPI

from app.api.api import api_routers
from app.settings import ApplicationSettings

app = FastAPI()

for api_router in api_routers:
    app.include_router(api_router, prefix="/api")

settings = ApplicationSettings()


async def main():
    uvicorn.run(app="main:app", host=settings.host, port=settings.port, reload=True)


if __name__ == "__main__":
    asyncio.run(main())
