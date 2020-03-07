from django.db import models
from django.contrib.auth.models import User
# Create your models here.


MODEL_CHOICES = [
    ("1", ("CNN")),
]


class MlModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    model_type = models.CharField(choices=MODEL_CHOICES,default="CNN",max_length=100)
    zipfile = models.FileField()

    def __str__(self):
        return self.user.username + " - " + self.model_name

class TrainedModel(models.Model):
    modelfrom = models.ForeignKey(MlModel,on_delete=models.CASCADE)
    trained_model = models.FileField()

    def __str__(self):
        return self.user.username + " - " + self.model_name
 

