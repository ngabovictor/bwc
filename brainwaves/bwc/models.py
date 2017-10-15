from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

# Carousel

class carousel(models.Model):
	image = models.FileField(help_text="Add images with same resolutions", upload_to='media/home/carousel')
	title = models.CharField(help_text="Add an image title", max_length=50)
	caption = models.TextField(help_text="Add an image more description",)

	def __str__(self):
		return self.title


class publication(models.Model):
	image = models.FileField(help_text="Add a thumbnail of the publication", upload_to='media/home/publications')
	title = models.CharField(help_text="Add the title", max_length=50)
	caption = models.TextField(help_text="Add the description",)
	author = models.CharField(help_text="Add the author's name", max_length=50)

	def __str__(self):
		return self.title


class work_category(models.Model):
	title = models.CharField(help_text="Add the title", max_length=50)
	description = models.TextField(help_text="Add the description")

	def __str__(self):
		return self.title



class work(models.Model):
	title = models.CharField(help_text="Add the title", max_length=50)
	image = models.FileField(help_text="Add a thumbnail of the work", upload_to='media/home/activities')
	icon = models.CharField(help_text="Add the icon, please make sure you write correctly, otherwise the icon will be missing. visit http://fontawesome.io for accurate names.", max_length=50)
	caption = models.TextField(help_text="Add a short caption")
	category = models.ForeignKey(work_category, help_text="Choose category for the work.", on_delete=models.CASCADE)
	date = models.DateField(default=datetime.today())
	description = models.TextField(help_text="Add a full description.")

	def __str__(self):
		return self.title



class training(models.Model):
	title = models.CharField(help_text="Add the title", max_length=50)
	image = models.FileField(help_text="Add a thumbnail of the work", upload_to='media/home/trainings')
	# icon = models.CharField(help_text="Add the icon, please make sure you write correctly, otherwise the icon will be missing. visit http://fontawesome.io for accurate names.", max_length=50)
	caption = models.TextField(help_text="Add a short caption")
	# category = models.ForeignKey(work_category, help_text="Choose category for the work.", on_delete=models.CASCADE)
	# date = models.DateField(default=datetime.today())
	description = models.TextField(help_text="Add a full description.")
	price = models.CharField(help_text="Add the training's price in USD.", max_length=50)


	def __str__(self):
		return self.title


class program(models.Model):
	title = models.CharField(help_text="Add the title", max_length=50)
	image = models.FileField(help_text="Add a thumbnail of the work", upload_to='media/home/programs')
	# icon = models.CharField(help_text="Add the icon, please make sure you write correctly, otherwise the icon will be missing. visit http://fontawesome.io for accurate names.", max_length=50)
	caption = models.TextField(help_text="Add a short caption")
	# category = models.ForeignKey(work_category, help_text="Choose category for the work.", on_delete=models.CASCADE)
	# date = models.DateField(default=datetime.today())
	description = models.TextField(help_text="Add a full description.")


	def __str__(self):
		return self.title




class paymentMethod(models.Model):
	title = models.CharField(help_text="Add name", max_length=50)
	description = models.TextField(help_text="Add a full description.")
	Yes = 'Yes'
	No = 'No'
	status = {
	(Yes, 'Yes'),
	(No, 'No'),
	}
	Active = models.CharField(help_text="Set status.", choices=status, default="Yes", max_length=10)

	def __str__(self):
		return str(self.title)



class registered(models.Model):
	names = models.CharField(help_text="Add names", max_length=50)
	email = models.EmailField(help_text="Add email address", default=' ')
	phone = models.CharField(help_text='Add phone number', default=' ', max_length=12)
	address = models.CharField(help_text='Add phone number', default=' ', max_length=50)
	description = models.TextField(help_text="Add a full description.")
	date = models.DateField(default=datetime.today())
	paid = models.CharField(help_text="Add the amount paid in USD.", max_length=50)
	training = models.ForeignKey(training, help_text="training registered.", on_delete=models.CASCADE)
	duration = models.CharField(help_text="Duration in months", max_length=2)
	payment = models.ForeignKey(paymentMethod, help_text="Add payment method", on_delete=models.CASCADE)


	def __str__(self):
		return str(self.names)+ ", " + str(self.email) + ", " + str(self.phone) + ", " + str(self.training)


class joined(models.Model):
	names = models.CharField(help_text="Add names", max_length=50)
	email = models.EmailField(help_text="Add email address", default=' ')
	phone = models.CharField(help_text='Add phone number', default=' ', max_length=12)
	address = models.CharField(help_text='Add phone number', default=' ', max_length=50)
	description = models.TextField(help_text="Add a full description.")
	date = models.DateField(default=datetime.today())
	program = models.ForeignKey(program, help_text="training registered.", on_delete=models.CASCADE)


	def __str__(self):
		return str(self.names) + ", " + str(self.email) + ", " + str(self.phone)+ ", " + str(self.program)





class mailbox(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	message = models.TextField()
	date = models.DateField(default=datetime.today())
	Read = 'Read'
	Unread = 'Unread'
	classification_choices = {
	(Read, 'Read'),
	(Unread, 'Unread'),
	}
	classifications = models.CharField(max_length=200, choices=classification_choices, default="Unread")

	def __str__(self):
	    return self.name
