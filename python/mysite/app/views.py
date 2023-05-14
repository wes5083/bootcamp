from django.shortcuts import render, HttpResponse

def index(request):
    # return HttpResponse("success")
    return render(request, "index.html")
