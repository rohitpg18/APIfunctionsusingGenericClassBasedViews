from rest_framework.response import Response
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view


# class StudentView (APIView):
#     def post (self, request, format=None):
#         serializer = StudentSerializer (data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'New Student Details Added Successfully', 'status':'success', 'candidate':serializer.data}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)

#     def get(self, request, format=None):
#         candidates = Student.objects.all()
#         serializer = StudentSerializer(candidates, many=True)
#         return Response({'status':'success', 'candidates':serializer.data}, status=status.HTTP_200_OK)


# class StudentUd(APIView):

#     def put (self, request , id , format=None):
#         item = Student.objects.get(pk=id)
#         serializer = StudentSerializer(instance=item , data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Student Details updated Successfully', 'candidate':serializer.data})
    
#     def delete (self, request, id, format=None):
#         item = Student.objects.get(pk=id)
#         item.delete()
#         return Response ("Student deleted")

from api.models import *
from api.serializers import StudentSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from api.pagination import StudentPagination , StudentOptionalPagination
from rest_framework.permissions import BasePermission
from .resources import StudentResources
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from django.shortcuts import render, redirect

class SnippetList(generics.ListCreateAPIView):
    permission_classes = [BasePermission]
    queryset =Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend , filters.OrderingFilter , filters.SearchFilter]
    filterset_fields = ['name']
    ordering_fields = ['name', 'id', 'phone_number' , 'email']
    search_fields = ['name']
    pagination_class = StudentOptionalPagination


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [BasePermission]
    queryset =Student.objects.all()
    serializer_class = StudentSerializer


def simple_upload (request):
    if request.method == 'POST':
        student_resource = StudentResources()
        dataset = Dataset()
        new_student = request.FILES['myfile']

        imported_data = dataset.load(new_student.read(), format='xlsx')
        for data in imported_data:
            print ((data[1]))
            value = Student(
                data[0],
                data[1],
                data[2],
                data[3],
            )
            value.save()
        return redirect ("student")
    return render (request, 'upload.html')


