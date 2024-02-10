from rest_framework import serializers

class serialize_wiki_article_view(serializers.Serializer) :
    title = serializers.CharField(required=True, max_length=150)
    author = serializers.CharField(required=True, max_length=50)
    article_html_content = serializers.CharField(required=True)