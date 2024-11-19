from django.shortcuts import render

from django.http import JsonResponse
from django.shortcuts import render

from .models import (Category, Location, Product, Professional, Specialist,
                     UserBase)


def home(request):
    categories = Category.objects.all()
    professionals = Professional.objects.filter(specialization__name = "Shifokor")[:3]
    users = UserBase.objects.all()
    category = request.GET.get("category")
    
    if category is not None:
        if category == "Shifokor":
            professionals2 = Professional.objects.filter(specialization__name = "Shifokor")[:3]
        else:
            professionals2 = Professional.objects.filter(specialization__name = "Yuristler")[:3]

        professionals3 = []
        for pro in professionals2:
            d = {}
            d['first_name'] = pro.first_name
            d['last_name'] = pro.last_name
            d['location'] = pro.locations.where
            d['image'] = pro.image.url
            d['specialists'] = []
            for s in pro.specialists.all():
                d['specialists'].append(s.name)
            professionals3.append(d)
            
        return JsonResponse({'professionals': professionals3})

    context = {
    "categories": categories,
    "professionals": professionals,
    "users": users,
    }
    return render(request, "page/home.html", context)



def view_more(request):
    what = request.GET.get("what")
    professionals = Professional.objects.filter(specialization__name = what)
    locations = Location.objects.all()
    categories = Specialist.objects.filter(specialization = what.replace("ler", "").upper())
    context = {
        "what": what,
        "professionals": professionals,
        "locations": locations,
        "categories": categories
    }
    return render(request, "page/view_more.html", context)

def apte_kar(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "page/aptekar.html", context)
