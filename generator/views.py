from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
	##return HttpResponse("This is home page")
	return render (request, 'generator/home.html',{'password':'fsdfs2fs5f456'})

def about(request):
	return render(request, 'generator/about.html')

def password(request):

	
	characters = list('abcdefghijklmnopqrstuvwxyz')
	#characters = list(string.ascii_lowercase)
	#characters = list(string.ascii_uppercase)
	#characters = list(string.punctuation)
	#characters.extend(list(string.digits))

	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	if request.GET.get('numbers'):
		characters.extend(list('0123456789'))		
	if request.GET.get('special'):
		characters.extend(list('!@#$%^&*()'))
	thepassword = ''
	length = int(request.GET.get('length',10))

	#thepassword = ("".join(random.suffle(characters)[0:length]))

	for x in range(length):
		thepassword += random.choice(characters)

	return render (request, 'generator/password.html', {'password':thepassword})