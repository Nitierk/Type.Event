from django.http import HttpResponse
from django.shortcuts import render

def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    elif request.method == "POST":
        return HttpResponse('Testando')