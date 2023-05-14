from django.shortcuts import render

from django.shortcuts import render, HttpResponse,redirect


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


def news(request):
    # GET method & POST method & request params
    print(request.method)
    print(request.GET)  # get request get params
    print(request.POST) # get request post params

    # response a content
    # return HttpResponse("This is content response")

    # response URL, redirect
    # return redirect("https://www.google.com")

    # response a page
    return render(request, "news.html",{"title":"This is a title"})
