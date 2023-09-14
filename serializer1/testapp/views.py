from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.

# for single student data :

def student_detail(request, xx):
	stu = Student.objects.get(id = xx)
	print('stu : ', stu)
	serializer = StudentSerializer(stu)
	print('serializer : ', serializer)
	print('serializer.data : ', serializer.data)
#	json_data = JSONRenderer().render(serializer.data)
#	print('json_data : ', json_data)
#	return HttpResponse(json_data, content_type='application/json')
	return JsonResponse(serializer.data)  # by default safe=True



# for all student data :
def students(request):
	stu = Student.objects.all()
	serializer = StudentSerializer(stu, many=True)
	json_data = JSONRenderer().render(serializer.data)
	return HttpResponse(json_data, content_type='json')
#	return JsonResponse(serializer.data, safe=False)  # safe=False bcoz data isn't in dict form here