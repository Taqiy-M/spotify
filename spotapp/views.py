from django.shortcuts import render

# Create your views here.
from rest_framework import status, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Artist, Album
from .serializer import ArtistSerializer, AlbumSerializer


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'autobiography']
    ordering_fields = ['name']
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     a = self.kwargs.get('pk')
    #     if not a:
    #         return Artist.objects.all()
    #     return Artist.objects.filter(id=a)

    @action(methods=['get'], detail=False)
    def pop(self, request):
        artists = Artist.objects.filter(genre='Pop')
        ser = ArtistSerializer(artists, many=True)
        return Response(ser.data)


    @action(methods=['get', 'post'], detail=True)
    def albums(self, request, pk=None):
        if request.method == 'POST':
            data = request.data
            ser = AlbumSerializer(data=data)
            if ser.is_valid():
                ser.save()
                oxirgi = Album.objects.last()
                oxirgi.artist.add(self.get_object())

                oxirgi.save()
                return Response(ser.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        qoshiqchi = Artist.objects.get(id=pk)
        albums = Album.objects.filter(artist=qoshiqchi)
        ser = AlbumSerializer(albums, many=True)
        return Response(ser.data)







