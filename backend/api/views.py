from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import serialize_wiki_article_view

from .sample_data import sampledata

@api_view(['GET'])
def wiki_article_view(request): 
    requested_article = serialize_wiki_article_view (data=sampledata)
    
    if requested_article.is_valid():
        return Response(requested_article.data)
    return Response(requested_article.errors)