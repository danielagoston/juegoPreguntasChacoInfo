from django.db import models

from apps.preguntas.models import Pregunta


from apps.usuarios.models import Usuario

class Partida(models.Model):
    
    player1 = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    preguntas = models.ManyToManyField(Pregunta, related_name="PreguntasDeLaPartida")
    
    termino = models.BooleanField(default=False)
    
    dificultad = [
	    ('1', 'Fácil'),
	    ('2', 'Media'),
	    ('3','Difícil'),
    ]
    dificultad = models.CharField(max_length=1,choices=dificultad,default='1')

    puntaje = models.PositiveBigIntegerField(default=0)
        
    def __str__(self):
        return 'Partida ' + str(self.id) + ' de ' + self.player1