import csv

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework import generics

from .serializers import UsersSerializer, OrdersSerializer
from .models import UsersModel, OrdersModel


class CreateVieUser(ListModelMixin, CreateAPIView):
    serializer_class = UsersSerializer
    queryset = UsersModel.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FindVieUser(ListModelMixin, CreateAPIView):
    serializer_class = UsersSerializer

    def get_queryset(self, ):
        params = self.request.query_params
        date_registration = params.get('date_registration', None)
        if not date_registration:
            return UsersModel.objects.all()
        return UsersModel.objects.filter(date_registration=date_registration)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# Парсер CSV
# def handle_files(f):
#     reader = csv.DictReader(open(f))
#     for row in reader:
#         name = row['name']
#         surname = row['surname']
#         date_birth = row['date_birth']
#         date_registration = row['date_registration']
#         order = row['order']
#         my_object = UsersModel(name=name,
#                                surname=surname,
#                                date_birth=date_birth,
#                                date_registration=date_registration,
#                                order=order)
#         my_object.save()
