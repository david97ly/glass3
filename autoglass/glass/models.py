from django.db import models


# Create your models here.



class Order(models.Model):
    orden = models.CharField(max_length = 10)

    def __unicode__(self):
        return "%s " % (self.orden)



class Fotos(models.Model):
	nombre = models.CharField(max_length=500)
	ruta = models.ImageField(upload_to='photos')
	valida = models.BooleanField(default=False)

	def __unicode__(self):
		return self.Snombre


class Slide(models.Model):
	mensaje = models.CharField(max_length=500)
	submensaje = models.CharField(max_length=500)
	valida = models.BooleanField(default=False)
	orden = models.ForeignKey(Order)
	foto = models.ImageField(upload_to='photos')


	def __unicode__(self):
		return "%s - %s " % (self.mensaje,self.submensaje)


class Mensajeb(models.Model):
	mensaje = models.CharField(max_length=500)
	submensaje = models.CharField(max_length=500)
	valida = models.BooleanField(default=False)
	foto = models.ImageField(upload_to='photos',null = True)

	def __unicode__(self):
		return "%s - %s " % (self.mensaje,self.submensaje)

class Servicios(models.Model):
    titulo = models.CharField(max_length=500,null=True)
    valida = models.BooleanField(default=False)
    orden = models.ForeignKey(Order)

    def __unicode__(self):
        return "%s " % (self.titulo)


class Info(models.Model):
    servicio = models.ForeignKey(Servicios)
    titulo = models.CharField(max_length=500)
    informacion = models.TextField(max_length=20000,null=True)
    valida = models.BooleanField(default=False)
    orden = models.ForeignKey(Order)
    foto = models.ImageField(upload_to='photos')

    def __unicode__(self):
        return "%s " % (self.titulo)


class Contactos(models.Model):
	telefono1 = models.CharField(max_length=500)
	telefono2 = models.CharField(max_length=500)
	correo = models.CharField(max_length=500)
	fax = models.CharField(max_length=500)
	address = models.CharField(max_length=500)

	def __unicode__(self):
		return "%s - %s " % (self.telefono1,self.correo)




class ServiPrin(models.Model):
	orden = models.ForeignKey(Order)
	servicio = models.ForeignKey(Servicios)

	def __unicode__(self):
		return "%s - %s" % (self.servicio.titulo,self.orden.orden)

class Visitas(models.Model):
	home = models.IntegerField(default=0)
	servi= models.IntegerField(default=0)
	fotos = models.IntegerField(default=0)
	contacto= models.IntegerField(default=0)
	mapa = models.IntegerField(default=0)

	def __unicode__(self):
		return "home %i - servicios %i - fotos %i - contactos %i - mapa %i" % (self.home, self.servi,self.fotos,self.contacto,self.mapa)
