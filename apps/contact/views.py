from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings

from .forms import ContactForm


def sendmail_contact_success(to_email):
    subject = "We receive your message."
    message = "Thank you for your message. We will contact you soon to answer all your questions."
    try:
        send_mail(
            subject,
            message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[to_email],
        )
    except BadHeaderError:
        return HttpResponse("Invalid header found.")


def sendmail_to_us(subject, message):
    try:
        send_mail(
            subject,
            message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
        )
    except BadHeaderError:
        return HttpResponse("Invalid header found.")


def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            message = form.cleaned_data["message"]
            name = form.cleaned_data["name"]
            phone_number = form.cleaned_data["phone_number"].as_e164
            email = form.cleaned_data["email"]

            sendmail_contact_success(email)

            subject = f"New Message from: email={email}"
            body = "name=" + name + "\r\n" + "phone=" + phone_number + "\r\n" + message
            sendmail_to_us(subject, body)

            return redirect("success")

    context = {"form": form}
    return render(request, "contact/contact.html", context)


def successView(request):
    return render(request, "contact/success.html")
