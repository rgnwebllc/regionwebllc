from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import date

@login_required
def dashboard_view(request):
    # Dummy data — replace with actual DB queries later
    recent_payments = [
        {'date': date(2024, 4, 22), 'amount': 99.99},
        {'date': date(2024, 3, 15), 'amount': 49.99},
    ]
    active_websites = [
        {'name': 'Client Site 1', 'url': 'https://example1.com'},
        {'name': 'Client Site 2', 'url': 'https://example2.com'},
    ]

    return render(request, 'accounts/dashboard.html', {
        'recent_payments': recent_payments,
        'active_websites': active_websites,
    })
