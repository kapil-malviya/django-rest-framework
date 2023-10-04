from rest_framework import serializers
from .models import Manager


class ManagerSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=88)
	email = serializers.EmailField(max_length=88)
	age = serializers.IntegerField()
	city = serializers.CharField(max_length=88)


	def create(self, validated_data):
		return Manager.objects.create(**validated_data)