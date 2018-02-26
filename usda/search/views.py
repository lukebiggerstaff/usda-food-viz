from django.shortcuts import render
from django.views.generic import FormView, ListView
from django.views.generic.edit import FormMixin

from .forms import Search
from .models import Food

# Create your views here.

class Home(FormView):
    form_class = Search
    template_name = 'search/home.html'

class Search(ListView, FormMixin):
    form_class = Search
    model = Food
    template_name = 'search/food_list.html'

    def sort_queries(self, query, string):
        return query.find_string_index(string)

    def get_queryset(self, *args, **kwargs):
        queries = self.request.GET['query'].split(' ')
        for query in queries:
            try:
                qs = qs.intersection(
                    Food.objects.filter(description__icontains=query)
                )
            except NameError:
                qs = Food.objects.filter(description__icontains=query)
        qs = sorted(qs, key=lambda x: self.sort_queries(x, queries[0]))
        return qs
