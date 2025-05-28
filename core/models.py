from django.db import models

# Mesmo que as tabelas já estejam criadas no mysql, para haver interação com o db deve-se especificar as tabelas e seus valores na classe
class Location(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)  # Data de criação
    update = models.DateTimeField(auto_now=True)  # Última atualização
    
    class Meta:
        db_table = 'countries'
        managed = False  # Informa ao Django que não deve tentar gerenciar a tabela
