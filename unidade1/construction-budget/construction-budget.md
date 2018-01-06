# Orçamento Construção

Para ajudar com o orçamento da construção da casa dos seus pais, Ricardo criou o programa Python abaixo que contabiliza
a quantidade de tijolos necessária para erguer uma casa com 3 metros de altura e 120 metros de comprimento, considerando
a medida de todas as paredes enfileiradas e cada tijolo com 30cm de largura e 20cm de altura.

```
num_tijolos_altura = 3 / 0.2
num_tijolos_largura = 120 / 0.3
num_tijolos_total = num_tijolos_altura * num_tijolos_largura
print 'O número total de tijolos é' + str(num_tijolos_total)
```

No entanto, ao tentar ajudar outros amigos, Ricardo sentiu a necessidade de sempre reescrever o código para atender a
diferentes tamanhos de parede e tijolos. Além disso, o programa atual não mostra o valor total do investimento,
considerando o preço do tijolo.

Aperfeiçoe o programa de Ricardo para que ele leia diferentes tamanhos de parede e tijolos, assim como o preço da 
unidade do tijolo e escreva na tela a quantidade de tijolos necessária e o valor do orçamento final, sem a necessidade
de reescrita do código.

## Entrada

O programa deverá ler cinco números maiores que zero, referentes ao preço da unidade do tijolo, à altura e comprimento
das paredes e à altura e comprimento dos tijolos.

## Saída

O programa deverá imprimir uma mensagem contendo: a quantidade de tijolos necessária e o valor do orçamento da obra.

## Exemplo de execução

A listagem abaixo demonstra o funcionamento correto do programa.

```
$ python buildingBudget.py
Digite o preço da unidade do tijolo (Em reais): 0.45
Digite a altura do tijolo (Em metros): 0.20
Digite o comprimento do tijolo (Em metros): 0.30
Digite a altura das paredes (Em metros): 3
Digite o comprimento das paredes (Em metros): 120
O número total de tijolos é 6000.0 e o orçamento final é de R$ 2700.0
$ _
```