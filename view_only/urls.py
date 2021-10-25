from django.urls import path

from . import views
urlpatterns = [
  path('', views.index),
  path('kara_age', views.karaage, name="karaage"),
  path('apple', views.many_apple),
  path('banana/<int:num>', views.many_banana),
  path('product/<int:num1>/<int:num2>', views.product)
]