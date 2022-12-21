from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    critic = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = [
            "id",
            "stars",
            "review",
            "spoilers",
            "movie_id",
            "critic",
        ]
        read_only_fields = ["movie_id", "critic"]

    def get_critic(self, obj):
        return {
            "id": obj.critic.id,
            "first_name": obj.critic.first_name,
            "last_name": obj.critic.last_name,
        }
