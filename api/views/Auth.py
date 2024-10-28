from rest_framework import status
from rest_framework.response import Response
from api.serializers.AuthSerializer import AuthenticationSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

class Auth(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = AuthenticationSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
