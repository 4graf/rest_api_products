from app.api.healthcheck.controllers import healthcheck_router
from app.api.product.controllers import product_router

api_routers = [product_router, healthcheck_router]
