from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class punctuacion(models.Model):
    puntuaciones = models.CharField(choices=(('bajo',1),('medio-bajo',2),('medio',3),('medio-alto',4),('alto',5)),max_length=20,blank=True)
    def __unicode__(self):
        return self.puntuaciones
class client(User):
    birth = models.DateField()
    #def natural_key(self):
    #    return (self.username,self.birth)
    def __unicode__(self):
        return self.username
class caracteristic(models.Model):
    type = models.CharField(max_length=40)
    information = models.TextField(max_length=200)
    def natural_key(self):
        return (self.type,self.information)
    def __unicode__(self):
        return self.type+" : "+self.information
    class Meta:
        unique_together = (('type', 'information'))
class price(models.Model):
    coins = models.CharField(max_length=30,choices=(('libras','libras'),('euros','euros'),('dollar','dollar')))
    cuantity = models.DecimalField(max_digits=6,decimal_places=2)
    link = models.URLField()
    def __unicode__(self):
        return self.cuantity.__str__()+" "+self.coins
class phone(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images',verbose_name="Imagen telefono",blank=True)
    tiempo_registro = models.DateField(auto_now=True)
    caracteristics_that_own = models.ManyToManyField(caracteristic)
    price_that_has = models.ForeignKey(price)
    visitas = models.IntegerField(default=0)
    puntuaction_that_has = models.ManyToManyField(punctuacion,blank=True)
    #natural_key.dependencies = ['example_app.person']
    def __unicode__(self):
        return self.name