from django.shortcuts import render,HttpResponse
from html5lib import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import students
from .serializers import studentsSerializer

# Create your views here.
class studentList(APIView):
    def get(self,request):
        students1 = students.objects.all()
        serializer = studentsSerializer(students1,many=True)
        return Response(serializer.data)
        
    def post(self):
        pass

def studentData(request):
    import requests
    import json
    ans = requests.get('http://127.0.0.1:8000/')
    return HttpResponse(ans.content)