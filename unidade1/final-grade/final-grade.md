# Nota na Final
Um estudante da UFCG, preocupado com seu andamento nas disciplinas, deseja saber que notas precisa tirar nas provas 
finais, para ser aprovado. Para isso, tentou escrever um pequeno programa que deveria ler da entrada as três notas das 
unidades, seus respectivos pesos e imprimir na saída a média parcial, bem como as notas que precisará tirar na final 
para: 1) ser aprovado na disciplina, o que equivale a ficar com média final maior ou igual a 5,0 (cinco); e 2) para ser 
aprovado e ficar com média final 7,0 (sete).

Por ser apenas aprendiz em python, o programa que ele fez, contudo, não funcionou como ele esperava. Pede-se que você 
escreva um programa funcione como esperado pelos testes.

## Como as notas são calculadas
Para calcular a nota necessária na final é preciso multiplicar a média parcial por 0,6 (seis décimos), subtrair esse 
valor da média final desejada e dividir o resultado por 0,4 (quatro décimos). A média final desejada é a média com que o
aluno ficará se obtiver aquela nota na prova final.

A média parcial, por sua vez, é calculada simplesmente pela média ponderada das três notas. Os pesos, que serão 
digitados na entrada como números decimais entre 0 e 1, representam as percentagens de cada unidade no cálculo da média
parcial.

## Exemplo de cálculo de notas
Por exemplo, suponha que uma disciplina tem pesos 10%, 30% e 60% para as três unidades. E que o aluno obteve notas 6,0
(seis), 5,0 (cinco) e 7,0 (sete), respectivamente. Sua média parcial será obtida, portanto, multiplicando 0,1 por 6,0,
somando isso a 0,3 vezes 5,0, e ainda a 0,6 vezes 7,0. Isso dá uma média parcial de 6,3 (seis vírgula três).

Nesse caso, para saber a nota mínima que o aluno precisará para passar na final, deverá multiplicar 6,3 por 0,6, 
subtrair esse valor de 5,0 e dividir tudo por 0,4. Fazendo os cálculos, obtém-se que a nota mínima que o aluno deve 
obter na final, para passar na disciplina é 3,0 (três). Cálculo semelhante pode ser feito para concluir que, para ficar
com média final maior ou igual a 7,0, o aluno precisaria tirar nota 8,0 na prova final.

## Exemplo de Execução
A listagem abaixo demonstra como o estudante deseja que o programa funcione quando estiver corretamente codificado. 
Observe que os números depois das interrogações dos prompts são os dados digitados pelo usuário. O restante do texto é 
produzido pelo programa. Veja que se trata do mesmo exemplo dado acima.

```
$ python final.py
== Estágio 1 ==
Peso? 0.1
Nota? 6.0
== Estágio 2 ==
Peso? 0.3
Nota? 5.0
== Estágio 3 ==
Peso? 0.6
Nota? 7.0
== Resultados ==
Média parcial: 6.3
Nota na final, pra média 5.0 = 3.0
Nota na final, pra média 7.0 = 8.0
$ _`
```