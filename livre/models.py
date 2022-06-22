from django.db import models

# Create your models here.

class Time(models.Model):
    nome = models.CharField(("Nome"), max_length=30)
    nome_abr = models.CharField(("Apelido"), max_length=5)
    logo = models.ImageField(("foto"), upload_to='', blank=True, null=True)
    class Meta:
        ordering = ('nome',)
    def __str__(self):
        return self.nome

class Jogo(models.Model):
    rodada = models.IntegerField()
    num = models.IntegerField(blank=True, null=True)
    num2 = models.IntegerField(blank=True, null=True)
    timea = models.CharField(max_length=30)
    placara = models.IntegerField(null=True, blank=True)
    placarb = models.IntegerField(null=True, blank=True)
    timeb = models.CharField(max_length=30)
    gols_total = models.IntegerField(blank=True, null=True)
    class Meta:
        ordering= ('rodada',)
    def __str__(self):
        return str(self.rodada) + "ª - " + self.timea + " x " + self.timeb

class Pontuar(models.Model):
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    j = models.IntegerField(default=0)
    pg = models.IntegerField(default=0)
    v =  models.IntegerField(default=0)
    e =  models.IntegerField(default=0)
    d = models.IntegerField(default=0)
    gp = models.IntegerField(default=0)
    gc = models.IntegerField(default=0)
    sg = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = "Tabelas"
        verbose_name = "Time"
    def __str__(self):
        return self.time.nome

