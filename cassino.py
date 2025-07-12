import random
saldo = 100
print("=" * 20, "Bem-vindo ao cassino fodinha", "=" * 20)
name = input("Insira o nome do jogador: ")
print(f"Olá {name} tudo bem? As regras são: você poderá jogar enquanto tiver dinheiro para apostar, se não você morre")
print(f"Atualmente seu saldo é de R${saldo}")

while saldo > 0:
    jogar = str(input("Você deseja continuar jogando [S/N] ")).strip().upper()
    if jogar != "S":
        print(f"Volte sempre, o jogador {name} ganhou R${saldo - 100} apostando!!!")
        break
    
    valor_aposta = int(input("Quantos reais você deseja apostar?: R$"))
    if valor_aposta > saldo:
        print(f"Burro pra krl irmão, você apostou mais do que tem")
        print(f"O jogador {name} morreu porque é cabaço e apostou mais do que tem")
        break
    
    saldo -= valor_aposta
    print('''
    [1] Adivinha o número (quadriplica o valor)
    [2] JokenPo (triplica o valor)
    [3] Par ou Impar (duplica o valor)
    ''')
    op = int(input("Digite uma das opções acima: "))
    
    if op == 1:
        num_comp = random.randint(1,10)
        num_jogador = int(input("Qual número o computador escolheu entre 1 e 10: "))
        if num_comp == num_jogador:
            print("Você ganhou")
            saldo += valor_aposta * 4
            print(f"Seu saldo é de R${saldo}")
        else:
            print(f"Você perdeu burro pra caralho, o número que havia escolhido era {num_comp}")
            print(f"Seu saldo atual é de {saldo}")
    
    elif op == 2:
        escolha_comp = random.randint(1,3)
        print('''
        [1] Pedra
        [2] Papel
        [3] Tesoura 
        ''')
        escolha_jog = int(input("Escolha uma das opções acima: "))
        
        if escolha_comp == escolha_jog:
            print(f"Empate! O computador escolheu {escolha_comp} e o {name} escolheu {escolha_jog}")
            print(f"Seu saldo atual é de {saldo}")
            saldo += valor_aposta
        elif (escolha_comp == 1 and escolha_jog == 3) or (escolha_comp == 2 and escolha_jog == 1) or (escolha_comp == 3 and escolha_jog == 2):
            print(f"Você perdeu! O computador escolheu {escolha_comp} e o jogador {name} escolheu {escolha_jog}")
            print(f"Seu saldo atual é de {saldo}")
        else:
            print(f"Você ganhou! O computador escolheu {escolha_comp} e o jogador {name} escolheu {escolha_jog}")
            saldo += valor_aposta * 3
            print(f"Seu saldo atual é de {saldo}")
    
    elif op == 3:
        print('''
        [1] Par
        [2] Impar
        ''')   
        par_ou_impar = int(input("Escolha uma das opções acima: "))
        par_ou_impar_num_jog = int(input("Escolha um número de 1 a 100: "))
        par_ou_impar_num_comp = random.randint(1,100)
        soma = par_ou_impar_num_comp + par_ou_impar_num_jog
        definindo = soma % 2
        
        if (par_ou_impar == 1 and definindo == 0) or (par_ou_impar == 2 and definindo != 0):
            print(f"O número é {soma} e você acertou! O jogador {name} ganhou")
            saldo += valor_aposta * 2
            print(f"Seu saldo atual é de {saldo}")
        else:
            print(f"O número é {soma} e você errou! O computador ganhou")
            print(f"Seu saldo atual é de {saldo}")

if saldo <= 0:
    print(f"O jogador {name} morreu pobre")