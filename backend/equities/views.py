from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import csv
import io
from equities.models import Equity,returns
import datetime
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
        if 'filetype' in request.POST and request.POST['filetype'] == 'returns':
            file = io.TextIOWrapper(request.FILES['file'])
            reader = csv.DictReader(file)
            for row in reader:
                if not Equity.objects.filter(equity_id=row['equity_id']).first():
                    
                    continue
                if returns.objects.filter(equity=Equity.objects.filter(equity_id=row['equity_id']).first(),date=datetime.datetime.strptime(row['date'],'%Y-%m-%d')).first():
                    continue
                returns_obj = returns(
                    equity = Equity.objects.filter(equity_id=row['equity_id']).first(),
                    open = row['open'],
                    close = row['close'],
                    day_return = row['returns'],
                    date = datetime.datetime.strptime(row['date'],'%Y-%m-%d')
                )
                returns_obj.save()
                print('Saved')
            return HttpResponse("Added Returns")

                    


        return HttpResponse('200')
    if request.method == "GET":
        return HttpResponse("Only Accepts POST Requests")