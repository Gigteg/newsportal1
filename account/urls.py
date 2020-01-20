from django.urls import path
from .views import signin, signup, signout, profile, ajax_reg

""" ЛОКАЛЬНАЯ ТАБЛИЦА МАРШРУТОВ """
urlpatterns = [
    path('signin', signin),
    path('signup', signup),
    path('signout', signout),
    path('profile', profile),
    path('ajax_reg', ajax_reg)
]
