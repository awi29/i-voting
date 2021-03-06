from __future__ import unicode_literals

from django.db import models

# Create your models here.
from accounts.models import Student
from accounts.models import Candidate


class StoreVote(models.Model):
	specialkey 		= models.CharField(blank=False,max_length=16)
	general 		= models.IntegerField(blank=False)
	cultural 		= models.IntegerField(blank=False)
	technical 		= models.IntegerField(blank=False)
	sports 			= models.IntegerField(blank=False)
	environmental 	= models.IntegerField(blank=False)
	mess 			= models.IntegerField(blank=False)
	maintenance		= models.IntegerField(blank=False)
	literary		= models.IntegerField(blank=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return specialkey

	def __unicode__(self):
		return specialkey

	class Meta:
		ordering = ['-timestamp']



class CandidateVotes(models.Model):
	candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE)
	votes = models.IntegerField(blank=False,default=0)

	def __str__(self):
		return self.candidate.student.username

	def __unicode(self):
		return self.candidate.student.username

	class Meta:
		ordering = ['candidate']
