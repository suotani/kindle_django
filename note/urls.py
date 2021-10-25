from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="note_list"),
  path('<int:pk>', views.show, name="note_detail"),
  path('create', views.create, name="note_create"),
  path('<int:pk>/update', views.update, name="note_update"),
  path('<int:pk>/delete', views.delete, name="note_delete"),
]