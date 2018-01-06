# Número de Fatias

Em uma festa foram compradas 32 fatias de pizza. Corrija o programa abaixo que lê da entrada o número de convidados da
festa e apresenta duas formas de dividir as fatias para os convidados, conforme mostrado nos exemplos abaixo. Assuma que
a festa tem pelo menos um convidado.

## Programa original

```
convidados = float(raw_input())
op1_inteira = 32 / convidados
op1_resto  = 32 % convidados
op2 = 32 / convidados
print 'Opção 1: $d fatias cada, 2 de resto' % (op1_inteira,op1_resto)
print 'Opção 2: $d' % op2
```

## Exemplo

```
10
Opção 1: 3 fatias cada, 2 de resto
Opção 2: 3.20 fatias cada
```