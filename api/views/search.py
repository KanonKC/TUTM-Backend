from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..constants import GET,POST,PUT,DELETE
from ..models import *
from rest_framework import status
from ..serializers import QueueSerializer
from django.forms.models import model_to_dict
from ..youtube import search

@api_view([GET])
def video_search(request,query:str):
    print(query)
    return Response({"result": search(query)},status=status.HTTP_200_OK)
