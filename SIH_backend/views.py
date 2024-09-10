from django.shortcuts import render, redirect
from django.core.mail import send_mail

def index(request):
    result = None
    if request.method == 'POST' and request.FILES['video']:
        video = request.FILES['video']
        # Logic to check if the video is a deepfake (placeholder)
        result = "Deepfake detected"  # or "Not a deepfake"
    return render(request, 'index.html', {'result': result})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            f"Message from {name}",
            message,
            email,
            ['nirajitpramanik@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')
