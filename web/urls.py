from django.urls import path
from web import views


app_name ="web"


urlpatterns = [
    path ("", views.index, name="index"),
    path("create_word/",views.create_word,name="create_word"),
    path("<str:id>/edit_word/",views.edit_word,name="edit_word"),
  
]