from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>/", views.wiki_article_view, name="wiki_article_view"),
]