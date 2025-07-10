from django.urls import path
from .views import login_view, verify_token, validate_token

urlpatterns = [
    path('login/', login_view),
    path('verify/', verify_token),
    path('validate/', validate_token),
]
