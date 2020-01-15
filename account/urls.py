from django.urls import path
from .views import signin, signup, signout, profile

""" ЛОКАЛЬНАЯ ТАБЛИЦА МАРШРУТОВ """
urlpatterns = [
    path('signin', signin),
    path('signup', signup),
    path('signout', signout),
    path('profile', profile),
    # path('signup_res', signup_res),
]