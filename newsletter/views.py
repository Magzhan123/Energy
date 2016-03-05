from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm, SignUpForm
# Create your views here.

def home(request):
	title = 'Welcome'
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form":form
	}
	if form.is_valid():
		instance = form.save(commit=False)
		if instance.full_name == None:
			instance.full_name = "Magzhan"
		instance.save()
	context = {
		"title": title,
		"form":form
	}

	return render(request, "home.html", context)


def contact(request):
	form =  ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print email, message, full_name
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'youotheremail@email.com']
		contact_message = "%s: %s via %s"%(
			form_full_name, 
			form_message,
			form_email)
		some_html_message = """
		<h1>Hello</h1>
		"""
		send_mail(subject, 
			contact_message, 
			from_email,
			[to_email],
			html_message = some_html_message,
			fail_silently=True)
	context = {
		"form": form,
	}
	return render(request, "forms.html", context)
