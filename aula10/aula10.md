## Aula 10

### Pergunta P1.1
No caso dos programas escritos em java e python, quando a capacidade máxima do array é ultrapassada e o programa tenta aceder a posição seguinte este lança uma exceção indicando que a posição que tentou aceder não pertence ao array. No caso do programa escrito em C++, quando a capacidade máxima do array é ultrapassada este continua a funcionar até encontrar uma posição de memória que não pertença ao programa, neste caso a execução é imediatamente parada devolvendo segmentation fault, é possível que as variáveis definidas antes do array sejam reescritas.

### Pergunta P1.2
À semelhança da questão anterior, nas linguagens java e python quando tentamos aceder a uma posição de memória que não pertença ao array o programa lança uma exceção. No caso do C++ é possível aceder a outras posições de memória, verificando-se na escrita dos valores no array e no final, na leitura.

### Pergunta P1.3

### Pergunta P1.4

A vulnerabilidade do código fornecido consiste na falta de verificação do tamanho do input, ou seja, na aplicação da função *atoi* ao valor de retorno da função *fgets*. Apesar de não ser possível a escrita de caracteres fora dos limites do buffer, é possível introduzir um valor grande como input. A próxima figura mostra o caso em que inserimos o valor *9999*, em que **len = atoi(p)** corresponde ao mesmo que **len = atoi(9999)**. Esta atribuição à variável *len* influencia o último ciclo de impressão, permitindo que sejam imprimidos valores para além daqueles delimitados pelo buffer (como por exemplo, variáveis de ambiente).

![Figura 1](https://github.com/uminho-miei-engseg/1718-G6/blob/master/aula10/images/1-4.png )


### Pergunta P1.5

[Alt text](https://github.com/uminho-miei-engseg/1718-G6/blob/master/aula10/images/1-5.png)


### Pergunta P1.6

![alt text](https://github.com/uminho-miei-engseg/1718-G6/blob/master/aula10/images/1-6.png)

### Pergunta P1.7

![alt text](https://github.com/uminho-miei-engseg/1718-G6/blob/master/aula10/images/1-7.png)
