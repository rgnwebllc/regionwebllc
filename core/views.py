from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
from datetime import datetime

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        full_message = f"Name: {name}\nEmail: {email}\nPhone Number: {phone}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject=f"New Inquiry from {name}",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
            )
            messages.success(request, "✅ Thank you! Your message has been sent.")
        except Exception:
            messages.error(request, "❌ Sorry, something went wrong. Please try again.")
        
        return redirect('/#contact')
    
    return render(request, 'core/home.html', {'year': datetime.now().year})

def about_view(request):
    return render(request, 'core/about.html')

def portfolio_view(request):
    projects = [
        {
            'title': 'Tech Repair Site',
            'description': 'A modern service website with scheduling features.',
            'image_url': '/static/images/project1.jpg',
            'url': 'https://techrescuellc.com'
        },
        {
            'title': 'Tech Repair Site',
            'description': 'A modern service website with scheduling features.',
            'image_url': '/static/images/project1.jpg',
            'url': 'https://techrescuellc.com'
        },
        {
            'title': 'Tech Repair Site',
            'description': 'A modern service website with scheduling features.',
            'image_url': '/static/images/project1.jpg',
            'url': 'https://techrescuellc.com'
        },
        # {
        #     'title': 'E-Commerce Store',
        #     'description': 'Custom storefront for an apparel brand.',
        #     'image_url': '/static/images/project2.jpg',
        #     'url': 'https://example.com/project2'
        # },
        # {
        #     'title': 'Landing Page',
        #     'description': 'Minimal one-page site optimized for conversions.',
        #     'image_url': '/static/images/project3.jpg',
        #     'url': ''
        # },
    ]
    return render(request, 'core/portfolio.html', {'projects': projects})

def pricing_view(request):
    return render(request, 'core/pricing.html')