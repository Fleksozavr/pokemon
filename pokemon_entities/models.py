from django.db import models  # noqa F401

# your models here


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.title
    

class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()

    apperated_at = models.DateTimeField(null=True)
    disappeared_at = models.DateTimeField(null=True)

    level = models.IntegerField(default=100)
    heal = models.IntegerField(default=100)
    strength = models.IntegerField(default=100)
    defence = models.IntegerField(default=100)
    stamina = models.IntegerField(default=100)

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True)