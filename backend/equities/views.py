from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import csv
import io
# Create your views here.
@csrf_exempt
def get_csv_file(request):
    if request.method == "POST":
        file = io.TextIOWrapper(request.FILES['file'])
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
        return HttpResponse('200')
    if request.method == "GET":
        return HttpResponse("Only Accepts POST Requests")