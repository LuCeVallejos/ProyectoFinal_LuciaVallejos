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





class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to="media/avatares", null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
    




class Perfil(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=2200)

    def __str__(self):
        return f"{self.usuario}"





class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to="media/posts", null=True, blank=True)
    epigrafe = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.epigrafe}"




class Comentario(models.Model):
    id = models.BigAutoField(primary_key=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.CharField(max_length=2200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"@{self.autor}: '{self.post}'"

