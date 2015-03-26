from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	links = models.ManyToManyField('links.Link', related_name='ulinks')


	def __unicode__(self):
		return self.get_full_name()

# Create your models here.
class Link(models.Model):
	user = models.ForeignKey('links.User')
	url = models.URLField()

	def __unicode__(self):
		return "%s - %s" % (self.user.first_name, self.url)