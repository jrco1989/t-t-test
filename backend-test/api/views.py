import logging

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserLoginSerializer, UserRegisterSerializer, UserActionLogSerializer,EventUserRegisterSerializer, CommentRegisterSerializer

logger = logging.getLogger('user_actions')

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        cedula = request.data.get("cedula")
        data = {
            "cedula": cedula,
        }
        
        serializer = UserLoginSerializer(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)

        logger.info(f"Login", extra={'user': user})

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "id_user": str(user.id),
        }, status=status.HTTP_200_OK)

class UserRegisterAPIView(APIView):
    print("post")
    permission_classes = [AllowAny]
    def post(self, request):
        print("#######################")
        print(request.data)
        print("#######################")
        cedula = request.data.get("cedula")
        data = {
            "cedula": cedula,
        }

        serializer = UserRegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Registro del usuario {cedula}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserActionLogCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserActionLogSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            user = request.user if request.user.is_authenticated else None
            action = serializer.validated_data.get('action', 'Acción sin especificar')
            
            logger.info(action, extra={'user': user})

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EventUserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    print("tttttttttttt")

    def post(self, request):
        print(request.data)
        print("request")

        serializer = EventUserRegisterSerializer(data=request.data, context={'request': request})
        print("3")

        if serializer.is_valid():
            user = request.user if request.user.is_authenticated else None
            action = serializer.validated_data.get('action', 'Acción sin especificar')
            
            logger.info(action, extra={'user': user})
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CommentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CommentRegisterSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user if request.user.is_authenticated else None
            action = serializer.validated_data.get('action', 'Acción sin especificar')
            
            logger.info(action, extra={'user': user})
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
