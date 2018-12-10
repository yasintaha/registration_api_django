from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Register_model
from app.serializer import Register_Serializer
# Create your views here.

class user_view(APIView):
   
    def get(self,request):
        register_var = Register_model.objects.all()
        serializer_var = Register_Serializer(register_var,many=True)
        return Response(serializer_var.data)

    def post(self,request):
        ser_var = Register_Serializer(data=request.data)
        if ser_var.is_valid():
            ser_var.save()
            return Response(ser_var.data,status=status.HTTP_201_CREATED)
        else:
            return Response(ser_var.data,status=status.HTTP_400_BAD_REQUEST)
     