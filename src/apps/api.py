from ninja import NinjaAPI

api = NinjaAPI(
    title="CostPI API",
    version="1.0.0",
    description="API for CostPI")


api.add_router('gantt/', 'apps.gantt.api.router')

