from django.db import models


class StockData(models.Model):
    _date = models.DateField(db_column='date')
    trade_code = models.CharField(max_length=25)
    high = models.FloatField()
    low = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()

    @property
    def date(self):
        return str(self._date)
