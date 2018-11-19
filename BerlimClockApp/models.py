from django.db import models

# Create your models here.

class GPIOPin(models.Model):
    modes = (("I", "IN"), ("O","OUT"), ("O", "None"))
    number = models.IntegerField()
    state = models.BooleanField()
    mode = models.CharField(choices=modes, max_length=5)

    def __str__(self):
        return f"GPIOPin nº{self.number} is {'on' if self.state else 'off'} on mode {self.mode}"
