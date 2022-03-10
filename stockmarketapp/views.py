import json
import urllib

from django.shortcuts import render


# Json link: https://drive.google.com/u/0/uc?id=15-C8dUTSEwy5bCrVI9ZxYNwHN0ZtY-o-&export=download


def index(request):
    url = "https://drive.google.com/u/0/uc?id=15-C8dUTSEwy5bCrVI9ZxYNwHN0ZtY-o-&export=download"
    response = urllib.request.urlopen(url)
    data_list = json.loads(response.read())
    return render(request, 'stockmarketapp/index.html', context={'data_list': data_list})
