from django.shortcuts import render, redirect
from bwc.models import *
from datetime import datetime
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect

# carousel
# publication
# work
# work_category
# training
# program
# registered
# mailbox

# Create your views here.
def index(request):
	data = {}

	data['carousel'] = carousel.objects.all()
	data['works'] = work.objects.all() #.order_by(-date)

	return render(request, 'index.html', data)



def whatwedo(request):
	data = {}
	data['works'] = work.objects.all()
	data['work_categories'] = work_category.objects.all()
	return render(request, 'what-we-do.html', data)



def ourprograms(request):
	data = {}
	data['programs'] = program.objects.all()
	return render(request, 'our-programs.html', data)



def contact(request):
	data = {}
	return render(request, 'contact.html', data)



def joinprogram(request):
	data = {}
	return render(request, 'join-us.html', data)



def register(request):
	data = {}
	return render(request, 'register.html', data)



def publications(request):
	data = {}
	data['publications'] = publication.objects.all()
	return render(request, 'publications.html', data)



def trainings(request):
	data = {}
	data['trainings'] = training.objects.all()
	return render(request, 'trainings.html', data)



def allprograms(request):
	data = {}
	data['programs'] = program.objects.all()
	return render(request, 'all-programs.html', data)



def alltrainings(request):
	data = {}
	data['trainings'] = training.objects.all()
	return render(request, 'all-trainings.html', data)


def sendmessage(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST.get('message')
		classifications = 'Unread'
		date = datetime.today()

		mailbox.objects.create(
			name = name,
			email = email,
			message = message,
			classifications = classifications,
			date = date,
			)
	
		#send_mail(
			#'Message from web by %s'%email,
			#message,
			#'coredev2017@gmail.com',
			#['contact@corelabsplus.com'],
			#fail_silently=False,
		#)
	return redirect('/')



def registering(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST.get('phone')
		paid = request.POST['paid']
		settraining = request.POST['training']
		address = request.POST['address']
		description = request.POST['description']

		traininginfo = training.objects.get(title = settraining)
		duration = float(traininginfo.price) / float(paid)

		registered.objects.create(
			name = name,
			email = email,
			phone = phone,
			address = address,
			training = settraining,
			description = description,
			duration =duration,
			date = datetime.today(),
			paid = paid,
			)
	
		#send_mail(
			#'Message from web by %s'%email,
			#message,
			#'coredev2017@gmail.com',
			#['contact@corelabsplus.com'],
			#fail_silently=False,
		#)
	return redirect('/')

