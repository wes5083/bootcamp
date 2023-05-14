from app.models import Department, UserInfo
from django.shortcuts import render, HttpResponse, redirect


def index(request):
    # return HttpResponse("success")
    return render(request, "index.html")


def orm(request):
    # add data
    Department.objects.create(title="business")
    Department.objects.create(title="art")
    Department.objects.create(title="technology")

    UserInfo.objects.create(name="Mick", password="123456", age=20)
    UserInfo.objects.create(name="Wes", password="123456", age=20)
    UserInfo.objects.create(name="Mandy", password="123456", age=20)
    UserInfo.objects.create(name="Lucy", password="123456", age=20)

    # delete data
    UserInfo.objects.filter(id=1).delete()

    Department.objects.all().delete()

    # query data

    # data_list = UserInfo.objects.all()
    # print(data_list)
    # for obj in data_list:
    #     print(obj.id, obj.name, obj.password, obj.age)

    data_list = UserInfo.objects.filter(id=1)
    print(data_list)

    data_list = UserInfo.objects.filter(id=1).first()
    print(data_list)

    # update data
    UserInfo.objects.filter(id=2).update(age=50)

    return HttpResponse("success")


def users_list(request):
    users_list = UserInfo.objects.all()
    for item in users_list:
        print(item.id, item.name, item.password, item.age)
    return render(request, "users_list.html", {"users_list": users_list})


def users_add(request):
    if request.method == "GET":
        return render(request, "users_add.html")
    name = request.POST.get("name")
    password = request.POST.get("password")
    age = request.POST.get("age")
    UserInfo.objects.create(name=name, password=password, age=age)
    return redirect("/users/list/")


def users_update(request):
    return render(request, "users_update.html")
