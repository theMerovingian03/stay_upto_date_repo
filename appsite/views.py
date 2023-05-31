from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from .models import FileProperties



def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def whyto(request):
    return render(request, 'whyto.html')

def team(request, member_id):
    members = {
        'rishi':{'first_name':'Rushikesh','last_name':'Borade' ,'contact':'12345', 'position':'Team Lead','email_member':'abc@gmail.com', 'image':'images/rishi.png', 'linkedin':'https://www.linkedin.com/in/rushikesh-borade-94b092234'},
        'roshan':{'first_name':'Roshan','last_name':'Tanpure' ,'contact':'12345', 'position':'Front-end Developer','email_member':'abc@gmail.com', 'image':'images/roshan.png', 'linkedin':'https://www.linkedin.com/in/'},
        'avinash':{'first_name':'Avinash','last_name':'Dadge' ,'contact':'12345', 'position':'Web Design','email_member':'abc@gmail.com', 'image':'images/avinash-modified.png', 'linkedin':'https://www.linkedin.com/in/avinash-dadge-9b0b19251'},
        'mahesh':{'first_name':'Mahesh','last_name':'Swami' ,'contact':'12345', 'position':'Database Management','email_member':'abc@gmail.com', 'image':'images/mahesh.png', 'linkedin':'https://www.linkedin.com/in/mahesh-swami-3b4950268'},
    }
    member = members.get(member_id)
    return render(request, 'team.html', {'member':member})



def email_status(request):
    return render(request, 'email_status.html')

def contact(request):
    if request.method == 'POST':
        # retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        
        try:
            # send email
            send_mail(
                subject=f'New submission regarding: {subject}',
                message=f'Name: {name}\nEmail: {email}\nMessage: {message}',
                from_email='stayuptodate23@outlook.com',
                recipient_list=['stayuptodate23@outlook.com'],
                fail_silently=False,
            )
        except BadHeaderError:
            # return error message
            return HttpResponse('Invalid header found.')
        except Exception as e:
            # return error message with exception details
            print(f'An error occurred while sending the email: {str(e)}')
            return HttpResponse('Error occured.')

        
        # return success message
        return render(request,'email_status.html')
    
    # if GET request, render contact form
    return render(request, 'contact.html')

def pricing(request):
    return render(request, 'pricing.html')

def industry(request, choice):
    queryset = FileProperties.objects.filter(industry_tag=choice)
    if not queryset:
        # Handle the case when there are no items in the queryset
        # You can return an empty context or an appropriate response
        context = {'objects': [], 'industry_tag': None}
    else:
        objects = queryset
        industry_tag = queryset[0].industry_tag
        context = {'objects': objects, 'industry_tag': industry_tag}
    
    return render(request, 'industry.html', context)



def all_industries(request):
    choices = FileProperties.industry_choices
    return render(request, 'all_industries.html', {'choices': choices})

def email_error(request):
    return render(request, 'email_error.html')

def index(request):
    if request.method == 'POST':
        return render(request, 'email_error.html')
    return render(request, 'index.html')