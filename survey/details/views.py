from django.shortcuts import render
from .models import society
from .serializers import societySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class societyAPI(APIView):
    def get(self ,request,format=None, pk=None):
        id=pk
        if id is not None:
            soc=society.objects.get(pk=id)
            serializer=societySerializer(soc)
            return Response(serializer.data, status=status.HTTP_200_OK)
        soc=society.objects.all()
        serializer=societySerializer(soc,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        serializer=societySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'data created'},status=status.HTTP_201_CREATED)

    def put(self,request,pk=None,format=None):
        soc=society.objects.get(id=pk)
        serializer=societySerializer(soc,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'data completely changed'},status=status.HTTP_201_CREATED)

    def patch(self,request,pk=None,format=None):
        soc=society.objects.get(id=pk)
        serializer=societySerializer(soc,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'data partially changed'},status=status.HTTP_201_CREATED)
    
    def delete(self, request,pk=None,format=None):
        soc=society.objects.get(id=pk)
        soc.delete()
        return Response({'msg':'deleted !'})
        