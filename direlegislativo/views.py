from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import serializers
from direlegislativo.models import Person

def get_serializer(model):
    serializerMeta = type(str("Meta"),(),{"fields": "__all__","model": model })
    serializer = type(str("importer"),(serializers.HyperlinkedModelSerializer,),{"Meta": serializerMeta})
    return serializer


class PersonViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
    queryset = Person.objects.all()
    serializer_class = get_serializer(Person)
