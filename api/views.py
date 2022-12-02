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


class SnippetList(generics.ListCreateAPIView):
    queryset =Student.objects.all()
    serializer_class = StudentSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Student.objects.all()
    serializer_class = StudentSerializer



