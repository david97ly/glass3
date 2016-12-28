from django import forms

from models import *



class MensajebForm(forms.ModelForm):
    class Meta:
        model = Mensajeb
        exclude = ("foto",)

class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        exclude = ()



class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        exclude = ('servicio',)

class ContactosForm(forms.ModelForm):
    class Meta:
        model = Contactos
        exclude = ()

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = Servicios
        exclude = ()

class FotosForm(forms.ModelForm):
    class Meta:
        model = Fotos
        exclude = ()

class ServiPrinForm(forms.ModelForm):
    class Meta:
        model =ServiPrin
        exclude = ()

class VisitasForm(forms.ModelForm):
    class Meta:
        model =ServiPrin
        exclude = ()
