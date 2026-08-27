from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPermissions
from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer