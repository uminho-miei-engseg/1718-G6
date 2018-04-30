## Aula 10

### Pergunta P1.1
No caso dos programas escritos em java e python, quando a capacidade máxima do array é ultrapassada e o programa tenta aceder a posição seguinte este lança uma exceção indicando que a posição que tentou aceder não pertence ao array. No caso do programa escrito em C++, quando a capacidade máxima do array é ultrapassada este continua a funcionar até encontrar uma posição de memória que não pertença ao programa, neste caso a execução é imediatamente parada devolvendo segmentation fault, é possível que as variáveis definidas antes do array sejam reescritas.

### Pergunta P1.2
À semelhança da questão anterior, nas linguagens java e python quando tentamos aceder a uma posição de memória que não pertença ao array o programa lança uma exceção. No caso do C++ é possível aceder a outras posições de memória, verificando-se na escrita dos valores no array e no final, na leitura.

### Pergunta P1.3

### Pergunta P1.4

A vulnerabilidade do código fornecido consiste na falta de verificação do tamanho do input, ou seja, na aplicação da função *atoi* ao valor de retorno da função *fgets* (uma solução passava por verificar se este valor era menor ou igual a 100). Apesar de não ser possível a escrita de caracteres fora dos limites do buffer, é possível introduzir um valor grande como input. Para melhor explicar, consideremos a próxima figura, que ilustra o caso em que inserimos o valor *9999*. Analisando o código, percebemos que isto corresponderia a efetuar **len = atoi(p)**, que é o mesmo que **len = atoi(9999)**. Esta atribuição à variável *len* influencia o último ciclo, permitindo que sejam imprimidos valores para além dos delimitados pelo buffer. Contudo, os valores imprimidos têm um limite que corresponde ao contexto ou ao espaço de endereçamento do programa.

![Figura 1](https://github.com/uminho-miei-engseg/1718-G6/blob/master/aula10/images/1-4.png)


### Pergunta P1.5

![Figura 2](https://github.com/uminho-miei-engseg/1718-G6/blob/master/aula10/images/1-5.png)

A figura anterior ilustra o *exploit* do *buffer overflow*, alterando da variável *control* através da escrita controlada no *buffer*. Neste caso, sabemos que as duas variáveis estão uma a seguir à outra. Como a stack cresce no sentido aposto, o facto de a variável *buffer* ser declarada depois da variável *control* permite que esta última seja atingida pelos caracteres fora do limite da primeira. Por este motivo, recorremos ao *gdb* para obter os endereços das duas variáveis. A subtração das mesmas no site disponibilizado permite obter o *offset* que as separa. Por último, recorremos ao comando de linha do *python* para imprimir o caracter **x** tantas vezes quando o valor do *offset* (**72 vezes**), seguido do valor pretendido para reescrever a variável **control**. A arquitetura representa os dados em *little-endian*, logo é necessário escrever estes últimos 4 bytes pela ordem inversa.


### Pergunta P1.6

![Figura 3](https://github.com/uminho-miei-engseg/1718-G6/blob/master/aula10/images/1-6.png)

Neste exercício o principal objetivo passa por escrever o endereço que aponta para a função *win* no lugar da variável *fp*, novamente através do buffer. Uma diferença é que neste caso precisamos de outra forma para fornecer os caracteres do buffer, uma vez que a função **gets** lê do stdin e os comandos deixam de ser interpretados como tal. Para isso recorremos novamente ao **gdb** para retirar o endereço das duas variáveis e do endereço que aponta para a função *win*. Através do *offset** (novamente 72), escrevemos a letra *a* 72 vezes, seguido de 6 letras. Estas 6 letras foram retiradas de uma tabela ASCII, de modo a corresponderem ao valor hexadecimal do endereço da função *win* (por exemplo, o caracter *U* é interpretado com o valor 55 em hexadecimal).

### Pergunta P1.7

![Figura 4](https://github.com/uminho-miei-engseg/1718-G6/blob/master/aula10/images/1-7.png)

Este exercício segue o mesmo padrão do anterior, com a diferença de que não foi possível encontrar todas as correspondências entre caracteres ASCII e o seu valor hexadecimal. Contudo, este problema foi resolvido através da utilização de um **pipe**, que redireciona o **output** do comando introduzido para o **input** do programa. 
