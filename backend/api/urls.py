from django.urls import path
from . import views

urlpatterns = [
    path("", views.article_list, name="article_list"),
    path("<int:id>/", views.wiki_article_view, name="wiki_article_view"),
]