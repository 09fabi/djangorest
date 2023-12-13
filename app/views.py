from django.shortcuts import render
from .serializers import EstudianteSerializer
from .models import Estudiante
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.

#CLASS BASE VIEW

class EstudiantesList(APIView):
    def get(self, request):
        estudi = Estudiante.objects.all()
        serial = EstudianteSerializer(estudi, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial = EstudianteSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Estudiante_detalle_class(APIView):
    def get_object(self, id):
        try:
            return Estudiante.objects.get(pk=id)
        except Estudiante.DoesNotExist:
            return Http404
        
    def get(self, request, id):
        estude = self.get_object(id)
        serial = EstudianteSerializer(estude)
        return Response(serial.data)
    
    def put(self, request, id):
        estude = self.get_object(id)
        serial = EstudianteSerializer(estude, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        estude = self.get_object(id)
        estude.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        
    
    

#FUNCION BASED VIEW

@api_view(['GET', 'POST'])
def estudiantes_list(request):
    if request.method == 'GET':
        estude = Estudiante.objects.all()
        seria = EstudianteSerializer(estude, many=True)
        return Response(seria.data)
    
    if request.method == 'POST':
        seria = EstudianteSerializer(data = request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_201_CREATED)
        return Response(seria.data, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def estudiante_detalle(request, id):
    try:
        estudi = Estudiante.objects.get(pk=id)
    except Estudiante.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = EstudianteSerializer(estudi)
        return Response(serial.data)
    
    if request.method == 'PUT':
        serial = EstudianteSerializer(estudi, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        estudi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)