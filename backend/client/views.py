from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import NotFound
from utils.serializers import LimitOffsetPaginationSerializer
from django.shortcuts import get_object_or_404

@api_view(["GET"])
#@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def get_client(request, id):
    try:
        client = Client.objects.get(id=id)
        return Response(ClientSerializer(client).data)
    except Client.DoesNotExist:
        raise NotFound(detail="User not found")

@api_view(["POST"])
def update_client(request, id):
    try:
        client = Client.objects.get(id=id)
    except Client.DoesNotExist:
        raise NotFound(detail="User not found")
    #serializer = ClientForm(request.data, instance = client)
    serializer = ClientSerializer(client, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(["GET"])
#@authentication_classes([SessionAuthentication])
#@permission_classes([IsAuthenticated])
def list_client(request):
    serializer = LimitOffsetPaginationSerializer(data=request.query_params)
    if serializer.is_valid(raise_exception=True):
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(Client.objects.all(), request)
        serializer = ClientSerializer(result_page, many=True, context={'request':request})
        print(serializer.data)
        return paginator.get_paginated_response(serializer.data)


@api_view(["POST"])
#@permission_classes([IsAuthenticated])
def create_client(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(["GET"])
def get_allergy(request, id):
    try:
        client = Client.objects.get(id=id)
    except Client.DoesNotExist:
        raise NotFound(detail="User not found")
    #serializer = ClientForm(request.data, instance = client)
    return Response(client.allergy)

@api_view(["POST"])
def add_allergy(request, id):
    try:
        client = Client.objects.get(id=id)
    except Client.DoesNotExist:
        raise NotFound(detail="User not found")
    serializer = AllergyRequestSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.validated_data)
        allergy = Allergy.objects.get_or_create(allergy=serializer.data.get("allergy"))[0]
        ClientAllergy.objects.create(client=client, allergy=allergy)
        return Response(AllergySerializer(allergy).data)

@api_view(["POST"])
def remove_allergy(request, id):
    try:
        client = Client.objects.get(id=id)
    except Client.DoesNotExist:
        raise NotFound(detail="User not found")
    #obj = ClientAllergy.objects.get(client=client, **request.data)
    print(request.data)
    serializer = AllergyRequestSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        ClientAllergy.objects.filter(client=client, allergy=request.data.get("allergy")).delete()
        return Response("ok")

@api_view(["GET"])
def get_medhist(request, id):
    try:
        client = Client.objects.get(id=id)
    except Client.DoesNotExist:
        raise NotFound(detail="User not found")
    return Response(client.medhist)

@api_view(["POST"])
def add_medhist(request, id):
    try:
        client = Client.objects.get(id=id)
    except Client.DoesNotExist:
        raise NotFound(detail="User not found")
    
    mutable_data = request.data.copy()
    mutable_data['client'] = client.id

    serializer = MedHistSerializer(data=mutable_data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
