from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from .serializers import ReminderSerializer

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def create_reminder(request):
    serializer=ReminderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response (serializer.data,status=HTTP_200_OK)
    return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
