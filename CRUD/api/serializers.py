from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=100)
	rollno = serializers.IntegerField()
	city = serializers.CharField(max_length=100)

	def create(self, validated_data):
		return Student.objects.create(**validated_data)

	def update(self, instance, validated_data):
		print('before instance name : ', instance.name)
		instance.name = validated_data.get('name', instance.name)
		print('after instance name : ', instance.name)
		instance.rollno = validated_data.get('rollno', instance.rollno)
		instance.city = validated_data.get('city', instance.city)
		instance.save()
		return instance

	# no need to create method for delete specifically