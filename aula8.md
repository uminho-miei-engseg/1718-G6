# Aula 8

#### P1.1
Através de https://informationisbeautiful.net/visualizations/million-lines-of-code/, seguem-se as linhas de código de cada software:
1. Linux 3.1 - 15 milhões
2. Facebook - 61 milhões
3. Software automóveis - 100 milhões
4. Google - 2 mil milhões

**1-** Através dos números anteriores, determinamos os limites (inferior e superior) de bugs para cada tipo de software. Os cálculos sustentam-se na seguinte afirmação *"Estima-se que qualquer pacote de software tem uma média de 5 a 50 bugs por cada 1000 SLOC"*, retirada dos apontamentos teóricos.
1. Linux 3.1 - 75000 a 750000 bugs
2. Facebook - 305000 a 3050000 bugs
3. Software de automóveis - 500000 a 5000000 bugs
4. Google - 10 a 100 milhões de bugs

**2-** De uma forma genérica, um bug é um erro/falha num programa que introduz resultados inesperados no seu funcionamento. Independentemente do contexto no qual está inserido, um bug tem uma relação muito forte com o número de linhas de código produzido (embora o número de erros por linhas de código dependa do contexto, daí os limites inferior e superior). Por este motivo, enquanto a relação **SLOC/bugs** é suficientemente forte para nos permitir calcular as estimativas anteriores, no caso **bugs/vulnerabilidades** essa relação é fraca (https://ieeexplore.ieee.org/document/7180086/). Esta fraca relação é reforçada através da resposta (no artigo anterior) à pergunta *Do the source code files with the most bugs also
have the most vulnerabilities?*, que mostrou que os ficheiros com maior número de bugs originaram poucas vulnerabilidades. Estas dependem do contexto, ou seja, das políticas de segurança adotadas. O mesmo tipo de bug pode originar uma vulnerabilidade num sistema, mas não apresentar qualquer tipo de ameaça às política de segurança impostas noutro.

#### P1.2


#### P1.3

As principais diferenças entre vulnerabilidades dia-zero de outro tipo de vulnerabilidades de codificação é o facto de estas, ao contrário da norma que "exige" a sua divulgação pública de forma a que o fornecedor possa corrigir essas falhas, estas são conhecidas apenas a um grupo restrito de pessoas que tem normalmente como objetivo fazer ataques a esse software. Usualmente inserem-se em dois tipos de meios, podendo haver mais, são eles o meio das vendas na dark web por exemplo, ou no meio militar de um país (ciberarmas).

Outra diferença óbvia centra-se claro no próprio nome, uma vulnerabilidade denomina-se de dia-zero por ter sido descoberta nesse dia, enquanto que uma vulnerabilidade que tenha sido descoberta há 30 dias, chamaria-se de dia-trinta. 

Um exemplo de um ataque dia-zero que ocorreu no Java da Oracle, permitia aceder remotamente sem a necessidade de se autenticar com o seu username e password. Isto fez com que, por exemplo, esta vulnerabilidade recebesse o maior valor possível na escala de impacto da Oracle.
