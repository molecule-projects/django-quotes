from django.urls import path

from .views import home_page_view, about_page_view  # new

app_name = 'quotes'

urlpatterns = [
    path('home/', home_page_view, name='home'),
    path('about/', about_page_view, name='about'),  # new
]
