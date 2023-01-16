from django.shortcuts import render,HttpResponse,redirect
from django.core.mail import EmailMessage, get_connection,send_mail

from django.conf import settings

from .models import *
# Create your views here.
def home(request):
    if request.method == "POST":
        if request.POST.get('med'):
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            college = request.POST.get('college', '')
            med = request.POST.get('med', '')
            formData=MedicalStudents(name=name,email=email,college=college,med=med)
            formData.save()
        else:
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            college = request.POST.get('college', '')
            eng = request.POST.get('eng', '')
            formData=EngineerStudents(name=name,email=email,college=college,eng=eng)
            formData.save()
    return render(request,'home.html')

def showData(request):
    print('showData',id)
    med=MedicalStudents.objects.all()
    eng=EngineerStudents.objects.all()
    return render(request,'view.html',{'med':med,'eng':eng})

def sendMessageall(request):
    print('send message to all')
    # print('id',id)
    if request.method == 'POST':
        print(request.POST)
        subject=request.POST['subject']
        print(subject)
        message=request.POST['message']
        print(message)

        getdata = request.POST['selected-mails']
        print(getdata)
        email_list=getdata.split(',')
        # request_getdata=request.body.decode('utf-8')
        email_from=settings.EMAIL_HOST_USER

        print(email_list)
        send_mail(subject,message,email_from,email_list)
        print(send_mail)
    return redirect('showdata')

        # return HttpResponse(request_getdata)  


    return HttpResponse('send message')

# def deletemessage(request,id):
#     print('dltmsg',id)
#     med=MedicalStudents.objects.get(id=id)
#     med.delete()
#     print('med',med)
#     # eng=EngineerStudents.objects.all()
#     # print(eng)
#     return redirect('showdata')
# def sendMessage(request,id):
#     print('send message function start')
#     med=MedicalStudents.objects.get(id=id)
#     subject="Email integration Task Send Mail From backend"
#     message="This popular Python web framework allows you to accelerate email delivery and make it much easier. And these code samples of sending emails with Django are going to prove that.  "
#     email_form=settings.EMAIL_HOST_USER
#     print(email_form)
#     recipient_list=['s.nargis1998@gmail.com']
#     print(recipient_list)
#     send_mail(subject,message,email_form,recipient_list)
#     print(send_mail)
#     return redirect('showdata')
    

# def sendMessage(request,id):
#     print('send message function start')
#     s=MedicalStudents.objects.get(id=id)
#     print(s)
#     subject=" "
#     message="email integration task assigned by junaid sir "
#     email_form=settings.EMAIL_HOST_USER
#     print(email_form)
#     recipient_list=['mumaicoding@gmail.com','skadnan7869@gmail.com','storingfiles1024@gmail.com','jc.juned.chaudhary@gmail.com','juned.6119006.it@mhssce.ac.in','suhail.7119012.co@mhssce.ac.in','junedchaudhary36gmail.com','pasif387@gmail.com','zikrakhan1032@gmail.com','er.kmk@123gmail.com','sahifashaikh929@gmail.com','jc.junaid.chaudhary@gmail.com','shaikhsaud8286@gmail.com','khanmisbahk@gmail.com','khansarfraz5346@gmail.com']
#     # recipient_list=['shaikhminhaj907@gmail.coms']
#     send_mail(subject,message,email_form,recipient_list)
#     print(send_mail)
#     return redirect('showdata')
   

def sendMessage(request,id):
    print('send message',id)
    med=MedicalStudents.objects.get(id=id)
    print('med',med)
    emailfrom=settings.EMAIL_HOST_USER
    print(settings.EMAIL_HOST_USER,'password',settings.EMAIL_HOST_PASSWORD)  
    if request.method == "POST":
        print(request.POST)
        emailfrom=settings.EMAIL_HOST_USER
        print(emailfrom)
        recipient_list=[med.email]
        # recipient_list = request.POST.getlist("email")
        print(type(recipient_list),recipient_list)
        subject = request.POST.get("subject")  
        message=request.POST.get("message")
        print(type(message),message)
        send_mail(subject,message,emailfrom,recipient_list)
    return redirect('showdata')
#     # if request.method == "POST":
#     #     with get_connection(  
#     #           host=settings.EMAIL_HOST,
#     #     port=settings.EMAIL_PORT,  
#     #    username=settings.EMAIL_HOST_USER,  
#     #    password=settings.EMAIL_HOST_PASSWORD,  
#     #     use_tls=settings.EMAIL_USE_TLS
#     #     ) as connection:  
#     #         # recipient_list = [request.POST.get("email"),]
#     #         recipient_list = [med.email]
#     #         print(type(recipient_list),recipient_list)
#     #         # subject = request.POST.get("subject")  
#     #         email_from = settings.EMAIL_HOST_USER 
#     #         print(email_from) 
#     #         message = request.POST.get("message")
#     #         print(message)  
#     #         EmailMessage(message, email_from, recipient_list, connection=connection).send()  
#             # send_mail(message, email_from, recipient_list, connection=connection)  
#     return redirect('showdata')
    #    with get_connection(host=settings.EMAIL_HOST,port=settings.EMAIL_PORT, username=settings.EMAIL_HOST_USER,password=settings.EMAIL_HOST_PASSWORD,use_tls=settings.EMAIL_USE_TLS) as connection:
    #     # connection = get_connection(host=settings.EMAIL_HOST,port=settings.EMAIL_PORT, username=settings.EMAIL_HOST_USER,password=settings.EMAIL_HOST_PASSWORD,use_tls=settings.EMAIL_USE_TLS,fail_silently=False) 
    #     # print(connection)
    #        email_from = settings.EMAIL_HOST_USER  
    #        recipient_list = [request.POST.get("email")]
    #     #    recipient_list = ['shaikhminhaj907@gmail.com' ]
    #        print(recipient_list)  
    #     #    message="qwerty098765432"
    #        message=request.POST.get("message")
    #        print(message) 
    #        send_mail( message, email_from, recipient_list)
             
        #    return redirect('showdata')
