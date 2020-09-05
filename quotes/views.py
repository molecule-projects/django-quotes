from django.shortcuts import render

from .models import Quote  # new


def home_page_view(request):
    template_name = 'quotes/home.html'
    queryset = Quote.objects.all()  # new
    # new
    context = {
        'object_list': queryset
    }
    return render(request, template_name, context)  # new


def about_page_view(request):
    template_name = 'quotes/about.html'
    return render(request, template_name)
