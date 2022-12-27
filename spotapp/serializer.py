from django.core.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from .models import Artist, Album, Song


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

    
    def validate_name(self, value):
        if len(value) <= 3:
            raise ValidationError(
                message="Ism 3 ta harfdan"
                        " katta bo'lishi kerak")
        return value


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
