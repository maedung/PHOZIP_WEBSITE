from django.shortcuts import render, HttpResponse
def index(request):
    return render(request, "PHO_ZIP_APP/home.html")

def phozipmenu(request):
    return render(request, "PHO_ZIP_APP/daymenu.html")

def phocahmenu(request):
    return render(request, "PHO_ZIP_APP/nightmenu.html")

def drinkmenu(request):
    return render(request, "PHO_ZIP_APP/drinkmenu.html")

def contact(request):
    return render(request, "PHO_ZIP_APP/contact.html")