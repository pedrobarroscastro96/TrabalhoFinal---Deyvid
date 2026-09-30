def mostrar_cardapio():
    print()
    print("---------------------------------------")
    print("          Lanchonete Perdões")
    print("----------------------------------------")
    print("Código   Produto             Preço")
    print("--------------------------------------")
    print("1        X-Tudo            R$ 18,00")
    print("2        X-Salada            R$ 20,00")
    print("3        X-Bacon             R$ 23,00")
    print("4        Batata Frita        R$ 12,00")
    print("5        Guarapan             R$  7,00")
    print("0        Finalizar pedido")
    print("---------------------------------------")


def escolher_produto():
    codigo = int(input("Digite o código do produto: "))

    if codigo == 1:
        produto = "X-Tudo"
        preco = 18.00

    elif codigo == 2:
        produto = "X-Salada"
        preco = 20.00

    elif codigo == 3:
        produto = "X-Bacon"
        preco = 23.00

    elif codigo == 4:
        produto = "Batata Frita"
        preco = 12.00

    elif codigo == 5:
        produto = "Gurapan"
        preco = 7.00

    else:
        produto = ""
        preco = 0

    return codigo, produto, preco


def calcular_desconto(total):
    if total < 50:
        percentual = 0

    elif total >= 50 and total < 100:
        percentual = 5

    else:
        percentual = 10

    valor_desconto = total * percentual / 100
    valor_final = total - valor_desconto

    return percentual, valor_desconto, valor_final


def escolher_pagamento():
    while True:
        print()
        print("---------- FORMA DE PAGAMENTO ----------")
        print("1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartão")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            return "Dinheiro"

        elif opcao == 2:
            return "PIX"

        elif opcao == 3:
            return "Cartão"

        else:
            print("Opção inválida! Escolha 1, 2 ou 3.")


def mostrar_resumo(nome_cliente, total, percentual,
                   valor_desconto, valor_final, pagamento):

    print()
    print("---------------------------------------")
    print("             RESUMO DO PEDIDO")
    print("---------------------------------------")
    print("Cliente:", nome_cliente)
    print("--------------------------------------")
    print(f"Valor original:  R$ {total:.2f}")
    print(f"Desconto:        {percentual}%")
    print(f"Valor desconto:  R$ {valor_desconto:.2f}")
    print(f"Valor final:     R$ {valor_final:.2f}")
    print(f"Pagamento:       {pagamento}")
    print("---------------------------------------")
    print("       Obrigado pela preferência!")
    print("---------------------------------------")


def main():

    print("---------------------------------------")
    print("          Lanchonete Perdões")
    print("---------------------------------------")

    nome_cliente = input("Digite o nome do cliente: ")

    total = 0
    continuar = True

    while continuar:

        mostrar_cardapio()

        codigo, produto, preco = escolher_produto()

        if codigo == 0:
            continuar = False

        elif codigo >= 1 and codigo <= 5:

            quantidade = int(
                input("Digite a quantidade desejada: ")
            )

            if quantidade > 0:

                subtotal = preco * quantidade

                total = total + subtotal

                print()
                print("Produto:", produto)
                print("Quantidade:", quantidade)
                print(f"Preço unitário: R$ {preco:.2f}")
                print(f"Subtotal: R$ {subtotal:.2f}")
                print(f"Total da compra: R$ {total:.2f}")

            else:
                print("A quantidade deve ser maior que zero.")

        else:
            print("Código inválido! Escolha um código de 0 a 5.")

    if total > 0:

        percentual, valor_desconto, valor_final = calcular_desconto(total)

        pagamento = escolher_pagamento()

        mostrar_resumo(
            nome_cliente,
            total,
            percentual,
            valor_desconto,
            valor_final,
            pagamento
        )

    else:

        print()
        print("Nenhum produto foi adicionado ao pedido.")
        print("Atendimento finalizado.")


if __name__ == "__main__":
    main()