from django.shortcuts import render_to_response

from datetime import datetime
from qtwitter import buscador
from django import forms

class QueryForm(forms.Form):
    hashtag = forms.CharField(required=True, max_length=50)
    

def queryTwitter(request):
    ahora = datetime.now()
    if request.method == "POST":
        formulario = QueryForm(request.POST)
        if formulario.is_valid():
            cd = formulario.cleaned_data
            busqueda = cd['hashtag']
            lista_twetts = buscador(busqueda, 'null')

    else:
        formulario = QueryForm()
        lista_twetts = []

    return render_to_response('twitter.html', {'tweets':lista_twetts,
                                               'now':ahora,
                                               'formulario':formulario})