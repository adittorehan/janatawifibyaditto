import json
import urllib.request

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from .form import StockDataForm
from .models import StockData
from django.utils.dateparse import parse_date
import locale


def json_to_db():
    url = "https://drive.google.com/u/0/uc?id=15-C8dUTSEwy5bCrVI9ZxYNwHN0ZtY-o-&export=download"
    response = urllib.request.urlopen(url)
    data_list = json.loads(response.read())
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    for data in data_list:
        StockData(
            _date=parse_date(data['date']),
            trade_code=data['trade_code'],
            high=locale.atof(data['high']),
            low=locale.atof(data['low']),
            open=locale.atof(data['open']),
            close=locale.atof(data['close']),
            volume=locale.atoi(data['volume'])
        ).save()


def index(request):
    if StockData.objects.all().count() == 0:
        json_to_db()
    return render(request, 'stockmarketapp/index.html', context={
        'trade_codes': StockData.objects.values_list('trade_code', flat=True).distinct()
    }
                  )


def get_data(request, trade_code=None):
    data_of_trade = StockData.objects.all().order_by('_date', 'id').filter(trade_code=trade_code)
    data = {
        "id": [val.id for val in data_of_trade],
        "trade_code": trade_code,
        "high": [val.high for val in data_of_trade],
        "low": [val.low for val in data_of_trade],
        "open": [val.open for val in data_of_trade],
        "close": [val.close for val in data_of_trade],
        "date": [val.date for val in data_of_trade],
        "volume": [val.volume for val in data_of_trade]
    }
    return JsonResponse(data)


def datapage(request, id):
    form = StockDataForm(instance=get_object_or_404(StockData, id=id))
    if request.method == 'POST':
        print(request)
        form = StockDataForm(request.POST, instance=get_object_or_404(StockData, id=id))
        if form.is_valid():
            form.save()
            return redirect('stockmarketapp:homepage')
    return render(request,
                  'stockmarketapp/dataform.html',
                  context={'data_form': form,
                           'id': id
                           }
                  )


def delete(request, id):
    stock_data = get_object_or_404(StockData, id=id)
    if stock_data is not None:
        stock_data.delete()
    return redirect('stockmarketapp:homepage')


def add_data(request):
    form = StockDataForm()
    if request.method == 'POST':
        form = StockDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stockmarketapp:homepage')
    return render(request,
                  'stockmarketapp/adddata.html',
                  context={
                      'data_form': form,
                      'id': id
                  }
                  )
