from django.shortcuts import render

from .models import Quote


def home_page_view(request):
    template_name = 'quotes/home.html'
    queryset = Quote.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, template_name, context)


def about_page_view(request):
    template_name = 'quotes/about.html'
    return render(request, template_name)
