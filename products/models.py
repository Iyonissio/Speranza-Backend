from django.db import models

class Condutor(models.Model):
    name  = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Viatura(models.Model):
    marca = models.CharField(max_length=30, blank=True)
    modelo = models.CharField(max_length=30, blank=True)
    cor_da_viatura = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.marca

class Chapa(models.Model):
    MATOLA_GAR = 'Matola Gar / Magoanini'
    NKOBE = 'Nkobe / Baixa'
    AVOADOR = 'A. Voador / Xipamanine'
    PRACA_DOS_COMBATENTES = 'Museu / P. Combatentes'

    ROTAS_POSSIVEIS = [
        (AVOADOR, 'A. Voador / Xipamanine'),
        (PRACA_DOS_COMBATENTES, 'Museu / P. Combatentes'),
        (MATOLA_GAR, 'Matola Gar / Magoanini'),
        (NKOBE, 'Nkobe / Baixa'), 
    ]

    ALCOOL= 'Condução sob efeito de Alcool'
    VELOCIDADE = 'Excesso de Velocidade'
    SUPERLOTACAO = 'Superlotação' 
    TIPO_INFRACAO = [
        (ALCOOL, 'Condução sob efeito de alcool'),
        (VELOCIDADE, 'Excesso de velocidade'),
        (SUPERLOTACAO, 'Superlotação'),
    ]

    LIMPO = 'Limpo'
    ACEITAVEL = 'Aceitavel'
    SUJO = 'Sujo'
    MUITO_SUJO = 'Muito Sujo'
    LIMPEZA_VIATURA = [
        (LIMPO, 'Limpo'),
        (ACEITAVEL, 'ACEITAVEL'),
        (SUJO, 'Sujo'),
        (MUITO_SUJO, 'Muito Sujo')
    ]

    matricula = models.CharField(max_length=100, blank=True)
    rotas = models.CharField(max_length=40, choices=ROTAS_POSSIVEIS, default=AVOADOR,)
    data_do_incidente = models.DateField(blank=True)
    tipo_de_infracao = models.CharField(max_length=50, choices=TIPO_INFRACAO, default=ALCOOL,) 
    limpeza_do_carro = models.CharField(max_length=20, choices=LIMPEZA_VIATURA, default=LIMPO,)
    observacoes = models.CharField(max_length=300)

    def __str__(self):
        return self.matricula

