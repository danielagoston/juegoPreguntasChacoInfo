from django import forms

from apps.preguntas.models import Pregunta, Opcion

from .models import Partida

class PartidaForm(forms.ModelForm):
    
    class Meta:
        model = Partida
        fields = []
        
    def __init__(self, *args, **kwargs):
            
        super(PartidaForm , self).__init__(*args, **kwargs)
            
        for x in Partida.objects.get(pk=self.instance.id).preguntas.all():
            print(x)
            self.fields['Pregunta '+str(x.id)] = forms.ModelChoiceField(label='Pregunta: '+str(x.pregunta), required=False, queryset=Opcion.objects.filter(pertenecientePregunta=x), widget= forms.RadioSelect(attrs = {'placeholder':x.pregunta}))