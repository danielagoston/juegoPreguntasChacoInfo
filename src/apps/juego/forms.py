from django import forms

from Apps.preguntas.models import Pregunta, OpcionPregunta

from .models import Juego

class JuegoForm(forms.ModelForm):

	class Meta:
		model = Juego
		fields = ['dificultad',]

	def __init__(self, *args, **kwargs):

		super(JuegoForm , self).__init__(*args, **kwargs)
		
		self.fields['dificultad'].widget.attrs['class'] = 'form-control'


class PartidaForm(forms.ModelForm):

	class Meta:
		model = Juego
		fields = []

	def __init__(self, *args, **kwargs):

		super(PartidaForm , self).__init__(*args, **kwargs)
		
		for x in Juego.objects.get(pk=self.instance.id).preguntas.all():
			self.fields['Pregunta '+str(x.id)] = forms.ModelChoiceField(label='Pregunta: '+str(x.nombre), required=False, queryset=OpcionPregunta.objects.filter(pregunta=x), widget= forms.RadioSelect(attrs = {'placeholder':x.nombre}))