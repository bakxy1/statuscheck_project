from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StatusCheckResultViewSet

router = DefaultRouter()
router.register(r"results", StatusCheckResultViewSet, basename="statuscheckresult")

urlpatterns = [path("", include(router.urls))]
