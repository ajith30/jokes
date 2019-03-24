from django.shortcuts import render, redirect #For CBV
from .forms import NewForm
from .models import Contact
import json
import requests
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy #FOR CBV

# Create your views here.
    
def home(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname') #Add attribute name='fname' at input tag in index.html 
        lastname = request.POST.get('lname') #Add attribute name='lname' at input tag in index.html 

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname) #It will retun jason file formatted data
        json_data = json.loads(r.text) # it will give jason data into dictionary formatted data
        joke = json_data.get('value').get('joke') # This is the way to access the joke value from the dictionary

        context = {'joke':joke}
        return render(request, 'mysite/index.html', context)
    
    else: #This else part give the defalt jokes if we didn't enter first and lat name at home page.
        firstname = 'Jason'
        lastname = 'Santhom'

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname) #It will retun jason file formatted data
        json_data = json.loads(r.text) # it will give jason data into dictionary formatted data
        joke = json_data.get('value').get('joke') # This is the way to access the joke value from the dictionary

        context = {'joke':joke}
        return render(request, 'mysite/index.html', context)
def thank_you(request):
    return render(request, 'mysite/thank_you.html')

def portfolio(request):
    return render(request, 'mysite/portfolio.html')

"""
class Contact(CreateView):  #This is CBV - contact Form
    model = Contact
    temlate_name = 'mysite/contact_form.html'
    form_class = NewForm
    success_url = reverse_lazy('home')    
"""

def contact(request):         #This is FBV - Contact Form
    if request.method == 'GET':
        form = NewForm()
    else:                          
        form = NewForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('thank_you')
    return render(request, "mysite/contact_form.html", {'form': form})


"""
# If we don't use any django forms option and if we make forms by only using HTML 
# Then create your required fields in HTML
# Note When you using this type then you should have mention action={% url 'contact'%} at form tag
def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email=email_r,subject=subject_r,message=message_r)
        c.save()

        return render(request,"mysite/contact_form.html",)
    else:
        return render(request,"mysite/contact_form.html", )
"""
