from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from readings.views_auth import RegisterView
from readings.views import BuildingViewSet, PowerReadingViewSet, RegisterUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'buildings', BuildingViewSet)
router.register(r'readings', PowerReadingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/register/', RegisterUser.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]