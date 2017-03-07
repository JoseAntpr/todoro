
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.serializers import UserSerializer


class UsersApi(APIView):

    def get(self, request):
        """
        Return a list of the system users
        :param request: HttpRequest
        :return: Response
        """

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request):
        """
        create a user
        :param request: HttpRequest
        :return: Response
        """

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailApi(APIView):
    """
    User detail (GET), updated user(PUT), delete(DELETE)
    """

    def get(self, request, pk):
        """
        Return a requested user
        :param request: HttpRequest
        :param pk: user primary key
        :return: Response
        """
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Updaates a user with the given daa
        :param request: HttpRequest
        :param pk: User primray key
        :return: Response
        """
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Deletes a user
        :param request: HttpRequest
        :param pk: User primary key
        :return: Response
        """

        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



