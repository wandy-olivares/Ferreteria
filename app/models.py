from django.db import models
from django.contrib.auth.models import AbstractUser


# Modelo para agregar imagenes de bienveinida en el inicio (header)
class WellcomeStart(models.Model):
      name_img = models.CharField(max_length=100)
      photo_welcome = models.ImageField(upload_to="", blank=True, null=True)
      photo_welcome_uno = models.ImageField(upload_to="", blank=True, null=True)
      photo_welcome_dos = models.ImageField(upload_to="", blank=True, null=True)
      photo_welcome_tres = models.ImageField(upload_to="", blank=True, null=True)

      
      
      
      def __str__(self) -> str:
            return self.name_img    


# Modelo extendido de user
class User(AbstractUser):
      paypal = models.CharField(max_length=100, blank=True)
      transferencia = models.CharField(max_length=100, blank=True)
      instagram = models.CharField(max_length=100, blank=True)
      facebook = models.CharField(max_length=100, blank=True)
      gmail = models.CharField(max_length=100, blank=True)
      photo = models.ImageField(upload_to="", blank=True, null=True)





# TourUser reprenta que el usuario tiene que tener un Tour en su historial de viajes
class Tour_user_model(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      name = models.CharField(max_length=100, blank=True    )
      number_id_tour = models.IntegerField(default=0, blank=True)

      def __str__(self) -> int:
            return self.name



# Box of    models Tours
class Box_tours(models.Model):
      name_tour = models.CharField(max_length=100)
      code_paquet = models.CharField(max_length=100, blank=True)
      value_cu= models.CharField(max_length=100, blank=True)

      price = models.CharField(max_length=10)
      description = models.CharField(max_length=500)
      
      dia = models.CharField(max_length=100, default=False)
      limites = models.CharField(max_length=100, blank=True)

      photo = models.ImageField(upload_to="", blank=True, null=True)
      photo1_s = models.ImageField(upload_to="", blank=True, null=True)
      photo2_s = models.ImageField(upload_to="", blank=True, null=True)
      photo3_s = models.ImageField(upload_to='', blank=True, null=True)
      photo4_s =models.ImageField(upload_to='', blank=True, null=True)

      buy_getting = models.IntegerField(default=0, blank=True)
      reserved_getting = models.IntegerField(default=0, blank=True)

      asientos = models.IntegerField(default=0, blank=True)

      def __str__(self) -> str:
            return self.name_tour
      


      

class Get_buy_tours(models.Model):
      box_tours = models.ForeignKey(Box_tours, on_delete=models.CASCADE)
      number_get_buy = models.IntegerField(default=0, blank=True)      

      def __str__(self) -> int:
            return str(self.number_get_buy)
      


class Blog(models.Model):
      title = models.CharField(max_length=100)
      description = models.CharField(max_length=500)
      photo = models.ImageField(upload_to="", blank=True, null=True)
      date = models.DateTimeField(auto_now_add=True)

      def __str__(self) -> str:
            return self.title
      

class Faq(models.Model):
      question = models.CharField(max_length=100)
      answer = models.CharField(max_length=500)