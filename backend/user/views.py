from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, BasePermission
from rest_framework.pagination import LimitOffsetPagination
from utils.serializers import LimitOffsetPaginationSerializer
from rest_framework.exceptions import NotFound, AuthenticationFailed



# Create your views here.
@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    print(username, password)
    user = authenticate(request, username=username, password=password)
    print(user)
    if user is not None:
        login(request, user)
        # set user-specific data in the session
        request.session['username'] = username
        request.session.save()
        return Response("Complete")
    raise AuthenticationFailed("Invalid details.");

@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response("Sucess!")

@api_view(["GET"])
#@authentication_classes([SessionAuthentication])
#@permission_classes([IsAuthenticated])
@permission_classes([AllowAny])
def whoami(request):
    user = request.user
    if not request.user.is_authenticated:
        return JsonResponse({"is_authenticated": False})
    else:
        return JsonResponse({"is_authenticated": True, "user": UserSerializer(user).data}) 

@api_view(["GET"])
def list_user(request):
    #serializer = UserSerializer(User.objects.all(), many=True)
    #return Response(serializer.data)
    serializer = LimitOffsetPaginationSerializer(data=request.query_params)
    if serializer.is_valid(raise_exception=True):
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(User.objects.all(), request)
        serializer = UserSerializer(result_page, many=True, context={'request':request})
        print(serializer.data)
        return paginator.get_paginated_response(serializer.data)



@api_view(["POST"])
@permission_classes([IsAdminUser])
def register_user(request):
    print(request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

class IsAdminOrOwner(BasePermission):
    message = 'Need to be an admin or the owner.'

    def has_permission(self, request, view):
        id = view.kwargs.get('id', None)
        return request.user.is_superuser or request.user.id == id

@api_view(["POST"])
@permission_classes([IsAdminOrOwner])
def update_user(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        raise NotFound(detail="User not found")
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)