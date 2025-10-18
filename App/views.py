from multiprocessing import context
from typing import Container
from django.shortcuts import render, HttpResponse
from datetime import datetime
from App.models import Contact
#dict

from bs4 import BeautifulSoup
import requests




# Create your views here.
def index(request):
    context = {
        'variable':"Aj is great"
    }
    return render(request, 'index.html',context)
   # return HttpResponse("<h1>this is home page</h1>")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("<h1>this is about page</h1>")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("<h1>this is services page</h1>")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, phone=phone, email=email, desc=desc, date= datetime.today())
        contact.save()

    
       
    return render(request, 'contact.html')
    #return HttpResponse("<h1>this is contact page</h1>")

# dict
def home(request):
    if request.method == "POST":
        word = request.POST['word']
        url = 'https://www.dictionary.com/browse/'+word
        r = requests.get(url)
        data = r.content
        soup = BeautifulSoup(data, 'html.parser')
        span = soup.find_all('span', {"class": "one-click-content"})

        param = {'text': span[0].text, 'word': word}
        return render(request, 'index.html', param)
    else:
        return render(request, 'index.html')
