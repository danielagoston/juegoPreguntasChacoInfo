from django.db import models

class CategoriaPregunta(models.Model):
	nombreCategoria = models.CharField(max_length=50)
	
	class Meta:
		db_table = 'categorias'
		
	def __str__(self):
		return self.nombreCategoria

class Pregunta(models.Model):
	pregunta = models.CharField(max_length=250)
	categoriaPregunta = models.ForeignKey(CategoriaPregunta, on_delete=models.CASCADE)

	dificultad = [
	    ('1', 'Fácil'),
	    ('2', 'Media'),
	    ('3','Difícil'),
    ]
	dificultadPregunta = models.CharField(max_length=1,choices=dificultad,default='1')

	def __str__(self):
		return self.pregunta


class Opcion(models.Model):
    texto = models.CharField(max_length=250)
    pertenecientePregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    valido = models.BooleanField(default=False)
    
    def __str__(self):
        return self.texto