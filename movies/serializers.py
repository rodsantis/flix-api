from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None

        
    def validate_release_data(self, value):
        if value.year < 1888:
            raise serializers.ValidationError('The release date year must be greater than 1888')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError("Resume has more words than the allowance. Please keep it under 500 characters.")
        return value