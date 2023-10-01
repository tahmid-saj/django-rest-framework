from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  name = serializers.CharField(read_only=False)
  description = serializers.CharField(read_only=False)
  active = serializers.BooleanField(read_only=False)

  def create(self, validated_data):
    return Movie.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.description = validated_data.get('description', instance.description)
    instance.active = validated_data.get('active', instance.active)
    instance.save()

    return instance

