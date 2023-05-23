from django.db import models

# Create your models here.
class Record(models.Model):
    album = models.CharField(max_length=125)
    artist= models.CharField(max_length=125)
    artwork = models.URLField(null=True, blank=True, max_length=300)
    date = models.DateField(auto_now_add=False, blank=True)
    price= models.DecimalField(max_digits=10, decimal_places=2, null=True)


    def __str__(self):
        return self.artist + " / " + self.album

    # def __str__(self):
    #     return str(self.album) + ": $" + str(self.price)
