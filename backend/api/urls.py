from django.urls import path
from . import views

urlpatterns = [
    path("",               views.article_list, name="article_list"),
    path("wiki/<str:id>/", views.article_view, name="article_view"),
    path("wiki/<str:id>/edit", views.article_edit, name="article_edit"),
]