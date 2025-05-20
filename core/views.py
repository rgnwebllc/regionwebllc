from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import threading
from .models import *
from .forms import TestimonialForm

@csrf_exempt
def update_lead_status(request):
    if request.method == 'POST':
        token = request.headers.get("Authorization")
        if token != f"Bearer {settings.DISCORD_LOG_TOKEN}":
            return JsonResponse({"error": "Unauthorized"}, status=403)

        try:
            data = json.loads(request.body)
            lead_id = data.get("lead_id")
            new_status = data.get("status")

            if new_status not in dict(Lead.STATUS_CHOICES):
                return JsonResponse({"error": "Invalid status"}, status=400)

            lead = Lead.objects.get(id=lead_id)
            lead.status = new_status
            lead.save()
            return JsonResponse({"success": True, "message": f"Lead {lead_id} updated to {new_status}"})
        except Lead.DoesNotExist:
            return JsonResponse({"error": "Lead not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def forward_log_to_discord(request):
    if request.method == 'POST':
        token = request.headers.get("Authorization")
        if token != f"Bearer {settings.DISCORD_LOG_TOKEN}":
            return JsonResponse({"error": "Unauthorized"}, status=403)

        try:
            data = json.loads(request.body)
            if "embeds" in data:
                payload = {"embeds": data["embeds"]}
            else:
                message = data.get('message', 'No message provided')
                payload = {"content": f"[Render Log] {message}"}

            response = requests.post(settings.DISCORD_WEBHOOK_URL, json=payload)

            if response.status_code in (200, 204):
                return JsonResponse({"status": "success"}, status=200)
            else:
                return JsonResponse({"error": "Failed to send to Discord"}, status=500)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid method"}, status=405)

def send_log_embed(name, email, phone, message):
    def _post():
        url = "https://www.regionwebllc.com/log-to-discord/"
        headers = {
            "Authorization": f"Bearer {settings.DISCORD_LOG_TOKEN}",
            "Content-Type": "application/json"
        }
        embed = {
            "embeds": [
                {
                    "title": "📬 New Contact Form Submission",
                    "color": 5763719,
                    "fields": [
                        {"name": "Name", "value": name, "inline": True},
                        {"name": "Email", "value": email, "inline": True},
                        {"name": "Phone", "value": phone, "inline": True},
                        {"name": "Message", "value": message or "*No message provided.*"}
                    ],
                    "footer": {"text": "Region Web LLC"},
                    "timestamp": datetime.utcnow().isoformat()
                }
            ]
        }
        try:
            requests.post(url, json=embed, headers=headers, timeout=5)
        except requests.exceptions.RequestException:
            pass

    threading.Thread(target=_post).start()

def send_consultation_embed(name, email, business, budget, details):
    def _post():
        url = "https://www.regionwebllc.com/log-to-discord/"
        headers = {
            "Authorization": f"Bearer {settings.DISCORD_LOG_TOKEN}",
            "Content-Type": "application/json"
        }
        embed = {
            "embeds": [
                {
                    "title": "📝 New Consultation Request",
                    "color": 3447003,
                    "fields": [
                        {"name": "Name", "value": name, "inline": True},
                        {"name": "Email", "value": email, "inline": True},
                        {"name": "Business", "value": business, "inline": True},
                        {"name": "Budget", "value": budget or "N/A", "inline": True},
                        {"name": "Details", "value": details or "*No details provided.*"}
                    ],
                    "footer": {"text": "Region Web LLC"},
                    "timestamp": datetime.utcnow().isoformat()
                }
            ]
        }
        try:
            requests.post(url, json=embed, headers=headers, timeout=5)
        except requests.exceptions.RequestException:
            pass

    threading.Thread(target=_post).start()

def send_testimonial_embed(name, role, company_name, quote):
    def _post():
        url = "https://www.regionwebllc.com/log-to-discord/"
        headers = {
            "Authorization": f"Bearer {settings.DISCORD_LOG_TOKEN}",
            "Content-Type": "application/json"
        }
        embed = {
            "embeds": [
                {
                    "title": "🌟 New Testimonial Submitted",
                    "color": 15844367,  # Gold tone
                    "fields": [
                        {"name": "Name", "value": name or "N/A", "inline": True},
                        {"name": "Role", "value": role or "N/A", "inline": True},
                        {"name": "Company", "value": company_name or "N/A", "inline": True},
                        {"name": "Quote", "value": quote or "*No quote provided.*"}
                    ],
                    "footer": {"text": "Region Web LLC"},
                    "timestamp": datetime.utcnow().isoformat()
                }
            ]
        }
        try:
            requests.post(url, json=embed, headers=headers, timeout=5)
        except requests.exceptions.RequestException:
            pass

    threading.Thread(target=_post).start()



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
        except Exception as e:
            print("❌ Email error:", e)
            messages.error(request, "❌ Email failed. Please try again.")
            return redirect('/#contact')

        try:
            send_log_embed(name, email, phone, message)
        except Exception as e:
            print("⚠️ Discord log error:", e)

        return redirect('/#contact')

    return render(request, 'core/home.html', {'year': datetime.now().year})

def consultation_request(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        business = request.POST.get('business')
        budget = request.POST.get('budget')
        details = request.POST.get('details')

        # 🔗 Construct Discord embed
        embed = {
            "embeds": [
                {
                    "title": "📝 New Consultation Request",
                    "color": 3447003,
                    "fields": [
                        {"name": "Name", "value": name, "inline": True},
                        {"name": "Email", "value": email, "inline": True},
                        {"name": "Business", "value": business, "inline": True},
                        {"name": "Budget", "value": budget or "N/A", "inline": True},
                        {"name": "Details", "value": details or "*No details provided.*"}
                    ],
                    "footer": {"text": "Region Web LLC"},
                    "timestamp": datetime.utcnow().isoformat()
                }
            ]
        }

        discord_message_id = None
        try:
            headers = {
                "Authorization": f"Bearer {settings.DISCORD_LOG_TOKEN}",
                "Content-Type": "application/json"
            }
            response = requests.post("https://www.regionwebllc.com/log-to-discord/", json=embed, headers=headers)
            if response.status_code == 200:
                discord_message_id = response.json().get("id")
        except Exception as e:
            print("⚠️ Discord logging failed:", e)

        # 🧾 Save lead including Discord message ID
        Lead.objects.create(
            name=name,
            email=email,
            business=business,
            budget=budget,
            details=details,
            status='new',
            discord_message_id=discord_message_id
        )

        # ✉️ Send email
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
            messages.error(request, "❌ Email failed. Please try again.")

        return redirect('/free-consultation/#consultation')

    return render(request, 'core/home.html', {'year': datetime.now().year})



def about_view(request):
    return render(request, 'core/about.html')

def features_view(request):
    return render(request, 'core/features.html')

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
            'url': ''
        },
        {
            'title': 'Your Website Here',
            'description': "Contact us today and have your website posted here.",
            'image_url': '/static/images/placeholder.png',
            'url': ''
        },
    ]
    return render(request, 'core/portfolio.html', {'projects': projects})

def testimonials_view(request):
    testimonials = Testimonial.objects.filter(approved=True).order_by('-created_at')
    form = TestimonialForm()

    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.approved = False  # Set to True if no moderation needed
            testimonial.save()
            
            # ⬇️ Log to Discord
            send_testimonial_embed(
                testimonial.name,
                testimonial.role,
                testimonial.company_name,
                testimonial.quote
            )

            messages.success(
                request,
                "Thank you for your testimonial. Your submission is pending and will be posted once approved."
            )
            return redirect('testimonials')

    return render(request, 'core/testimonials.html', {
        'testimonials': testimonials,
        'form': form
    })

def consultation_view(request):
    return render(request, 'core/pricing.html')