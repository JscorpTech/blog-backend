from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SettingsView, HealthView

router = DefaultRouter()
router.register("settings", SettingsView, basename="settings")


urlpatterns = [
    path("", include(router.urls)),
    path("health/", HealthView.as_view(), name="health"),
]
