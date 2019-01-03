from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from .serializer import file_serializer

class file_upload_view(APIView):
    def post(self,request):

        serializer_value = file_serializer(data=request.data)
        if serializer_value.is_valid():
            serializer_value.save()
            return Response(serializer_value.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_value.data,status=status.HTTP_404_BAD_REQUEST)    

