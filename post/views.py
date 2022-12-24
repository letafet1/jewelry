from django.shortcuts import render
from .models import Prods, Category
from rest_framework import generics



def index_view(request):
    prods= Prods.objects.order_by("id")
    context={
        "prods": prods
    }
    return render(request,"index.html",context)

