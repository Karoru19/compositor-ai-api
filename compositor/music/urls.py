from django.urls import path, include
from rest_framework import routers
from . import viewsets


router = routers.DefaultRouter()
router.register(r"compose", viewsets.ComposeViewSet, base_name="compose")
router.register(r"composition", viewsets.CompositionViewSet)
router.register(r"history", viewsets.HistoryViewSet)
router.register(r"login", viewsets.LoginViewSet, base_name="login")
router.register(r"register", viewsets.RegisterViewSet, base_name="register")
router.register(
    r"password-change", viewsets.PasswordChangeViewSet, base_name="password_change"
)
router.register(
    r"password-reset", viewsets.PasswordResetViewSet, base_name="password_reset"
)
router.register(
    r"password-reset/confirm",
    viewsets.PasswordResetConfirmViewSet,
    base_name="password_reset_confirm",
)
router.register(r"profile", viewsets.ProfileViewSet)
router.register(r"song", viewsets.SongViewSet)

urlpatterns = [path("", include(router.urls))]
