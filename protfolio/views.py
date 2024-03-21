from django.conf import settings
from django.shortcuts import render,HttpResponse
from django.contrib import messages

from django.views import View 
from django.core.mail import send_mail
from .models import Project,Posts

class index(View):
    def get(self, request):
        projects = Project.objects.all()
        post=Posts.objects.all()
        
        context={
            'projects': projects,
            "post":post,
        }
        return render(request, "index.html", context)


def send_mail_view(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        # Your email configuration
        sender_email = 'royal.chaulagain321@gmail.com'

        try:
    # Compose the email message
            html_message = f"""
            <p>Dear {name},</p>
            <p>Thank you for reaching out to us via our portfolio contact form. We appreciate your interest and will get back to you as soon as possible.</p>
            <p>Here is a copy of the message you sent:</p>
            <p><strong>Subject:</strong> {subject}</p>
            <p><strong>Message:</strong></p>
            <p>{message}</p>
            <p>I aim to respond to all inquiries within 24-48 hours. In the meantime, feel free to browse my portfolio for more information about my work.</p>
            <p>Best regards,<br/>
            Samir Chaulagain<br/>
            +977-9803510597</p>
            """



            # Sending an email notification to the site owner/administrator
            send_mail(
                subject,
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                settings.EMAIL_HOST_USER,
                [sender_email],  # Replace with the recipient's email address
                fail_silently=False,
            )

            # Sending an acknowledgment email to the sender
            send_mail(
                'Message Received, Thanks for Contacting Us',
                message,  # Plain text message, ignored if html_message is present
                settings.EMAIL_HOST_USER,
                [email],  # Use the email provided by the user in the form
                fail_silently=False,
                html_message=html_message,  # Pass the HTML content here
            )

            # Displaying success message if emails are sent successfully
            messages.success(request, 'Contact form has been successfully sent.')
            return HttpResponse('Email sent successfully!')
        except Exception as e:
            # Handling exceptions if email sending fails
            messages.error(request, f'An error occurred: {str(e)}')
            return HttpResponse('An error occurred while sending the email. Please try again later.')
    else:
        # Displaying error message if the request method is not 'POST'
        return HttpResponse('This view only accepts POST requests.')