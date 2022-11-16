from django import forms

class ComicsFormulario(forms.Form):

    titulo = forms.CharField()
    guionista = forms.CharField()
    dibujante = forms.CharField()
    otros_artistas = forms.CharField()
    editorial = forms.CharField()

class GuionistasFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()

class DibujantesFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()

class EditorialesFormulario(forms.Form):

    nombre = forms.CharField()
    país = forms.CharField()