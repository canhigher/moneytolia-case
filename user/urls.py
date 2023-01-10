from django.urls import path

from user.views import RegistrationView, LogoutView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegistrationView.as_view()),
    path('logout/', LogoutView.as_view())
]
