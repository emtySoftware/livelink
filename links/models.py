from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	links = models.ManyToManyField('links.Link', related_name='ulinks')

# Create your models here.
class Link(models.Model):
	user = models.ForeignKey('links.User')
	url = models.URLField()

	def __unicode__(self):
		return "%s - %s" % (self.user.first_name, self.url)