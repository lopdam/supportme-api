from django.db import models

from django.contrib.auth.models import User
from apps.hueca.models import Hueca
from django.core.validators import MinValueValidator, MaxValueValidator

#Like, Rating, Comment

class Like(models.Model):
    hueca = models.ForeignKey(Hueca, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('hueca', 'user',)

    def __str__(self):
        return str(self.user)+" : "+str(self.hueca)


class Rating(models.Model):
    score=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    hueca = models.ForeignKey(Hueca, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('hueca', 'user',)

    def __str__(self):
        return str(self.user)+" : "+str(self.hueca)+" : "+str(self.score)


class Comment(models.Model):
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    hueca = models.ForeignKey(Hueca, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)+":"+str(self.hueca)
