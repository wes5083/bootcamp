from django.db import models


class Department(models.Model):
    title = models.CharField(verbose_name='title', max_length=64)


class UserInfo(models.Model):
    name = models.CharField(verbose_name='user name', max_length=64)
    password = models.CharField(verbose_name='password', max_length=64)
    age = models.IntegerField(verbose_name='age', default=0)
    balance = models.DecimalField(verbose_name='account balance', max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name='create time')

    # depart_id: django auto generate; relate to Department table
    # delete cascade
    depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE)
    # depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.SET_NULL(), null=True, blank=True)

    gender_choices = (
        (1, "male"),
        (2, "femal"),
    )
    gender = models.SmallIntegerField(verbose_name="gender", choices=gender_choices)
