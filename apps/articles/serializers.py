from rest_framework import serializers

from ..users.models import User
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author_id = serializers.IntegerField(source="author.id", read_only=True)
    author_username = serializers.CharField(source="author.username", read_only=True)

    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        required=False,
    )

    class Meta:
        model = Article
        fields = ["id", "title", "content", "author", "author_id", "author_username", "created_at"]

    def update(self, validated_data: dict, instance: Article) -> Article:
        validated_data.pop("author", None)
        return super().update(validated_data, instance)
