# Controle de Água

Preocupada com a crise hídrica na cidade de Campina Grande, Carolina, uma estudante de Computação resolve escrever um 
programa Python para controlar o uso da água em sua casa.

```
import math

velocidade_de_vazao = 0.3
seccao = (math.pi * 0.0127**2) / 4
vazao = velocidade_de_vazao * seccao * 1000            #convertendo para litros
tempo = 1800                                           #em segundos
quantidade_de_agua = tempo * vazao
print "Quantidade de água =", quantidade_de_agua, "litros."
```

Sabendo que o valor 0.0127 representa o diâmetro em metros de um cano residencial de 1/2 polegada, melhore a escrita do
programa para que ele seja capaz de ler a velocidade de vazão, o diâmetro do cano e o tempo (em segundos) em que a 
torneira ficará ligada e escreva a quantidade de água utilizada.

## Entrada

O programa deverá ler três números maiores que zero, referentes às unidades de velocidade de vazão (em metros/segundo),
diâmetro do cano (em metros) e o tempo (número inteiro, em segundos).

## Saída
O programa deverá imprimir uma mensagem contendo a quantidade de água (em litros) utilizada. Formatação de string não 
deve ser utilizada nesse exercício.

## Exemplo de execução

A listagem abaixo demonstra o funcionamento correto do programa.

```
$ python controle_agua.py
0.3
0.0127
1800
Quantidade de água = 68.4055096782 litros.
```