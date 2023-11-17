from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response

from .models import Video
from .serializers import VideoSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def video_list(request):
    if request.method == 'GET':
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return JsonResponse({"videos": serializer.data}, safe=False)
    if request.method == 'POST':
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

