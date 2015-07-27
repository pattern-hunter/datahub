from django.db import models

# Create your models here.

class Dummy(models.Model):
	class Meta:
		permissions = (
			("can_view","can view api"),
			("can_edit","can edit api"),
				)
