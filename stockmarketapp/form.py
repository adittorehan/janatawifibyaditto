from django.forms import ModelForm, DateInput
from .models import StockData


class StockDataForm(ModelForm):
    class Meta:
        model = StockData
        fields = '__all__'
        labels = {
            "_date": "Date"
        }

        widgets = {
            "_date": DateInput(attrs={
                "placeholder": "YYYY-Month-Day, eg. 2022-03-17"
            })

        }


