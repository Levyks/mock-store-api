from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializers import UserSerializer


class CsrfView(APIView):
    def get(self, request):
        return Response({'X-CSRFTOKEN': get_token(request)})


class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return Response(UserSerializer(user).data)

        else:
            return Response({'detail': 'Invalid credentials.'}, status=400)


class LogoutView(APIView):

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'detail': 'Not logged in.'}, status=400)

        logout(request)
        return Response({'detail': 'Successfully logged out.'})

class ChangePasswordView(APIView):

    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):

        old_password = request.data['old_password']
        if not request.user.check_password(old_password):
            return Response({'detail': 'Incorrect password.'}, status=400)

        if not request.user.can_change_password:
            return Response({'detail': 'The password of this user cannot be changed.'}, status=403)

        request.user.set_password(request.data['new_password'])
        request.user.save()

        return Response({'detail': 'Password changed.'})


class WhoAmIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, format=None):
        return Response(UserSerializer(request.user).data)
