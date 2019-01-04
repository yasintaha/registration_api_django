from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
import boto3
from botocore.client import Config
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from .models import file_model
from .serializer import file_serializer

class file_upload_view(APIView):
    def get(self,request):
        data_model = file_model.objects.all()
        ser_data  = file_serializer(data_model,many=True)
        return Response(ser_data.data,status=status.HTTP_200_OK)

    def post(self,request):

        serializer_value = file_serializer(data=request.data)
        if serializer_value.is_valid():
            var = serializer_value.save()
            var.key = '/video/'
            key = var.key
            var.save()

            file_name = request.data['file']
            # print(file_name)    

            # Your S3bucket credentials 
            aws_id = ""
            aws_secret = ""
            BUCKET_NAME = ""

            s3 = boto3.resource(
                's3',
                aws_access_key_id=aws_id,
                aws_secret_access_key=aws_secret,
                config=Config(signature_version='s3v4')
            )

            # s3.Bucket(BUCKET_NAME).put_object(Key=key,Body=file_name, ACL="bucket-owner-full-control")



            return Response(serializer_value.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_value.data,status=status.HTTP_404_BAD_REQUEST)    

