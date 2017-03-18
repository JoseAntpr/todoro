
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import  GenericViewSet

from users.serializers import UserSerializer, UserListSerializer
from users.permissions import UserPermission


class UserViewSet(GenericViewSet):

    permission_classes = (UserPermission, )

    def list(self, request):
        """
        Return a list of the system users
        :param request: HttpRequest
        :return: Response
        """

        users = User.objects.all().values("id","username")
        page = self.paginate_queryset(users)
        serializer = UserListSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def create(self, request):
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

    def retrieve(self, request, pk):
        """
        Return a requested user
        :param request: HttpRequest
        :param pk: user primary key
        :return: Response
        """
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk):
        """
        Updaates a user with the given daa
        :param request: HttpRequest
        :param pk: User primray key
        :return: Response
        """
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        """
        Deletes a user
        :param request: HttpRequest
        :param pk: User primary key
        :return: Response
        """

        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



