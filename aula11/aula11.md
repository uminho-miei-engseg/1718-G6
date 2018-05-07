## Aula 11

### Pergunta P1.1

### Pergunta P1.2


1. A vulnerabilidade desta função está relacionada com o tamanho passado como argumento, uma vez que na função, apesar de se garantir que o intervalo do valor tamanho é entre 0 e MAX_SIZE, prevenindo a alocação de grandes quantidades de memória. A variável tamanho_real que é do mesmo tipo que a variável tamanho, pode apresentar valores muito grandes, uma vez que é o resultado da operação (tamanho -1), se o tamanho for igual a 0 verifica-se um undeflow, uma vez que o tipo de dados size_t não tem representação de números negativos.
 
2. Para demostrar a vulnerabilidade só é necessário passar o argumento tamanho com valor 0.

![Figura 1](https://github.com/uminho-miei-engseg/1718-G6/blob/master/aula11/imagens/1-2.PNG "Figura 1")

3. Ao executar o programa é apresentado o erro Segmentation fault. Uma vez que a função malloc não consegue alocar a quantidade de memória pedida, devolvendo NULL como resultado, o comando memcpy vai tentar escrever no variável destino que tem valor NULL, provocando sempre o erro Segmentation fault.


### Pergunta P1.3

1. A vulnerabilidade do programa *erro_sinal.c* consiste na atribuição de uma variável do tipo **size_t** (*tamanho*) a uma variável do tipo **int** (*tamanho_real*). O tipo *size_t* utiliza 8 bytes para representar inteiros positivos, enquanto que o tipo *int* utiliza 4 bytes para representar tanto positivos como negativos. A atribuição ``` tamanho_real = tamanho ``` pode provocar overflow na variável *tamanho_real*, tornando-a negativa e terminando a execução do programa.

2. ![Figura 2](https://github.com/uminho-miei-engseg/1718-G6/blob/master/aula11/imagens/1-3-2.PNG "Figura 2")

3. ![Figura 2](https://github.com/uminho-miei-engseg/1718-G6/blob/master/aula11/imagens/1-3-1.PNG "Figura 3")
