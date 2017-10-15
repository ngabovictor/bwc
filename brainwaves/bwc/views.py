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
	data['works'] = work.objects.all() .order_by('-date')

	return render(request, 'index.html', data)



def whatwedo(request):
	data = {}
	data['works'] = work.objects.all()
	data['work_categories'] = work_category.objects.all()
	return render(request, 'what-we-do.html', data)



def ourprograms(request):
	data = {}
	data['programs'] = program.objects.all()
	data['program'] = program.objects.all().first()
	return render(request, 'our-programs.html', data)

def ourprogram(request, program_id):
	data = {}
	data['programs'] = program.objects.all()
	data['program'] = program.objects.get(pk=program_id)
	return render(request, 'our-programs.html', data)



def contact(request):
	data = {}
	return render(request, 'contact.html', data)



def joinprogram(request, program_id):
	data = {}
	data['programs'] = program.objects.all()
	data['choosen'] = program.objects.get(id=program_id)
	return render(request, 'join-us.html', data)


def joinprogram_in(request):

	if request.method=='POST':
		names = request.POST['names']
		phone = request.POST['phone']
		email = request.POST['email']
		address = request.POST['address']
		description = request.POST['description']
		program_ref = request.POST['program']

		program_id = program.objects.get(id = program_ref)

		joined.objects.create(
			names = names,
			phone = phone,
			email = email,
			address = address,
			description = description,
			program = program_id,
			date = datetime.today(),)
	return redirect('/')



def register(request, training_id):
	data = {}
	data['trainings'] = training.objects.all()
	data['choosen'] = training.objects.get(id=training_id)
	data['paymentMethods'] = paymentMethod.objects.all()
	return render(request, 'register.html', data)



def publications(request):
	data = {}
	data['publications'] = publication.objects.all()
	return render(request, 'publications.html', data)



def trainings(request):
	data = {}
	data['trainings'] = training.objects.all()
	data['training'] = training.objects.all().first()
	return render(request, 'trainings.html', data)



def ourtraining(request, training_id):
	data = {}
	data['trainings'] = training.objects.all()
	data['training'] = training.objects.get(pk=training_id)
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
		names = request.POST['names']
		email = request.POST['email']
		phone = request.POST.get('phone')
		paid = request.POST['paid']
		settraining = request.POST['training']
		address = request.POST['address']
		description = request.POST['description']
		duration = request.POST['duration']
		payment = request.POST['payment']

		registered.objects.create(
			names = names,
			email = email,
			phone = phone,
			address = address,
			training = training.objects.get(id=settraining),
			description = description,
			duration =duration,
			date = datetime.today(),
			paid = paid,
			payment = paymentMethod.objects.get(id=payment,)
			)
	
		#send_mail(
			#'Message from web by %s'%email,
			#message,
			#'coredev2017@gmail.com',
			#['contact@corelabsplus.com'],
			#fail_silently=False,
		#)
	return redirect('/')

