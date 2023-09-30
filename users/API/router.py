from django.urls import path
from users.API.views import RegisterView, UserView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('auth/register', RegisterView.as_view()),
    path('auth/login', TokenObtainPairView.as_view()),
    path('auth/me', UserView.as_view())

]
