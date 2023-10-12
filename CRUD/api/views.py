from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
import io 
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.


@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        idd = pythondata.get('id', None)
        if idd is not None:
            stu = Student.objects.get(id=idd)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            response = {'msg': 'Data Created'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')


    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        idd = pythondata.get('id')
        stu = Student.objects.get(id=idd)
        serializer = StudentSerializer(stu, data=pythondata, partial=True)   # if partial=True is not there then, it'll require all feilds
        if serializer.is_valid():
            serializer.save()
            response = {'msg': 'Data Updated'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'DELETE':
    	json_data = request.body
    	stream = io.BytesIO(json_data)
    	pythondata = JSONParser().parse(stream)
    	idd = pythondata.get('id') 
    	stu = Student.objects.get(id=idd)
    	stu.delete()
    	response = {'msg':'Data Deleted'}
    	json_data = JSONRenderer().render(response)
    	return HttpResponse(json_data, content_type='application/json')
    	# return JsonResponse(response, safe=False)
