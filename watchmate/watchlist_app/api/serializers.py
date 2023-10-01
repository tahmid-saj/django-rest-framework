from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform



class WatchListSerializer(serializers.ModelSerializer):

  # len_name = serializers.SerializerMethodField()

  class Meta:
    model = WatchList
    fields = "__all__"
    # exclude = ["active"]

class StreamPlatformSerializer(serializers.ModelSerializer):

  # watchlist = WatchListSerializer(many=True, read_only=True)
  # watchlist = serializers.StringRelatedField(many=True)
  watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

  class Meta:
    model = StreamPlatform
    fields = "__all__"


  # def get_len_name(self, object):
  #   length = len(object.name)
  #   return length


  # def validate(self, data):
  #   if data['name'] == data['description']:
  #     raise serializers.ValidationError('Name and description cannot be the same')
  #   else:
  #     return data
    

  # def validate_name(self, value):
  #   if len(value) < 2:
  #     raise serializers.ValidationError('Name is too short')
  #   else:
  #     return value


# def name_length(value):
#   if len(value) < 2:
#     raise serializers.ValidationError('Name is too short')

# class MovieSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only=True)
#   name = serializers.CharField(validators=[name_length])
#   description = serializers.CharField(read_only=False)
#   active = serializers.BooleanField(read_only=False)

#   def create(self, validated_data):
#     return Movie.objects.create(**validated_data)

#   def update(self, instance, validated_data):
#     instance.name = validated_data.get('name', instance.name)
#     instance.description = validated_data.get('description', instance.description)
#     instance.active = validated_data.get('active', instance.active)
#     instance.save()

#     return instance
  
#   def validate(self, data):
#     if data['name'] == data['description']:
#       raise serializers.ValidationError('Name and description cannot be the same')
#     else:
#       return data
    

#   def validate_name(self, value):
#     if len(value) < 2:
#       raise serializers.ValidationError('Name is too short')
#     else:
#       return value


