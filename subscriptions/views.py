from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from subscriptions.forms import SubscriptionForm
from subscriptions.models import Subscription
from django.core import mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})

    subscription = Subscription.objects.create(**form.cleaned_data)

    _send_mail(
        'subscriptions/subscription_email.txt',
        {'subscription': subscription},
        'Confirmação de inscrição!',
        settings.DEFAULT_FROM_EMAIL,
        subscription.email)

    return HttpResponseRedirect('/inscricao/{}/'.format(subscription.pk))


def new(request):
    return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})


def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        raise Http404

    return render(request,
                  'subscriptions/subscription_detail.html',
                  {'subscription': subscription})


def _send_mail(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    email = mail.send_mail(subject, body, from_, [from_, to])
