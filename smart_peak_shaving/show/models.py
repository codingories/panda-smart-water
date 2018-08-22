from django.db import models


# Create your models here.
class client(models.Model):
    name = models.CharField(max_length=30, default="海南水司调峰系统")
    phone_number = models.CharField(max_length=18, default="13000000000")
    address = models.CharField(max_length=20, default="上海")
    account = models.CharField(max_length=20, default="admin")
    password = models.CharField(max_length=20, default="123456")


class problem_sort(models.Model):
    problem_sort_name = models.CharField(max_length=10, default="全局问题")

class problem_detail(models.Model):
    problem_sort_detail = models.CharField(max_length=15, default="分")

class item_name(models.Model):
    item_name_detail = models.CharField(max_length=15, default="场景模拟")

