from django.db import models

# Create your models here.

class Log(models.Model):
	text = models.CharField(max_length=100)
	data = models.CharField(max_length=100)
	hora = models.CharField(max_length=100)

class Usuario(models.Model):
	nome = models.CharField(max_length=150)
	senha = models.CharField(max_length=30)
	email = models.EmailField(max_length=64, unique=True)

class Historico_jogo(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
	usuario_nome = models.CharField(max_length=100)
	adversario_nome = models.CharField(max_length=100,default='')
	dificuldade = models.CharField(max_length=15)
	cor = models.CharField(max_length=15)
	velocidade = models.CharField(max_length=10)
 
class Velocidades(models.Model):
	velocidade = models.CharField(max_length=10)
 
class Cores(models.Model):
    cor = models.CharField(max_length=15)

class Dificuldades(models.Model):
    dificuldade = models.CharField(max_length=15)
    
class Cores_UI(models.Model):
    coresUI = models.CharField(max_length=20)
    
class Numero_Logs_Historicos(models.Model):
    numeroLogs = models.IntegerField(default=0)
    numeroHistoricos = models.IntegerField(default=0)
    
class Usuario_Logado(models.Model):
    usuario_email = models.EmailField(max_length=64)
    logado = models.CharField(max_length=1)