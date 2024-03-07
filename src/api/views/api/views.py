import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request


class HelloAPIView(APIView):
    def get(self, request: Request):
        return Response({"message": "Hello, world!"})


class DateAPIView(APIView):
    def get(self, request: Request):
        return Response({"date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
