from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import date
from django.utils.safestring import mark_safe
import json

@login_required
def dashboard_view(request):
    # Dummy data — replace with actual DB queries later
    recent_payments = [
        {'date': date(2024, 4, 22), 'amount': 99.99},
        {'date': date(2024, 3, 15), 'amount': 49.99},
    ]
    active_websites = [
    {'name': 'Site A', 'url': 'https://site-a.com', 'clicks': 140},
    {'name': 'Site B', 'url': 'https://site-b.com', 'clicks': 95},
    {'name': 'Site C', 'url': 'https://site-c.com', 'clicks': 130},
    {'name': 'Site D', 'url': 'https://site-d.com', 'clicks': 60},
    {'name': 'Site E', 'url': 'https://site-e.com', 'clicks': 400},
    {'name': 'Site F', 'url': 'https://site-f.com', 'clicks': 35},
]
    website_names = [site['name'] for site in active_websites]
    click_counts = [site['clicks'] for site in active_websites]


    return render(request, 'accounts/dashboard.html', {
    'recent_payments': recent_payments,
    'active_websites': active_websites,
    'website_names': mark_safe(json.dumps(website_names)),
    'click_counts': mark_safe(json.dumps(click_counts)),
})

@login_required
def payments_view(request):
    return render(request, 'accounts/payments.html')

@login_required
def settings_view(request):
    return render(request, 'accounts/settings.html')