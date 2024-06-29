from django.shortcuts import render
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Service
from .serializers import ServiceSerializer

# Create your views here.
@api_view(["GET", "POST"])
def list_service(request):
    service = Service.objects.all()
    serializer = ServiceSerializer(service, many=True)
    return Response(serializer.data)

@api_view(["GET", "POST"])
def add_service(request):
    serializer = ServiceSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(["GET", "POST"])
def remove_service(request):
    Service.objects.filter(id=request.data.get("id")).delete()
    return Response("Done")

@api_view(["GET", "POST"])
def update_service(request):
    print(request.data)
    try:
        service = Service.objects.get(id=request.data.get("id"))
    except (Service.DoesNotExist, ValueError):
        raise NotFound(detail="Service not found")
    #serializer = ClientForm(request.data, instance = client)
    serializer = ServiceSerializer(service, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)