from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
	# name = serializers.CharField(read_only=True)                # for single field
	class Meta:
		model = Student
		# fields = ['id', 'name', 'rollno', 'city']
		fields = '__all__'
		# read_only_fields = ['name', 'rollno']              # for multiple fields
		extra_kwargs = {'name':{'read_only':True}}


	# No need to create or define create and update method, ModelSerializer do this work on its own
	# in case of validations, we have to define explicitly
