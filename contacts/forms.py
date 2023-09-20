from django import forms

class ContatcForm(forms.Form):
    name = forms.CharField(label='Nome')
    phone = forms.CharField(label="Telefone", required=False)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, label="Mensagem")