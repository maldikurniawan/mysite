from django.urls import path
from api.views.Auth import Auth

urlpatterns = [
    path("auth/", Auth.as_view()),
]
