from django.shortcuts import render
from django.views.generic import ListView, CreateView 
from django.views.generic.edit import UpdateView 
from django.urls import reverse_lazy

from .models import Partida
from apps.preguntas.models import Pregunta, Opcion

import random

class ListaDePartidas(ListView):
    model = Partida
    template_name = 'partidas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['Partidas'] = Partida.objects.filter(player1=self.request.user)

        return context

class CrearPartida(CreateView):
    model = Partida
    template_name = 'partida.html'
    fields = ['dificultad']
    success_url = reverse_lazy('partidas')

    def form_valid(self, form):
        
        f = form.save(commit=False)

        preguntas = list(Pregunta.objects.filter(dificultadPregunta=f.dificultad))
        
        f.player1 = self.request.user

        f = form.save(commit=True)

        f.preguntas.set(random.sample(preguntas, 3))
         
        return super(CrearPartida, self).form_valid(form)

class JugandoPartida(UpdateView):
    model = Partida
    template_name = 'jugandopartida.html'
    fields = []
    success_url = reverse_lazy('partidas')

    def form_valid(self, form):
        
        f = form.save(commit=False)

        formValues = []

        for x in self.request.POST:
            formValues.append(self.request.POST.get(x, None))

        formValues.pop(0)

        correctas = 0
        for clave in formValues:
            if(Opcion.objects.get(pk=clave).correcta):
                correctas +=1

        if correctas < 2:
            f.puntos = 0
        elif correctas == 2:
            f.puntos = int(self.object.dificultad)
        else:
            f.puntos = int(self.object.dificultad) * 2

        f.finalizado = True
        
        return super(JugandoPartida, self).form_valid(form)