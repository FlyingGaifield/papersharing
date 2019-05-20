from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Catalogue, Item

# Create your views here.
def index(request):
    catalogue_list = Catalogue.objects.all()
    context = {'catalogue_list': catalogue_list}
    return render(request, 'share/index.html', context)

def detail(request, catalogue_id):
    try:
    	catalogue = Catalogue.objects.get(pk=catalogue_id)
    	catalogue_list = Catalogue.objects.all()
    	context = {'catalogue_list': catalogue_list, 'catalogue': catalogue}
    	print(catalogue)
    except Catalogue.DoesNotExist:
        raise Http404("Catalogue does not exist")
    return render(request, 'share/detail.html', context)


def add(request):
    a = request.GET['a'] # catalogue
    b = request.GET['b'] # item_name
    c = request.GET['c'] # item_url
    d = request.GET['d'] # item_conf
    e = request.GET['e'] # item_date
    f = request.GET['f'] # item_reader
    g = request.GET['g'] # item_description
    test_repeat = Item.objects.filter(item_name = b)
    catalogue_list = Catalogue.objects.all()
    context = {'catalogue_list': catalogue_list}
    if len(test_repeat) == 1:
        return render(request, 'share/wrong.html', context)
    else:
        catalogue = Catalogue.objects.get(catalogue_text = a)
        create = Item.objects.create(catalogue = catalogue, item_name = b, item_url =c, item_conf = d, item_date =e ,item_reader=f, item_description = g, pub_date = timezone.now())
        return render(request, 'share/result.html', context)