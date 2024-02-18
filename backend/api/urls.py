from django.urls import path
from . import views

urlpatterns = [
    path("",               views.article_list, name="article_list"),
    path("wiki/<str:id>/", views.article_view, name="article_view"),
]