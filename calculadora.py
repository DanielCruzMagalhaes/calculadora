# Crie uma calculadora que faça  1- operações de soma,subtração,divisão,mutiplicação e exponenciação
# A função deve receber dois numeros e as operações que serão realizadas. 
print('\t---- Calculadora ----')


def  calculadora(n1:float,op:str, n2:float):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        return n1/n2
    else:
        return("Você não escolheu uma operação válida")
    

n1 = float(input('Digite o primeiro número:'))
op = input('Digite a operação:')
n2 = float(input('Digite o segundo número:'))
    
calculate = calculadora(n1,op,n2)
print(calculate)
