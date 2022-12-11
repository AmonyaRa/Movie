from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from applications.account.views import RegisterUserApiView

urlpatterns = [
    path('register/', RegisterUserApiView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh', TokenRefreshView.as_view())
]
