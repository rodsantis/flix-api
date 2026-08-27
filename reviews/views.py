from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPermissions
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer