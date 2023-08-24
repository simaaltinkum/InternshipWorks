from django.shortcuts import render
from django.core.mail import send_mail
from faker import Faker
from .models import Email


def send_email(request):
    if request.method == 'POST':
        # subject = 'Test Email'
        # message = 'This is a test email sent from Django.'
        from_email = 'simaaltinkum02@gmail.com'
        recipient_email = request.POST['email']
        recipient_title = request.POST['title']
        recipient_message = request.POST['message']

        send_mail(recipient_title, recipient_message, from_email, [recipient_email])

        # Email.objects.create(email=recipient_email)
        query = Email.objects.all().order_by('id')
        query.save()

        return render(request, 'success.html')

    return render(request, 'send_email.html')


def send_gonderilenler(request):

    liste = Email.objects.all()
    context = {
        "liste" : liste
    }
    return render(request, 'send_gonderilenler.html', context)

def send_message(request, pk):

    obj = Email.objects.get(pk = pk)
    context = {
        "obj" : obj
    }
    return render(request, 'send_message.html', context)

def record_email(request, num_emails=10):
    fake = Faker()

    for _ in range(num_emails):

        email = fake.email()

        email = Email.objects.create(email=email)

        email.title = "Title's pk", str(email.pk)
        email.message = "Email's pk", str(email.pk)
        email.save()

    return render(request,'record_email.html')

def show_email(request):
    email = Email.objects.all().order_by('-id')[:10]

    context = {
        'email': email
    }
    return render(request, 'show_email.html', context)
