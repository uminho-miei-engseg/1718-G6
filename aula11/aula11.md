## Aula 11

### Pergunta P1.1

1. A vulnerabilidade existente na função vulnerável está presente no tipo dos argumentos x e y. Caso sejam passados como argumento, números muito grandes, poderemos ultrapassar o número de bits do size_t fazendo com que sejam convertidos para números menores. Desta forma poderíamos estar então, a escrever em memória não alocada a esta função.

2.
```C
int main() {
	char *matriz;
	vulneravel(matriz, 670000000,690000000, '150');
} 
```

3. Ao executar o programa deparamo-nos com um _segmentation fault_ pois não se consegue alocar a memória pretendida e como tal estaremos a tentar escrever em memória que não foi alocada à função.

### Pergunta P1.2


1. A vulnerabilidade desta função está relacionada com o tamanho passado como argumento, uma vez que na função, apesar de se garantir que o intervalo do valor tamanho é entre 0 e MAX_SIZE, prevenindo a alocação de grandes quantidades de memória. A variável tamanho_real que é do mesmo tipo que a variável tamanho, pode apresentar valores muito grandes, uma vez que é o resultado da operação (tamanho -1), se o tamanho for igual a 0 verifica-se um undeflow, uma vez que o tipo de dados size_t não tem representação de números negativos.
 
2. Para demostrar a vulnerabilidade só é necessário passar o argumento tamanho com valor 0.

![Figura 1](https://github.com/uminho-miei-engseg/1718-G6/blob/master/aula11/imagens/1-2.PNG "Figura 1")

3. Ao executar o programa é apresentado o erro Segmentation fault. Uma vez que a função malloc não consegue alocar a quantidade de memória pedida, devolvendo NULL como resultado, o comando memcpy vai tentar escrever no variável destino que tem valor NULL, provocando sempre o erro Segmentation fault.


### Pergunta P1.3

1. A vulnerabilidade do programa *erro_sinal.c* consiste na atribuição de uma variável do tipo **size_t** (*tamanho*) a uma variável do tipo **int** (*tamanho_real*). O tipo *size_t* utiliza 8 bytes para representar inteiros positivos, enquanto que o tipo *int* utiliza 4 bytes para representar tanto positivos como negativos. A atribuição ``` tamanho_real = tamanho ``` pode provocar overflow na variável *tamanho_real*, tornando-a negativa e terminando a execução do programa.

2. 

![Figura 2](https://github.com/uminho-miei-engseg/1718-G6/blob/master/aula11/imagens/1-3-2.PNG "Figura 2")

3. As funções **malloc** e **memcpy** tratam dos argumentos representativos do tamanho como *size_t*, logo a variável *tamanho_real* não é representada como um número negativo nestas funções. Contudo, esta nova atribuição coloca um valor superior a **2048(MAX_SIZE)** na variável *tamanho_real*. Desta forma, a função **malloc** tenta alocar um número enorme de bytes, provocando erro de *segmentation fault* no programa. Mais especificamente o erro ``` ENOMEM Out of memory. Possibly, the application hit the  RLIMIT_AS  or  RLIMIT_DATA  limit described in getrlimit(2). ``` que mostra que a função não suporta valores tão elevados para alocação de memória.

![Figura 2](https://github.com/uminho-miei-engseg/1718-G6/blob/master/aula11/imagens/1-3-1.PNG "Figura 3")
