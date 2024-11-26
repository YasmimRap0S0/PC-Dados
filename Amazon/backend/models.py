from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_cadastro = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f'{self.nome} - {self.email} - {self.telefone}'
    
class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2) 
    cep = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.rua}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado} - {self.cep}'
    
   

class Item (models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.IntegerField()
    
    def __str__(self):
        return f'{self.nome} - {self.descricao} - R$ {self.preco} - Estoque: {self.estoque}'

class Vendedor(models.Model):
    nome = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

class FormaPagamento(models.Model):
    descricao = models.CharField(max_length=30,
                                 choices=[
                                     ('dinheiro', 'Dinheiro'),
                                     ('cartao_credito', 'Cartão de Crédito'),
                                     ('cartao_debito', 'Cartão de Débito'),
                                     ('pix', 'Pix'),

                                ],
                                null=True, 
                                blank=True
                                  
                                 )

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    endereco_entrega = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    itens = models.ManyToManyField(Item)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateTimeField()
    
    def __str__(self): 
        return f'{self.cliente} - {self.vendedor} - {self.data_pedido}'
    


    
