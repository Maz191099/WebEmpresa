from django import forms

class ContactForm(forms.Form):
    name =      forms.CharField(label="Nombre", required=True)
    email =     forms.EmailField(label="Email", required=True)
    contect =   forms.CharField(label="Mensaje", required=True, widget=forms.Textarea)