from django.contrib.auth.models import User, Group, Permission
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password

# Create your views here.
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from app.serializer import UserSerializer, GroupSerializer, PermissionSerializer, UserSerializerDepth, \
    ContentTypeSerializer, ContentType


class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializerDepth


class UserCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            validate_password(password=data['password'], user=User)
            data['password'] = make_password(data['password'])
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse(JSONRenderer().render(serializer.data), content_type='application/json',
                                    status=status.HTTP_201_CREATED)
            return HttpResponse(JSONRenderer().render(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return HttpResponse(JSONRenderer().render({"Error": str(e)}), content_type='application/json',
                                status=status.HTTP_400_BAD_REQUEST)


class UserRUD(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'username'
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        try:
            data = request.data
            if 'password' in data.keys():
                validate_password(password=data['password'], user=User)
                data['password'] = make_password(data['password'])
            user = User.objects.get(username__exact=data['username'])
            serializer = UserSerializer(user, data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse(JSONRenderer().render(serializer.data), content_type='application/json')
            return HttpResponse(JSONRenderer().render(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return HttpResponse(JSONRenderer().render({"Error": str(e)}), content_type='application/json',
                                status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        try:
            data = request.data
            if 'password' in data.keys():
                validate_password(password=data['password'], user=User)
                data['password'] = make_password(data['password'])
            user = User.objects.get(username__exact=data['username'])
            serializer = UserSerializer(user, data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse(JSONRenderer().render(serializer.data), content_type='application/json')
            return HttpResponse(JSONRenderer().render(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return HttpResponse(JSONRenderer().render({"Error": str(e)}), content_type='application/json',
                                status=status.HTTP_400_BAD_REQUEST)


class GroupLC(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Group.objects.all().order_by('-id')
    serializer_class = GroupSerializer


class GroupRUD(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Group.objects.all().order_by('-id')
    serializer_class = GroupSerializer


class PermissionsLC(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Permission.objects.all().order_by('-id')
    serializer_class = PermissionSerializer


class ContentTypeLC(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = ContentType.objects.all().order_by('-id')
    serializer_class = ContentTypeSerializer


class CheckPermission(APIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    def post(self, request, *args, **kwargs):
        try:
            # user = UserSerializerDepth(User.objects.get(username__exact=request.user)).data
            permission = Permission.objects.get(codename__exact=request.data['permission'])
            user = User.objects.filter(Q(username__exact=request.user) & (Q(groups__permissions__in=[permission.id]) |
                                                                          Q(user_permissions__in=[permission.id])))
            if user:
                return HttpResponse(JSONRenderer().render({"details": "Permission granted"}),
                                    content_type='application/json')
            return HttpResponse(JSONRenderer().render({"details": "Permission denied"}),
                                status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return HttpResponse(JSONRenderer().render({"Error": str(e)}), content_type='application/json',
                                status=status.HTTP_400_BAD_REQUEST)
