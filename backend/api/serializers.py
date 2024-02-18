from rest_framework import serializers

class serialize_article_list(serializers.Serializer):
    id = serializers.CharField(required=True, max_length=24)
    title = serializers.CharField(required=True, max_length=150)
    author = serializers.CharField(required=True, max_length=150)

class serialize_article_view(serializers.Serializer) :
    title = serializers.CharField(required=True, max_length=150)
    author = serializers.CharField(required=True, max_length=50)
    html_content = serializers.CharField(required=True)
    table_of_content = serializers.ListField()