  """
# 1. Faça um programa que leia um número inteiro e o imprima

numero = int(input("Digite um numero inteiro: "))
print(numero)

# 2. Faça um programa que leia um número Real e o imprima.

numero = float(input("Digite um numero real:"))
print(numero)

# 3. Peça ao utilizador para digitar três valores inteiros e imprima a soma deles.

numero1 = int(input('Digite um números inteiro: '))
numero2 = int(input('Digite um números inteiro: '))
numero3 = int(input('Digite um números inteiro: '))
print(f'A soma dos numeros é: {numero1 + numero2 + numero3}')

# 4. Leia um número real e imprima o resultado do quadrado desse número.

numero = 11.34
print(f'O quadrado de {numero} é {numero ** 2}')

# 5. leia um número real e imprima a quinta parte desse numero.

numero = 122.54323
print(f'A quinta parte de {numero} é {numero/5}')

# 6. Leia uma temperatura em graus Celsius e apresente-a convertida em graus fahrenheit.
# A formula de conversão é: F = C*(9.0/5.0)+32.0, sendo c a temperatura em Fahrenheit e C
# a temperatura em Celsius.

C = 19.4
F = C*(9.0/5.0)+32.0
print(F)

# 7. Leia uma temperatura em graus fahrenheit e aprente-a convertida em graus Celsius
# a formula de conversão é: C = 5.0*(F - 32.0)/9, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit

F = 0
C = 5.0*(F - 32.0)/9
print(C)

# 8. Leia uma temperatura em Graus Kelvin e apresente-a convertida em graus Celsius.
# a formula de conversão é: C = K - 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin

K = 312
C = K - 273.15
print(C)

# 9. Leia uma temperatura em Graus Celsius e apresente-a convertida em graus Kelvin.
# a formula de conversão é: K = C + 273.15, sendo C a temperatura em Celsius e K a temperatura em Kevin

C = 18.3
K = C + 273.15
print(K)

# 10. leia uma velocidade em mk/h e apresente-a convertida em m/s. a formula é: M = K/3.6

K = 299
M = 299/3.6
print(M)

# 11. leia uma velocidade em m/s e apresente-a convertida em k. a formula é: K = M*3.6

M = 100
K = M*3.6
print(K)

# 12. Leia uma distancia em Milhas e apresente-a convertida em quilômetros. A formula de conversão é
# K = 1,61* M

M = 500
K = 1.61*M
print(K)

# 13. Leia uma distancia em quilômetros e apresente-a convertida em Milhas. A formula de conversão é
# M = K/1,61

K = 2000
M = K/1.61
print(M)

# 14. Leia um Ângulo em Graus e apresente-o convertido em Radiano. A formula de conversão é
# R = G*180/π

G = 92
π = 3.14
R = G*π/180
print(R)

# 15. Leia um ângulo em Radiano e apresente-o convertido em Graus. a Formula de conversão é
# G = R*180/π

R = 0.25
π = 3.14
G = R*180/π
print(G)

# 16. Leia um comprimento em polegadas e apresente-o em centímetros.
# A formula para conversão é C = P *2.54

P = 16
C = P*2.54
print(C)

# 17. Leia um comprimento em Centímetros e apresente-o em polegadas.
# A formula para conversão é P = C/2.54

C = 250
P = C/2.54
print(P)

# 18. Leia um valor em Metros cúbicos M³ e apresente-o convertido em litros
# A formula de conversaõ é L = 1000*M

M = 30
L = 1000*M
print(L)

# 19. Leia um valor em litros e apresente-o convertido em Metros cúbicos M³
# A formula de conversaõ é M³ = L/1000

L = 143857
M = L/1000
print(M)

# 20. Leia um valor de massa em quilogramas e apresente-o convertido em libras
# A formula de conversão é: L = k/0.45

K = 66
L = K/0.45
print(L)

# 21. Leia um valor de massa em Libras e apresente-o convertido em Quilogramas
# A formula de conversão é: K = L*0.45

L = 45
K = L*.045
print(K)

# 22. leia um valor de comprimento em jardas e apresente-o convertido em metros
# A formula de conversão é M = 0.91*J

J = 18
M = 0.91*J
print(M)

# 23. Leia um valor de comprimento em Metros e apresente convertido em Jardas
# A formula de conversão é J = M/0.91

M = 1200
J = M/0.91
print(J)

# 24. Leia um valor de área em Metros quadrados M² e apresente-o convertido em Acres
# A fórmula de conversar é A = M*0.000247

M = 489
A = M*0.000247
print(A)

# 25. Leia um valor de área em Acres e apresente-o convertido em M²
# A fórmula de conversão é M = A/0.000247

A = 292
M = A/0.000247
print(M)

# 26. Leia um valor de área em metros quadrados e apresente-o convertido em hectares
# A formula de conversão é: H = M*0.0001

M = 123000
H = M*0.0001
print(H)

# 27. Leia um valor de área em hectares e apresente-o convertido em metros quadrados
# A formula de conversão é: M = H*10000

H = 16.8
M = H*10000
print(M)

# 28. Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos valores lidos

num1 = 34
num2 = 85
num3= 12
print((num1**2) + (num2**2) + (num3**2))

# 29. Leia quatro notas, calcule a média aritmética e imprima o resultado

nota1 = 9.6
nota2 = 4
nota3 = 7.4
nota4 = 9.2
media = (nota1 + nota2 + nota3 + nota4) / 4
print(media)

# 30. Leia um valor em real e a cotação do dolar. Em seguida imprima o valor correspondente em dólares

Real = float(input('Valor em Reais:'))
Dolar = 5.16
print(f'O valor em dólares de R$ {Real} é de US$ {Real*Dolar}')

# 31. Leia um número inteiro e imprima seu antecessor e seu sucessor

num1 = int(input('Digite o número'))
print(f'O antecessor de {num1} é {num1-1} e o sucessor é {num1+1}')

# 32. Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro

num = int(input('Digite um numero inteiro:'))
print(f'A soma do sucessor do triplo de {num} com o antecessor do seu dobro é:'
      f'{(num*3-1)+(num*2-1)}')

# 33. Leia o tamanho do lado de um quadrado e imprima como resultado a sua área

lquadrado = int(input('Digite o tamanho de um dos lados de um quadrado em centímetros:'))
print(f'A área de um quadrado de {lquadrado} centímetros de lado é de {lquadrado**2} centímetros quadrados.')

# 34. Leia o valor do raio de um circulo e calcule e imprima a área do circulo correspondente
# A area do circulo é π * reaio², considere π= 3.141592

raio = int(input('Digite o raio do circulo em centimetros:'))
π = 3.141592
print(f'A área de um círculo de {raio} centímetros de raio é de: {π*(raio**2)}')

# 35. Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
# hipotenusa =  √a²+b². Faça um programa que receba os valores de a e b e calcule o valor
# da hipotenusa através da equação. imprima o resultado dessa operação

import math
print('Vamos calcular a hipotenusa de um triângulo')
a = int(input('Digite o valor do primeiro cateto'))
b = int(input('Digite o valor do segundo cateto'))
h = math.sqrt(a**2 + b**2)
print(f'A hipotenusa de um triângulo de catetos {a} e {b} é: {h}')

# 36. Leia a altura e o raio de um curlindro circular e imprima o volume do cilindro
# O volume de um cilindro circular é calculado por meio da segunte formula
# V = π*raio²*altura, onde π = 3.141592

π = 3.141592
raio = int(input('Defina o raio do cilindro'))
altura = int(input('Defina a altura do cilindro'))
volume = π*raio**2*altura
print(f'O volume do cilindro é de {volume}')

"""