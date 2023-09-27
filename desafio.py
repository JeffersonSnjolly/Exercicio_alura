import os

while True:
    print("=============jogo dos numeros================")
    print("""
          1 - Par/Impar
          2 - Positivo/Negativo
          3 - Inteiro/Decimal
          4 - Ordem correta dos numeros
          5 - Sair da aplicão""")
    print("=============================================")
    op = input("Digite a opação desejada: => ")
    
    if op == "1":
        print("=============Par ou Impar===============")
        num = int(input("Digite qualque numero inteiro: => "))
        if num % 2 == 0:
            print(f"{num} é par!")
            input("Tecle enter para voltar ao menu:")
            os.system("cls")
        else:
            print(f"{num} é impar!")
            input("Tecle enter para voltar ao menu:")
            os.system("cls")
    elif op == "2":
        print("===========Positivo ou Negativo=============")
        num = int(input("Digite qualque numero inteiro: => "))
        if num > 0:
            print(f"{num} é positivo!")
            input("Tecle enter para voltar ao menu:")
            os.system("cls")
        elif num < 0:
            print(f"{num} é negativo!")
            input("Tecle enter para voltar ao menu:")
            os.system("cls")
        else:
            print(f"{num} é neutro")
            input("Tecle enter para voltar ao menu:")
            os.system("cls")
    elif op == "3":
        print("============Inteiro ou Decimal=============")
        num = float(input("Digite qualque numero: => "))
        if (num == round(num)):
            print(f"{int(num)} é inteiro!")
            input("Tecle enter para voltar ao menu:")
            os.system("cls")
        else:
            print(f"{num} é Decimal")
            input("Tecle enter para voltar ao menu:")
            os.system("cls")
    elif op == "4":
        print("==========Ordem correta dos numeros===========")
        print("Digite 3 numeros:")
        num1 = float(input("Digite primeiro numero: => "))
        num2 = float(input("Digite segundo numero: => "))
        num3 = float(input("Digite terceiro numero: => "))
        print(f"Ordem digitada {num1}, {num2}, {num3}")
        if num3 < num2:
            step = num3
            num3 = num2
            num2 = step
        if num2 < num1:
            step = num2
            num2 = num1
            num1 = step
        if num3 < num2:
            step = num3
            num3 = num2
            num2 = step
        print(f"Ordem correta {num1}, {num2}, {num3}")
        input("Tecle enter para voltar ao menu:")
        os.system("cls")
    elif op == "5":
        print("Obrigado!")
        break