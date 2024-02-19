from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import  Admins, Books, Airplanes, Airports, Flights, Passports, Users
from .serializers import AdminsSerializer, BooksSerializer
from rest_framework.parsers import JSONParser

# Create your views here.

def admin(request):
    if request.method == 'GET':
        snippets = Admins.objects.all()
        serializer = AdminsSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdminsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
