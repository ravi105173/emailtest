from django.shortcuts import render
from emailtest.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def student(request):
    subject = 'django email test'
    message = 'hello! this is test mail from django project emailtest'
    recepient = 'ravi105173@gmail.com'
    send_mail(subject , message , EMAIL_HOST_USER , [recepient] , fail_silently=False)
    return render(request, '<h4>mail test</h4>')

