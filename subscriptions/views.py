from django.http import HttpResponseRedirect
from django.shortcuts import render
from subscriptions.forms import SubscriptionForm
from django.core import mail
from django.template.loader import render_to_string

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        form.full_clean()
        body = render_to_string('subscriptions/subscription_email.txt',form.cleaned_data)
        mail.send_mail('Confirmação de inscrição',
                        body,
                        'contato@eventif.com.br',
                        ['contato@eventif.com.br', form.cleaned_data['email']])
        return HttpResponseRedirect('/inscricao/')
    context = {"form": SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)