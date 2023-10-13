from rest_framework import serializers
from .models import Student



# Validators (for reuse)
def start_with_r(value):
	if value[0].lower() != 'r':
		raise serializers.ValidationError('name must start with "r".')



class StudentSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=100, validators=[start_with_r])
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


	# Field level validation
	def validate_rollno(self, value):
		if value >= 200:
			raise serializers.ValidationError('Seat full')
		return value


	# object level validation for multiple fields
	def validate(self, data):
		nm = data.get('name')
		ct = data.get('city')
		if nm.lower() == 'rohit' and ct.lower() != 'dilli':
			raise serializers.ValidationError('for rohit city must be dilli')
		return data



# priority for validations : 

#  Validators > Field level validations > Object level