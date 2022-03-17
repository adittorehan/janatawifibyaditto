import json
import urllib

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from .form import StockDataForm
from .models import StockData
from django.views.generic.base import TemplateView
from django.utils.dateparse import parse_date
import locale


# Json link: https://drive.google.com/u/0/uc?id=15-C8dUTSEwy5bCrVI9ZxYNwHN0ZtY-o-&export=download

# For Storing the data into the mysql server:
# locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
#     for data in data_list:
#         StockData(
#             date=parse_date(data['date']),
#             trade_code=data['trade_code'],
#             high=locale.atof(data['high']),
#             low=locale.atof(data['low']),
#             open=locale.atof(data['open']),
#             close=locale.atof(data['close']),
#             volume=locale.atoi(data['volume'])
#         ).save()

# Homepage
def index(request):
    paginator = Paginator(StockData.objects.all().order_by('_date', 'id'), 30)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'stockmarketapp/index.html', context={'page_obj': page_obj})


# Get Stock Data as JSON for chart

def get_data(request):
    close = []
    # To store unique date only
    date = []
    volume = []
    trade_code = []
    stock_data = StockData.objects.all().order_by('_date', 'id')
    for value in stock_data:
        close.append(value.close)
        volume.append(value.volume)
        date.append(value.date)
        trade_code.append(value.trade_code)
    date = list(date)
    date.sort()

    # Tried to draw chart by total value for a specific field but in mixed chart close and
    # volume values have too much difference, so I did not proceed because the chart becomes worse than this
    # for s_date in date:
    #     t_close = 0
    #     t_volume = 0
    #     for s_data in StockData.objects.filter(_date=s_date):
    #         t_close += s_data.close
    #         t_volume += s_data.volume
    #     close.append(t_close)
    #     volume.append(t_volume)

    data = {
        "close": close,
        "date": date,
        "trade_code": trade_code,
        "volume": volume

    }
    return JsonResponse(data)


# Edit Stock Data
def datapage(request, id):
    form = StockDataForm(instance=get_object_or_404(StockData, id=id))
    if request.method == 'POST':
        print(request)
        form = StockDataForm(request.POST, instance=get_object_or_404(StockData, id=id))
        if form.is_valid():
            form.save()
    return render(request,
                  'stockmarketapp/dataform.html',
                  context={'data_form': form,
                           'id': id
                           }
                  )


def delete(request, id):
    stock_data = get_object_or_404(StockData, id=id)
    if stock_data is None:
        stock_data.delete()
    return redirect('stockmarketapp:homepage')


# Add New Stock Data
def add_data(request):
    form = StockDataForm()
    if request.method == 'POST':
        form = StockDataForm(request.POST, instance=get_object_or_404(StockData, id=id))
        if form.is_valid():
            form.save()
    return render(request,
                  'stockmarketapp/adddata.html',
                  context={'data_form': form,
                           'id': id
                           }
                  )
