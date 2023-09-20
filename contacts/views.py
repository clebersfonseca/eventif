from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.core import mail
from django.shortcuts import render
from django.template.loader import render_to_string
from contacts.forms import ContatcForm


def contact(request):
    if request.method == 'POST':
        form = ContatcForm(request.POST)

        if form.is_valid():
            body = render_to_string('contacts/contact_email.txt', form.cleaned_data)

            mail.send_mail('Contato',
                           body,
                           form.cleaned_data['email'],
                           ['contato@eventif.com.br', form.cleaned_data['email']])
            messages.success(request, 'Contato enviado com sucesso!')
            return HttpResponseRedirect('/contato/')
        else:
            return render(request, 'contacts/contact_form.html', {'form': form})

    else:
        return render(request, 'contacts/contact_form.html', {'form': ContatcForm()})