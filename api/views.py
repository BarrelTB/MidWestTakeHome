import json
# from django.http import JsonResponse
from django.forms.models import model_to_dict
from home.models import LoremIpsum, Contact
from rest_framework.response import Response
from rest_framework.decorators import api_view
from home.serializers import ContactSerializer, LoremIpsumSerializer

@api_view(["GET"])
def get_lorem_ipsum_content(request, *args, **kwargs):
    instance = LoremIpsum.objects.all()
    data = {}
    if instance:
        data = [LoremIpsumSerializer({'id' : item.id, 'title' : item.title, 'text' : item.text, 'img' : item.img}).data for item in instance]
        #data = LoremIpsumSerializer(instance).data
    return Response(data)

@api_view(["POST"])
def post_contact_message(request, *args, **kwargs):
    serializer =  ContactSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.save()
        return Response(serializer.data)