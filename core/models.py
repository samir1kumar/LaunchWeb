from django.db import models

# Create your models here.
class Join(models.Model):
	email = models.EmailField()
	ref_id = models.CharField(max_length = 120, unique = True, default='ABC')
	ip_address = models.CharField(max_length=50, default='ABC')
	timestamp = models.DateTimeField(auto_now = False, auto_now_add= True)
	updated = models.DateTimeField(auto_now = True, auto_now_add = False)

	def __unicode__(self):
		return "%s"%(self.email)

	class Meta:
		unique_together = ('email', 'ref_id')