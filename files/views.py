from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("hello there")

def files(request):
    # we want to  render our teplate here and send it to the user
    return render(request,'files/files.html', {'data': 'whats in la la lan'})
