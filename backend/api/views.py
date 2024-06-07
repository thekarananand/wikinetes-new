from rest_framework import status

from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import serialize_article_list, serialize_article_view, serialize_article_edit
from .mongo_interface import fetch_article_list, fetch_article_view, fetch_article_edit, update_article

@api_view(['GET'])
def ping(request):
    return Response( {'ping': 'pong'} )

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

@api_view(['GET', 'PUT', 'OPTIONS'])
def article_edit(request, id):
    if request.method == 'GET':
        article_edit_data = serialize_article_edit( data=fetch_article_edit(id) )
        if article_edit_data.is_valid():
            return Response(article_edit_data.data)

    elif request.method == 'PUT':
        article_edit_data = serialize_article_edit( data=request.data )
        print(request.data)
        if article_edit_data.is_valid():
            update_article(id, article_edit_data.data)
            return Response(article_edit_data.data, status=status.HTTP_201_CREATED)
        # return Response(article_edit_data.errors, status=status.HTTP_201_CREATED)
        return Response(article_edit_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Response(markdown.error)
