from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, PlatformApiCallViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'products', ProductViewSet)
router.register(r'platform-apicalls', PlatformApiCallViewSet)
# router.register(r'order-list', OrderListView)



urlpatterns = [
    path('api/', include(router.urls)),
    # path('get-token/', get_auth_token, name='get_auth_token'),
    # path('platform-apicalls/', PlatformApiCallMixin),
    # path('order-list/', OrderListView.as_view()),



]
