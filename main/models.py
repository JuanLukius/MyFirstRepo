from django.db import models

class MagicItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    type = models.TextField()

    @property
    def is_not_a_waste_of_money(self):
        return self.price == 0