from django.shortcuts import render
from .models import Inventory
from .serializers import InventorySerializer
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.decorators import api_view
from client.models import *
from client.serializers import *
# Create your views here.

@api_view(["POST"])
def add_inv(request):
    serializer = InventorySerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(["POST"])
def remove_inv(request, item_name):
    print(request.data)
    try:
        Inventory.objects.get(item_name=item_name).delete()
    except Inventory.DoesNotExist:
        raise NotFound("Inventory does not exist.")
    return Response("Deleted")

@api_view(["GET", "POST"])
def list_inv(request):
    inv = Inventory.objects.all()
    serializer = InventorySerializer(inv, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def update_inv(request, item_name):
    try:
        inv = Inventory.objects.get(item_name=item_name)
    except Inventory.DoesNotExist:
        raise NotFound("Inventory does not exist")
    serializer = InventorySerializer(inv, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)