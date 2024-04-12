from django.urls import path
from .views import SignUpView

urlpatterns = [
    path("cadastreSe/", SignUpView.as_view(), name="signup"),
]
