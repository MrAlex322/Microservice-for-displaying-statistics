from django.db import models


class Statistics(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(unique=False)
    views = models.IntegerField(null=True, blank=True)
    clicks = models.IntegerField(null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.5)
    cpc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cpm = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.cost is not None:
            self.cost = self.clicks * 0.5

        if self.clicks:
            self.cpc = self.cost / self.clicks
        else:
            self.cpc = None

        if self.views:
            self.cpm = (self.cost / self.views) * 1000
        else:
            self.cpm = None

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.date)


