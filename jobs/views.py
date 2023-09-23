from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated
# Create your views here.
class DemoView(APIView):
     permission_classes = [IsAuthenticated]  #isse bas whi log is token to accesskr skte hai jo authenticated honge. agr isko remove krdiya to sare log dekh payenge.
     def get(self ,request):
         print(request.user)
         return Response({'success' : "Yuy ! you are authenticated"})



class JobView(APIView):
    def get(self,request):
        category = self.request.query_params.get('category')
        if category:
            queryset = Job.objects.filter(category__category_name = category)
        else:
            queryset = Job.objects.all()
        serializer = JobSerializer(queryset , many = True)
        return Response({ 'count' : len(serializer.data) , 'data' :serializer.data })

