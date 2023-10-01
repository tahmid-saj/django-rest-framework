from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse

@api_view(['GET',])
def movie_list(request):
  movies = Movie.objects.all()
  serializer = MovieSerializer(movies, many=True)

  return Response(serializer.data)

@api_view()
def movie_details(request, pk):
  movie = Movie.objects.get(pk=pk)
  data = {
    'name': movie.name,
    'description': movie.description,
    'active': movie.active
  }
  print(movie.name)

  return JsonResponse(data)