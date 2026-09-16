preço_burguer = 32.50
preço_batata = 18.00
preço_refri = 8.50
preço_sobremesa = 15.00

print("Calculadora de pedidos")
print("Cardapio:")
print(f"1. Burguer: R$ {preço_burguer:.2f}")
print(f"2. Batata: R$ {preço_batata:.2f}")
print(f"3. Refrigerante: R$ {preço_refri:.2f}")
print(f"4. Sobremesa: R$ {preço_sobremesa:.2f}")

quantidade_burger = int(input("Digite quantos hambúrgueres você deseja: "))
quantidade_batata = int(input("Digite quantas porções de batata você deseja: "))
quantidade_refri = int(input("Digite quantos refrigerantes você deseja: "))
quantidade_sobremesa = int(input("Digite quantas sobremesas você deseja: "))

total_burguer = preço_burguer * quantidade_burger
total_batata = preço_batata * quantidade_batata
total_refri = preço_refri * quantidade_refri
total_sobremesa = preço_sobremesa * quantidade_sobremesa

total_pedido = total_burguer + total_batata + total_refri + total_sobremesa
print(f"Total do pedido: R$ {total_pedido:.2f}")   
taxa_serviço = total_pedido * 0.10
print(f"Taxa de serviço (10%): R$ {taxa_serviço:.2f}")

print()
print("Nota fiscal:")   
print()
print(f"Hambúrgueres: {quantidade_burger} x R$ {preço_burguer:.2f} = R$ {total_burguer:.2f}")
print(f"Batatas: {quantidade_batata} x R$ {preço_batata:.2f} = R$ {total_batata:.2f}")
print(f"Refrigerantes: {quantidade_refri} x R$ {preço_refri:.2f} = R$ {total_refri:.2f}")
print(f"Sobremesas: {quantidade_sobremesa} x R$ {preço_sobremesa:.2f} = R$ {total_sobremesa:.2f}")
print(f"taxa de serviço (10%): R$ {taxa_serviço:.2f}")
print(f"Total do pedido: R$ {total_pedido + taxa_serviço:.2f}")
print()
print("Obrigado por seu pedido! Volte sempre!") 