from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import csv
import io
from equities.models import Equity
# Create your views here.
@csrf_exempt
def get_csv_file(request):
    if request.method == "POST":
        if 'filetype' in request.POST and request.POST['filetype'] == "equities":
            file = io.TextIOWrapper(request.FILES['file'])
            reader = csv.DictReader(file)
            for row in reader:
                if Equity.objects.filter(equity_id=row['id']).first():
                    continue
                else:
                    equity = Equity(
                        equity_id=row['id'],
                        equity_name=row['name'],
                        equity_desc=row['description']
                    )
                    equity.save()
                    return HttpResponse("Added Equities")


        return HttpResponse('200')
    if request.method == "GET":
        return HttpResponse("Only Accepts POST Requests")