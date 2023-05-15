from django.shortcuts import render,HttpResponse


def depart_list(request):
    return render(request, "depart_list.html")
