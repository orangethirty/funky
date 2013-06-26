from .models import Puli


from django.shortcuts import render_to_response, render
from django.core.urlresolvers import reverse_lazy


def index(request):
    
    return render_to_response('index/index.html')

   
def search(request):
    q = request.GET['query']
    
    return render('search/results/results_list.html', q=q)
   