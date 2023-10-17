from rest_framework import serializers
from .models import Student
 
# Create a serializer for the Student model
class StudentSerializer(serializers.ModelSerializer):
    # Custom validator for checking if the name starts with 'r'
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name must start with "r".')

    # Define the 'name' field with the 'start_with_r' validator
    name = serializers.CharField(validators=['start_with_r'])

    class Meta:
        model = Student
        # Define the fields to include in the serialization
        # You can use '__all__' to include all fields, or specify them individually
        fields = ['id', 'name', 'rollno', 'city']

    # Field-level validation for the 'rollno' field
    def validate_rollno(self, value):
        # Check if the roll number is greater than or equal to 200
        if value >= 200:
            raise serializers.ValidationError('Seat full')
        return value

    # Object-level validation for multiple fields
    def validate(self, data):
        # Get the 'name' and 'city' values from the data dictionary
        nm = data.get('name')
        ct = data.get('city')

        # Check if the name is 'rohit' and the city is not 'dilli'
        if nm.lower() == 'rohit' and ct.lower() != 'dilli':
            raise serializers.ValidationError('For Rohit, city must be "dilli"')

        return data
