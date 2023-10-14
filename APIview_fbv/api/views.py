from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.
'''
@api_view()         # by default  @api_view(['GET'])
def hello_kapil(request):
	return Response({'msg':'Hello Kapil'})


@api_view(['POST'])
def hello_kapil(request):
	if request.method == 'POST':
		print(request.data)
		return Response({'msg':'post request'})

'''


@api_view(['GET', 'POST'])
def hello_kapil(request):
	if request.method == 'GET':
		return Response({'msg':'get request'})
	if request.method == 'POST':
		print(request.data)
		return Response({'msg':'post request', 'data':request.data})
