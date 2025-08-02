def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    
    return num1 / num2
    
print("Escolha uma operação:")
print("1. Somar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

while True:
    escolha = input("Digite sua escolha (1/2/3/4): ")

    if escolha in ('1', '2', '3', '4'):
        try:
            
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Digite um número.")
            continue 

        if escolha == '1':
            print(f"{num1} + {num2} = {somar(num1, num2)}")
        elif escolha == '2':
            print(f"{num1} - {num2} = {subtrair(num1, num2)}")
        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif escolha == '4':
            
            try:
                print(f"{num1} / {num2} = {dividir(num1, num2)}")
            except ZeroDivisionError:
                print("Erro: Não é possível dividir por zero.")
                
        continuar = input("Realizar outro cálculo? (sim/nao): ").lower()
        if continuar == 'nao':
            break
    else:
        
        print("Escolha inválida.")