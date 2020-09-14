from rest_framework import  serializers
from .models import Post, Article, Club

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class ClubSerializer(serializers.ModelSerializer):
	class Meta:
		model = Club
		fields = '__all__'