from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from applications.movie.models import Movie, Relation, Like
from applications.movie.permissions import IsOwner, IsRelationOwner
from applications.movie.serializers import MovieSerializer, RelationSerializer


# Create your views here.


class MovieApiView(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsOwner]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['owner']
    search_fields = ['title']
    ordering_fields = ['title']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RelationApiView(mixins.UpdateModelMixin, GenericViewSet):
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer
    permission_classes = [IsRelationOwner]
    lookup_field = 'movie'  # чтобы пользователь не нужно было передавать id фильма

    def get_object(self):
        obj = Relation.objects.get_or_create(owner=self.request.user, movie_id=self.kwargs['movie'])
        return obj


class LikeApiView(mixins.UpdateModelMixin, GenericViewSet):
    queryset = Like.objects.all()
    serializer_class = RelationSerializer
    permission_classes = [IsRelationOwner]
    lookup_field = 'movie'  # чтобы пользователь не нужно было передавать id фильма

    def get_object(self):
        obj = Like.objects.get_or_create(owner=self.request.user, movie_id=self.kwargs['movie'])
        return obj
