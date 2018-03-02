from django.shortcuts import render
from django.views.generic import FormView, ListView
from django.views.generic.edit import FormMixin
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import viewsets, mixins
from rest_framework.exceptions import APIException

from .forms import Search
from .models import Food
from .serializers import FoodSerializer


class FoodViewSet(mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()


class MissingQueryException(APIException):
    status_code = 400
    default_detail = "must submit query in format of ?query= to search uri"


class SearchViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = FoodSerializer

    def _sort_queries(self, query, string):
        return query.find_string_index(string)

    def get_queryset(self, *args, **kwargs):
        try:
            queries = self.request.query_params['query'].split(' ')
        except MultiValueDictKeyError:
            raise MissingQueryException("must submit query to search uri")
        for query in queries:
            try:
                qs = qs.intersection(
                    Food.objects.filter(description__icontains=query)
                )
            except NameError:
                qs = Food.objects.filter(description__icontains=query)
        qs = sorted(qs, key=lambda x: self._sort_queries(x, queries[0]))
        return qs
