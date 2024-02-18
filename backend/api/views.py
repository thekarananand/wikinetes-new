from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import     serialize_article_list, serialize_article_view
from .mongo_interface import     fetch_article_list,     fetch_article_view, fetch_markdown

@api_view(['GET'])
def article_list(request):
    article_list = serialize_article_list(data=fetch_article_list(), many=True)
    if article_list.is_valid():
        return Response(article_list.data)
    return Response(article_list.errors)

@api_view(['GET'])
def article_view(request, id): 
    requested_article = serialize_article_view(data=fetch_article_view(id=id))
    if requested_article.is_valid():
        return Response(requested_article.data)
    return Response(requested_article.errors)