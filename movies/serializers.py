from rest_framework import serializers
from genres.serializers import GenreSerializer
from genres.models import Genre
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "duration",
            "premiere",
            "budget",
            "overview",
            "genres",
        ]

    def create(self, validated_data):
        genres_data = validated_data.pop("genres")

        movie = Movie.objects.create(**validated_data)

        genres_list = [Genre.objects.get_or_create(**genre)[0] for genre in genres_data]

        movie.genres.set(genres_list)

        return movie
