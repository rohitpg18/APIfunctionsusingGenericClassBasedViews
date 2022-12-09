from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from .models import Emp
from .serializers import EmpSerializer
from rest_framework import status
# from rest_framework.permissions import BasePermission
from rest_framework import viewsets
 
class EmpViewSet(viewsets.ViewSet):
    def list(self, request):
        emp = Emp.objects.all()
        serializer = EmpSerializer (emp, many=True)
        return Response(serializer.data)
    
    def retrieve(self , request, pk=None):
        id = pk
        if id is not None:
            emp = Emp.objects.get(id=id)
            serializer = EmpSerializer(emp)
            return Response(serializer.data)

    def create(self, request):
        serializer = EmpSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'New Student Details Added Successfully', 'status':'success', 'candidate':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def update(self, request, pk):
        id = pk
        item = Emp.objects.get(pk=id)
        serializer = EmpSerializer(instance=item , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Student Details updated Successfully', 'candidate':serializer.data})
        return Response(serializer.errors)
    
    def destroy(self, request, pk):
        id=pk
        item = Emp.objects.get(pk=id)
        item.delete()
        return Response({'msg':'Data Deleted'})
    


