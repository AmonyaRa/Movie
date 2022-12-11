from rest_framework import serializers

from applications.movie.models import Movie, Relation


class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(
        source='owner.username')  # выводит owner (имя), если хотим через id, то вместо username можете написать id

    class Meta:
        model = Movie
        fields = '__all__'


class RelationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(
        source='owner.username')

    class Meta:
        model = Movie
        fields = ['movie', 'rating']

    def to_representation(self, instance):
        rate = super().to_representation(instance)
        rep = list(map(lambda x: sum(x) // len(x), rate.get('rating')))
        return rep


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(
        source='owner.username')

    class Meta:
        model = Movie
        fields = ['movie', 'like']
