from django.shortcuts import render
from django.shortcuts import HttpResponse # changes by Muhammad Shoaib Sikander
from django.views.generic import TemplateView # changes by Muhammad Shoaib Sikander

# Create your views here.

def home_page(request):
    return HttpResponse('***** Welcome to Home Page *****')

class page_1(TemplateView):
    template_name = 'pages/page_1.html'

def page_2(request):
    return render(request, 'pages/page_2.html')

def page_3(request):
    return HttpResponse('You are on Page 3')
