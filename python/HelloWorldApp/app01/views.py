from django.shortcuts import render

from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Welcome")


def user_list(request):
    name = "Wes"
    roles = ["admin", "guest"]
    user = {"name": "Wes", "salary": 1000, "role": "admin"}
    user_lists = [
        {"name": "Wes1", "salary": 1000, "role": "admin"},
        {"name": "Wes2", "salary": 2000, "role": "guest"},
        {"name": "Wes3", "salary": 3000, "role": "admin"},

    ]
    return render(request, "user_list.html", {"name": name, "role": roles, "user": user,"user_lists":user_lists})


def user_add(request):
    return render(request, "user_add.html")
