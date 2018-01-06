# Área e Volume de uma Esfera

Uma esfera é um sólido geométrico com uma superfície fechada e o cálculo de sua área e volume depende do seu raio. 
O programa abaixo recebe o raio de uma esfera e imprime a área dessa esfera considerando apenas a parte inteira.

```
# coding: utf-8
# Área de uma esfera
import math

raio = float(raw_input())
area = 4 * math.pi * raio ** 2

print '%d' % area
```

Com base no programa fornecido, escreva um novo programa que recebe o raio de uma esfera e calcula e imprime com duas 
casas decimais o volume desta esfera.

## Entrada

No novo programa, o valor do raio é lido da entrada padrão.

## Saída

Na saída, o novo programa deve imprimir em ponto flutuante (2 casas decimais) o valor do volume da esfera.

## Exemplo de Entrada e Saída

```
python solution.py
1
4.19
```