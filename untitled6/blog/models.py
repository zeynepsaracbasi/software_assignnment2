
from django.db import models

#Blog = [['apple','iphone7 is very expensive'],['school','students are getting bored'],['healty life','doing sport is good for human health']]

class Blog(models.Model):

    name = models.CharField(max_length=220)
    description = models.CharField(max_length=520)