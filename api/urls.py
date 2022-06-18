"""URLs api rest"""

# Local
from .patches import routers

# Urls
from api.products import router as products_router
from api.purchases import router as purchases_router

"""
from .warehouse import router as router_warehouse

router = routers.DefaultRouter()
router.extend(router_warehouse)
urlpatterns = router.urls
"""
urlpatterns = []
urlpatterns.extend(products_router.urlpatterns)
urlpatterns.extend(purchases_router.urlpatterns)
