from django.db import models

class Categoria(models.Model):
    nome = models.CharField(verbose_name='Categoria do Produto', blank=False, null=False, max_length=200)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table  = 'categoria'

    def __str__(self):
            return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(verbose_name='Fornecedor do Produto', blank=False, null=False, max_length=150)
    contato = models.CharField(verbose_name='Contato do Fornecedor', blank=False, null=False, max_length=15)
    cnpj = models.CharField(verbose_name='CNPJ do Fornecedor', blank=False, null=False, max_length=14, unique=True)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        db_table  = 'fornecedor'

    def __str__(self):
        return (f' {self.nome} -  {self.cnpj}')