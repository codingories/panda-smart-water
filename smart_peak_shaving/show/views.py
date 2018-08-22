from django.shortcuts import render
from .models import *


# Create your views here.
def show_0(request):
    problem_list = problem_detail.objects.all()
    # print(problem_list)
    # for pl in problem_list:
    #     print(pl.problem_sort_detail)
    # print(locals())
    return render(request, 'show_0.html', {'problem_list': problem_list})
