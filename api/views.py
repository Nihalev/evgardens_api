from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PlatsSerializer
from .models import Plants


class PlantView(APIView):
    def post(self, request):
        serializer = PlatsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self,reqest,id=None):
        if id:
            item = Plants.objects.get(id=id)
            serializer = PlatsSerializer(item)
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        items = Plants.objects.all()
        serializer = PlatsSerializer(items, many=True)
        # return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.data)
    
    def patch(self,reqest,id=None):
        item = Plants.objects.get(id=id)
        serializer = PlatsSerializer(item,data=reqest.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id=None):
        item =  get_object_or_404(Plants,id=id)
        item.delete()
        return Response({"status":"success","data":"item_deleted"})