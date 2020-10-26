from django.urls import path
from . import views
urlpatterns = [
    path('' , views.home_view , name = "homepage"),
    path('posts/create/' , views.create_post , name = "create-post"),
    path('posts/delete/' , views.delete_page , name = "delete-page"),
    path('post/delete/<int:id>/' , views.deletePost , name = "delete_post"),
    path('posts/update/' , views.update , name = "update-page"),
    path('post/update/<int:id>/' , views.update_post , name = "update-post")
]
