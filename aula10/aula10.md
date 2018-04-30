## Aula 10

### Pergunta P1.1
No caso dos programas escritos em java e python, quando a capacidade máxima do array é ultrapassada e o programa tenta aceder a posição seguinte este lança uma exceção indicando que a posição que tentou aceder não pertence ao array. No caso do programa escrito em C++, quando a capacidade máxima do array é ultrapassada este continua a funcionar até encontrar uma posição de memória que não pertença ao programa, neste caso a execução é imediatamente parada devolvendo segmentation fault, é possível que as variáveis definidas antes do array sejam reescritas.

### Pergunta P1.2
À semelhança da questão anterior, nas linguagens java e python quando tentamos aceder a uma posição de memória que não pertença ao array o programa lança uma exceção. No caso do C++ é possível aceder a outras posições de memória, verificando-se na escrita dos valores no array e no final, na leitura.

### Pergunta P1.3

### Pergunta P1.4

Apesar de a função *fgets* ser uma versão estável da função *gets*, que não lê mais do que o número passado como argumento (*sizeof buffer* - 100 caracteres), a conversão do valor de retorno (p - *char \* *) para inteiro através da função *atoi* não é segura. Apesar de a função *fgets* limitar a quantidade de caracteres que é possível inserir no buffer (neste caso 100 caracteres), a conversão para valores maiores de 100 produz um buffer overflow.

![](http://github.com/uminho-miei-engseg/1718-G6/edit/master/aula10/images/1-4.png)


### Pergunta P1.5

![alt text](http://github.com/uminho-miei-engseg/1718-G6/edit/master/aula10/images/1-5.png)


### Pergunta P1.6

![alt text](http://github.com/uminho-miei-engseg/1718-G6/edit/master/aula10/images/1-6.png)

### Pergunta P1.7

![alt text](http://github.com/uminho-miei-engseg/1718-G6/edit/master/aula10/images/1-7.png)
