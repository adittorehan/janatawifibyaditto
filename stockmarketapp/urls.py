from unicodedata import name
from django.urls import path
from . import views

app_name = 'stockmarketapp'
urlpatterns = [
    path('', views.index, name='homepage'),
    path('dataform/<int:id>', views.datapage, name='dataform'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('adddata/', views.add_data, name='add_data'),
    path('chart-data/<trade_code>', views.get_data, name='chart-data')
]
