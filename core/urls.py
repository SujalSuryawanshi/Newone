from django.urls import path
from .views import Home,AddPost,Edit,DeletePost
from . import views
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path("add-item/", AddPost.as_view(), name="add"),
    path("delete/<int:pk>/remove", DeletePost.as_view(), name="delete"),
    path("edit/<int:pk>", Edit.as_view(), name="edit"),
]


