from django.http.response import HttpResponse

from django.shortcuts import redirect, render
from django.urls import reverse

from app.forms import SubscribeForm
from app.models import Subscription

# Create your views here.
def home(request):
    users = Subscription.objects.all()
    context = {"users": users}
    return render(request, "app/index.html", context)

def subscribe(request):
    subscribe_form = SubscribeForm()
    error_message = ""
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            return redirect(reverse("thank_you"))

    context = {"form": subscribe_form, "error_message": error_message}
    return render(request, "app/subscribe.html", context)


def thank_you(request):
    context = {}
    return render(request, "app/thank_you.html", context)