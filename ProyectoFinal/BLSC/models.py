from django.db import models
from django.contrib.auth.models import User


class Obra(models.Model):
    ObraSeleccion = (
    ('poesía','Poesía'),
    ('ficción', 'Ficción'),
    ('no-ficción','No-ficción'),
    ('drama','Drama'),
    ('ensayo','Ensayo'),
    ('otro', 'Otro'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=15, choices=ObraSeleccion, default='otro')
    autor = models.CharField(max_length=40)
    año = models.IntegerField() 
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(null=True, blank=True)
    emailUsuario = models.EmailField()
    imagenObra = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    class Meta:
        ordering = ['usuario', '-fechaPublicacion']

    def __str__(self):
        return self.titulo



class Comentario(models.Model):
    comentario = models.ForeignKey(Obra, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return f"@{self.nombre} comentó: '{self.comentario}'"







