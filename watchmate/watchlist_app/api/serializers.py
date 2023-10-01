from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  name = serializers.CharField(read_only=False)
  description = serializers.CharField(read_only=False)
  active = serializers.BooleanField(read_only=False)
  

