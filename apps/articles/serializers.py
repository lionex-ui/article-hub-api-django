from typing import Any

from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author_id = serializers.IntegerField(source="author.id", read_only=True)
    author_username = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Article
        fields = ["id", "title", "content", "tags", "author_id", "author_username", "created_at"]

    # noinspection PyMethodMayBeStatic
    def validate_tags(self, tags: Any) -> list[str]:
        if not isinstance(tags, list):
            raise serializers.ValidationError("Tags must be a list.")

        return tags

    def create(self, validated_data: dict) -> Article:
        user = self.context["request"].user
        return Article.objects.create(author=user, **validated_data)
