from django.db import models
from django.db.models import Model

# Create your models here.
class AdminDetails(models.Model):
	username = models.CharField(max_length=100,default=None,null=True)
	password = models.CharField(max_length=100,default=None,null=True)
	class Meta:
		db_table = 'AdminDetails'

class voter_register(models.Model):
	voter_name = models.CharField(max_length=100,default=None,null=True)
	Age = models.CharField(max_length=100,default=None,null=True)
	Gender = models.CharField(max_length=100,default=None,null=True)
	Address = models.CharField(max_length=100,default=None,null=True)
	username = models.CharField(max_length=100,default=None,null=True)
	password = models.CharField(max_length=100,default=None,null=True)
	confirm_password = models.CharField(max_length=100,default=None,null=True)
	class Meta:
		db_table = 'voter_register'

class master_table(models.Model):
	aadhar_card_no = models.CharField(max_length=100,default=None,null=True)
	class Meta:
		db_table = 'master_table'

class election_detail(models.Model):
	election_name = models.CharField(max_length=100,default=None,null=True)
	election_category = models.CharField(max_length=100,default=None,null=True)
	start_date = models.CharField(max_length=100,default=None,null=True)
	end_date = models.CharField(max_length=100,default=None,null=True)
	election_commission = models.CharField(max_length=100,default=None,null=True)
	state = models.CharField(max_length=100,default=None,null=True)
	class Meta:
		db_table = 'election_detail'


class candidate_detail(models.Model):
	candidate_name = models.CharField(max_length=100,default=None,null=True)
	election_name = models.CharField(max_length=100,default=None,null=True)
	age = models.CharField(max_length=100,default=None,null=True)
	gender = models.CharField(max_length=100,default=None,null=True)
	political_party = models.CharField(max_length=100,default=None,null=True)
	caste = models.CharField(max_length=100,default=None,null=True)
	Address = models.CharField(max_length=100,default=None,null=True)
	election_name =	models.CharField(max_length=100,default=None,null=True)
	Vote =	models.CharField(max_length=100,default=None,null=True)
	class Meta:
		db_table = 'candidate_detail'

class vote(models.Model):
	voter_id = models.CharField(max_length=100,default=None,null=True)
	election_id = models.CharField(max_length=100,default=None,null=True)
	candidate_id = models.CharField(max_length=100,default=None,null=True)
	candidate_name = models.CharField(max_length=100,default=None,null=True)
	political_party = models.CharField(max_length=100,default=None,null=True)
	election_name = models.CharField(max_length=100,default=None,null=True)
	Date = models.CharField(max_length=100,default=None,null=True)
	class Meta:
		db_table = 'add_vote'











	

