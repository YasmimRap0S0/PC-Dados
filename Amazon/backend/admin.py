from django.contrib import admin
from .models import Cliente, Endereco, Vendedor, Item, Pedido, FormaPagamento

admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(Vendedor)
admin.site.register(Item)
admin.site.register(Pedido)
admin.site.register(FormaPagamento)