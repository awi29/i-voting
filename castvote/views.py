import re
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from accounts.models import Student
from accounts.models import Candidate
from django.contrib import messages


encryptedkey = ['104','421','251','340','874','982','124','719','364','284','412']


# @login_required
# def voting(request):
# 	if request.user.is_authenticated():
# 		username = request.user.username
# 		student = Student.objects.get(username=username)
# 		year = student.year
# 		students = Student.objecs.filter(iscandidate=True, year=year).order_by('firstname')
# 	# POSTS = ['general','cultural','technical','sports','environmental','mess','maintenance']
# 		posts = ['General Secretary','Cultural Secretary'
# 				  'Technical Secretary', 'Sports Secretary'
# 				  'Environmental Secretary', 'Mess Secretary',
# 				   'Maintenance Secretary', 'Literary Secretary'
# 			]

# 		context = {
# 			'general_sec' : [],
# 			'cultural_sec': [],
# 			'technical_sec': [],
# 			'sports_sec' : [],
# 			'environmental_sec' : [],
# 			'mess_sec' : [],
# 			'maintenance_sec' : [],
# 			'unchosen' : []
# 		}

# 		for student in students:
# 			candidate = Candidate.objects.get(student=student)
# 			post = candidate.postname
# 			i = 0
# 			while i < 8:
# 				if post == posts[i]:
# 					break

# 			if i==0 :
# 				context['general_sec'].append(candidate)
# 			elif i==1 :
# 				context['cultural_sec'].append(candidate)
# 			elif i==2 :
# 				context['technical_sec'].append(candidate)
# 			elif i==3 :
# 				context['sports_sec'].append(candidate)
# 			elif i==4 :
# 				context['environmental_sec'].append(candidate)
# 			elif i==5 :
# 				context['mess_sec'].append(candidate)
# 			elif i==6 :
# 				context['maintenance_sec'].append(candidate)
# 			else :
# 				context['unchosen'].append(candidate)


# 		return render(request,'castvote/votingform.html',context)



@login_required
def voting(request):
	context = {}
	if request.user.is_authenticated():
		username = request.user.username
		student = Student.objects.get(username=username)
		year = student.year
		
		context['encryptedkey'] = encryptedkey
		context['general_sec'] = Candidate.objects.filter(student__year=year,student__iscandidate=True,postname='General Secretary').order_by('student__username')
		context['cultural_sec'] = Candidate.objects.filter(student__year=year,student__iscandidate=True,postname='Cultural Secretary').order_by('student__username')
		context['technical_sec'] = Candidate.objects.filter(student__year=year,student__iscandidate=True,postname='Technical Secretary').order_by('student__username')
		context['sports_sec'] = Candidate.objects.filter(student__year=year,student__iscandidate=True,postname='Sports Secretary').order_by('student__username')
		context['environmental_sec'] = Candidate.objects.filter(student__year=year,student__iscandidate=True, postname='Environmental Secretary').order_by('student__username')
		context['mess_sec'] = Candidate.objects.filter(student__year=year,student__iscandidate=True,postname='Mess Secretary').order_by('student__username')
		context['maintenance_sec'] = Candidate.objects.filter(student__year=year,student__iscandidate=True,postname='Maintenance Secretary').order_by('student__username')
		context['literary_sec'] = Candidate.objects.filter(student__year=year,student__iscandidate=True,postname='Literary Secretary').order_by('student__username')	


		# for index,candidate in enumerate(context['general_sec']):
		# 	candidate1 = [encryptedkey[index],candidate]


		# for candidate in context['general_sec']:
		# 	print candidate[0],candidate[1]

		return render(request,'castvote/castvote.html',context)




def storevote(request):
	errors = []
	context = {}
	if request.user.is_authenticated():
		username = request.user.username
		try:
			student = Student.objects.get(username=username)
		except Student.DoesNotExist:
			return HttpResponse("<h3>No student with username - " ,username, "exists in database</h3>")

		if request.method == "POST":
			try:
				general 	= request.POST.get('general','')
				cultural 	= request.POST.get('cultural','')
				technical 	= request.POST.get('technical','')
				sports 		= request.POST.get('sports','')
				environmental = request.POST.get('environmental','')
				mess 		= request.POST.get('mess','')
				maintenance = request.POST.get('maintenance','')
				literary 	= request.POST.get('literary','')

				# print "\n\n"
				# print "general  = ", general
				# print "cultural = ", cultural
				# print "technical = ", technical
				# print "sports = ",sports
				# print "environmental = ", environmental
				# print "mess  = ",mess
				# print "maintenance  = ", maintenance
				# print "literary  = ",literary
				# print "\n\n"

				if is_number(general):
					if general not in encryptedkey:
						context['error_general'] = '*Dont Change value in the form'
				else:
					context['error_general'] = '*Please Select Candidate for general secretary'

				if is_number(cultural):
					if cultural not in encryptedkey:
						context['error_cultural'] = '*Dont Change value in the form'
				else:
					context['error_cultural'] = '*Please Select Candidate for cultural secretary'


				if is_number(technical):
					if technical not in encryptedkey:
						context['error_technical'] = '*Dont Change value in the form'
				else:
					context['error_technical'] = '*Please Select Candidate for technical secretary'

				if is_number(sports):
					if sports not in encryptedkey:
						context['error_sports'] = '*Dont Change value in the form'
				else:
					context['error_sports'] = '*Please Select Candidate for sports secretary'


				if is_number(environmental):
					if environmental not in encryptedkey:
						context['error_environmental'] = '*Dont Change value in the form'
				else:
					context['error_environmental'] = '*Please Select Candidate for environmental secretary'


				if is_number(mess):
					if mess not in encryptedkey:
						context['error_mess'] = '*Dont Change value in the form'
				else:
					context['error_mess'] = '*Please Select Candidate for mess secretary'

				
				if is_number(maintenance):
					if maintenance not in encryptedkey:
						context['error_maintenance'] = '*Dont Change value in the form'
				else:
					context['error_maintenance'] = '*Please Select Candidate for maintenance secretary'


				if is_number(literary):
					if literary not in encryptedkey:
						context['error_literary'] = '*Dont Change value in the form'
				else:
					context['error_literary'] = '*Please Select Candidate for literary secretary'


				return HttpResponse("Vote Received")
			except ValueError:
				return HttpResponse("<h3>Please Select candidate for every post</h3>") 

		else :
			return HttpResponse("<h3> Method of submission should be <strong>POST</strong></h3>")

	else :
		return HttpResponse("<h3>You are not authenticated to vote</h3>")




def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False




def printga():
	print "\n\n"
	print "general  = ", general
	print "cultural = ", cultural
	print "technical = ", technical
	print "sports = ",sports
	print "environmental = ", environmental
	print "mess  = ",mess
	print "maintenance  = ", maintenance
	print "literary  = ",literary
	print "\n\n"

	# general 	= int(request.POST.get('general',''))
	# cultural 	= int(request.POST.get('cultural',''))
	# technical 	= int(request.POST.get('technical',''))
	# sports 		= int(request.POST.get('sports',''))
	# environmental = int(request.POST.get('environmental',''))
	# mess 		= int(request.POST.get('mess',''))
	# maintenance = int(request.POST.get('maintenance',''))
	# literary 	= int(request.POST.get('literary',''))

