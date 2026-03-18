from django.db import models

class Veduci(models.Model):
    meno = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.meno

    class Meta:
        verbose_name = "Vedúci"
        verbose_name_plural = "Vedúci"

class Kruzok(models.Model):
    nazov = models.CharField(max_length=100)
    den = models.CharField(max_length=20)
    miestnost = models.CharField(max_length=50)
    # Prepojenie na model Veduci (1 vedúci môže mať viac krúžkov)
    veduci = models.ForeignKey(Veduci, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nazov} ({self.den})"

    class Meta:
        verbose_name = "Krúžok"
        verbose_name_plural = "Krúžky"