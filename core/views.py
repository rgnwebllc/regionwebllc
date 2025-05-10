from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from datetime import datetime


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        subject = f"New Inquiry from {name}"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [settings.CONTACT_RECEIVER_EMAIL]

        # Plain text (fallback)
        text_content = f"""
Name: {name}
Email: {email}
Phone Number: {phone}

Message:
{message}
        """

        # HTML version using Django template (or inline if preferred)
        html_content = render_to_string('emails/inquiry_email.html', {
        'name': name,
        'email': email,
        'phone': phone,
        'message': message,
        'year': datetime.now().year,
})

        try:
            msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, "✅ Thank you! Your message has been sent.")
        except Exception:
            messages.error(request, "❌ Sorry, something went wrong. Please try again.")

        return redirect('/#contact')

    return render(request, 'core/home.html', {'year': datetime.now().year})

def consultation_request(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        business = request.POST.get('business')
        budget = request.POST.get('budget')
        details = request.POST.get('details')

        subject = f"Free Consultation Request from {name}"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [settings.CONTACT_RECEIVER_EMAIL]

        text_content = f"""
Name: {name}
Email: {email}
Business: {business}
Budget: {budget}

Details:
{details}
        """

        html_content = render_to_string('emails/consultation_email.html', {
            'name': name,
            'email': email,
            'business': business,
            'budget': budget,
            'details': details,
            'year': datetime.now().year,
        })

        try:
            msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, "✅ Thank you! We'll follow up with you shortly.")
        except Exception:
            messages.error(request, "❌ Something went wrong. Please try again.")

        return redirect('/consultation/#consultation')

    return redirect('/')


def about_view(request):
    return render(request, 'core/about.html')

def portfolio_view(request):
    projects = [
        {
            'title': 'Tech Rescue LLC',
            'description': 'A modern service website with scheduling features.',
            'image_url': '/static/images/project1.jpg',
            'url': 'https://techrescuellc.com'
        },
        {
            'title': 'Your Website Here',
            'description': 'Contact us today and have your website posted here.',
            'image_url': '/static/images/placeholder.png',
            'url': '#'
        },
        {
            'title': 'Your Website Here',
            'description': "It's free advertisement.",
            'image_url': '/static/images/placeholder.png',
            'url': '#'
        },
    ]
    return render(request, 'core/portfolio.html', {'projects': projects})

def consultation_view(request):
    return render(request, 'core/pricing.html')