from django.db import models


class Record(models.Model):
    date = models.DateField()
    income = models.IntegerField()
    outcome = models.IntegerField()

    def __str__(self):
        return f"収入:{self.income}, 支出:{self.outcome}, 日付:{self.date}"
