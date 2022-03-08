from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('hihihihi')

#-------------------------------------------

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import WorkoutClass, Member, MemberCredit, Booking
from app.serializers import WorkoutClassSerializer

@api_view(['GET', 'POST'])
def workoutclass_list(request):
    """
    List all workout classes, or create a new workout class
    """

    if request.method == 'GET':
        workout_class = WorkoutClass.objects.all()
        serializer = WorkoutClassSerializer(workout_class, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WorkoutClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
