from django.db import models

# Create your models here.


class Generacion(models.Model):
    generacion = models.DateField()
    
    def __str__(self):
        return str(self.generacion)

class Escuela(models.Model):
    generacion = models.ForeignKey(Generacion, on_delete=models.CASCADE, 
    null=True, blank=True, related_name='año')
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    director = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Grupo (models.Model):
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE, 
    null=True, blank=True,
    related_name='salon')
    grupo = models.CharField(max_length=10)
    jefe_grupo =models.CharField(max_length=20, null=True, blank=True)
    folio_grupo = models.CharField(max_length=5, null=True, blank=True)
    postales = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return self.grupo


moldura =  [  
    (1, 'PIRAMIDAL NEGRO'),
    (2, 'PIRAMIDAL VINO'),
    (3, 'PIRAMIDAL CAFE'),

    (4, 'ROLEX CAFE'),
    (5, 'ROLEX NEGRO'),
    (6, 'ROLEX VINO'),


    (9, 'CRISTAL GRANDE'),

    (10, 'MERCURIO'),
    (11, 'CORONA'),
    (12, 'ESTRELLA'),
    (14, 'MARIPOSA'),
    (15, 'ROMANA'),
    (16, 'MONACO'),

    (17, 'ANUBIS'),
    (18, 'ESLOVENIA'),
    (19, 'INGLESA'),
    (20, 'BERLIN'),
    (21, 'FLORENCIA'),
    (22, 'RESINA'),
    (23, 'CRISTAL CHICO'),

]
placa = [

    (12, '---'),
    (1, 'MEDITERRANEA'),
    (2, '4 PIEZAS'),
    (3, 'PELLISCO'),
    (4, 'PLANA'),
    (5, 'CORTE PLANO'),
    (6, 'CORAZON'),
    (7, 'PALERMO'),
    (8, 'PERGAMINO'),
    (9, 'COLUMNAS'),
    (10, 'CIRCULO'),
    (11, 'piramide'),
]
colorPlaca = [ 

    (7, '---'),
    (1, 'CAFE'),
    (2, 'NEGRO'),
    (3, 'ROJO'),
    (4, 'AZUL'),
    (5, 'VERDE'),
    (6, 'PLATA'),
]

class Alumno (models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, 
    null=True, blank=False, related_name='alumno')
    nombre = models.CharField(max_length=30)
    tipo_moldura = models.IntegerField(null=True, blank=False, choices=moldura)
    tipo_placa = models.CharField(max_length=20,null=True, blank=False, choices=placa, default=1)
    color_placa = models.CharField(max_length=20, null=True, blank=False, choices=colorPlaca,default=1)
    folio = models.CharField(max_length=6, null=True, blank=True)
    pedido_extra= models.CharField(max_length=20, null=True, blank=True)
    taza = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Pago (models.Model):
    nombre = models.ForeignKey(Alumno, on_delete=models.CASCADE,
    null=True, blank=False, related_name='anticipo')
    monto = models.FloatField(max_length=10)
    fecha= models.DateField(null=True, blank=False)

    def __str__(self):
        return self.monto

class Control (models.Model):
    nombre = models.ForeignKey(Alumno, on_delete=models.CASCADE,
    null=True, blank=False, related_name='control')
    foto_enviada = models.DateField(null=True, blank=True)
    archivo_foto = models.CharField(max_length=25, null=True, blank=True)
    placa_enviada = models.DateField(null=True, blank=True)
    archivo_placa = models.CharField(max_length=25, null=True, blank=True)
    foto_recibida = models.DateField(null=True, blank=True)
    placa_recibida = models.DateField(null=True, blank=True)
    foto_armada = models.DateField(null=True, blank=True)
    foto_entregada = models.DateField(null=True, blank=True)


