from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from .models import Event, News, Testimonial


def home_page(request: HttpRequest) -> HttpResponse:
    latest_news = News.objects.all()[:5]
    testimonials = Testimonial.objects.all()[:3]
    return render(request, 'website/home.html', {
        'latest_news': latest_news,
        'testimonials': testimonials,
    })


def about_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'website/about.html')


def performances_page(request: HttpRequest) -> HttpResponse:
    upcoming = Event.objects.filter(is_upcoming=True).order_by('date')
    past = Event.objects.filter(is_upcoming=False).order_by('-date')[:10]
    return render(request, 'website/performances.html', {'upcoming': upcoming, 'past': past})


def gallery_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'website/gallery.html')


def bookings_page(request: HttpRequest) -> HttpResponse:
    from .forms import BookingForm

    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned = form.cleaned_data
            subject = f"New Booking: {cleaned['name']} - {cleaned['event_date']}"
            body = (
                f"Name: {cleaned['name']}\n"
                f"Email: {cleaned['email']}\n"
                f"Phone: {cleaned.get('phone', '')}\n"
                f"Event Date: {cleaned['event_date']}\n"
                f"Event Type: {cleaned['event_type']}\n\n"
                f"Message:\n{cleaned['message']}"
            )
            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'website/bookings.html', {'form': form})


def contact_page(request: HttpRequest) -> HttpResponse:
    from .forms import ContactForm

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            subject = f"Contact Form: {cleaned['name']}"
            body = (
                f"Name: {cleaned['name']}\n"
                f"Email: {cleaned['email']}\n\n"
                f"Message:\n{cleaned['message']}"
            )
            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

# Create your views here.
