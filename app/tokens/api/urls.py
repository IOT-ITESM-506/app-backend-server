from django.urls import path
from tokens.api import views
from tokens.api.views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'token'

urlpatterns = [
    path('tokens/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tokens/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]