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

**Vulnerabilidades de projeto:**

1.	Falta ou falha nos requisitos de autenticação no acesso a funcionalidades ou a dados restritos *(CWE-285: Improper Authorization)*.
Esta vulnerabilidade permite aos utilizadores acesso a funcionalidade e/ou dados que não estão autorizados a usar ou ver. Esta falha pode levar a vários problemas, como por exemplo exposição de informação, negação de serviço, manipulação de dados, comprometendo a confidencialidade, integridade e controlo de acesso do sistema.
De modo a resolver estas vulnerabilidades é necessário voltar a fase de planeamento e reavaliar os requisitos de autenticação e acrescentar os que forem necessários.

2.	Falta ou falha nos requisitos de validação de input *(CWE-20: Improper Input Validation)*.
Neste caso um atacante introduzir um input que o sistema não está preparado para processar, o que pode conduzir a várias situações indesejadas como por exemplo uma alteração no fluxo de controlo, controlo arbitrário de recursos ou a execução de código arbitrário.
A semelhança do caso anterior é necessária voltar a fase de planeamento para reavaliar os requisitos de validação de input e adicionar mais restrições de modo a tornar o sistema mais seguro.

**Vulnerabilidade de codificação:**

1.	Execução com níveis de privilégios desnecessário *(CWE-250: Execution with Unnecessary Privileges)*.
	Quando são usados privilégios extra, como privilégios de administrador, são expostas vulnerabilidade que estavam inacessíveis, uma vez que com privilégios extra o sistema pode desabilitar certas normas de segurança o que permite que vulnerabilidades já existentes sejam alvo de possíveis ataques.
	Para solucionar estes problemas é crucial identificar e isolar os casos em que é estritamente necessário a utilização de privilégios extra, verificando sempre que possível se os privilégios estão de acordo com as operações que vão ser executadas, tentando manter os requisitos mínimos para a execução de cada operação.

2.	Utilização de métodos criptográficos que não atingem os requisitos mínimos de segurança (CWE-261: Weak Cryptography for Passwords).
Ao serem usados métodos criptográficos fracos comprometemos a segurança de todo o sistema. É também importante ter em conta a validade dos métodos, uma vez que estes pode tornar-se obsoletos com o passar do tempo, devido ao avanço tecnológico e a possíveis descoberta de vulnerabilidades.
Assim sendo é essencial verificar se os métodos garantem os requisitos mínimos de segurança e efetuar as atualizações necessárias para garantir esses mesmos requisitos.

**Vulnerabilidades operacionais:**

1.	Guardar as palavras chave sem serem cifradas (CWE-13: ASP.NET Misconfiguration: Password in Configuration File).
Esta vulnerabilidade é encontrada com mais frequência em ficheiros de configuração, mas aplica-se a todos os casos que impliquem a gravação de palavras chave sem encriptação. Consequentemente, possibilita o acesso a determinados dados ou funcionalidade a qualquer entidade que tenha acesso ao ficheiro de configuração.
De modo a resolver este problema é necessário cifrar qualquer palavra chave antes de ser gravada em ficheiros.

2.	Acesso a conjunto de ficheiros confidenciais (CWE-548: Information Exposure Through Directory Listing).
Esta vulnerabilidade possibilita o acesso a dados sensíveis, sendo que um atacante pode explorar esta falha e obter dados importantes ou alterar os mesmos.
Para evitar estas vulnerabilidades é necessário garantir restrições de acesso a estes ficheiros.



#### P1.3

As principais diferenças entre vulnerabilidades dia-zero de outro tipo de vulnerabilidades de codificação é o facto de estas, ao contrário da norma que "exige" a sua divulgação pública de forma a que o fornecedor possa corrigir essas falhas, estas são conhecidas apenas a um grupo restrito de pessoas que tem normalmente como objetivo fazer ataques a esse software. Usualmente inserem-se em dois tipos de meios, podendo haver mais, são eles o meio das vendas na dark web por exemplo, ou no meio militar de um país (ciberarmas).

Outra diferença óbvia centra-se claro no próprio nome, uma vulnerabilidade denomina-se de dia-zero por ter sido descoberta nesse dia, enquanto que uma vulnerabilidade que tenha sido descoberta há 30 dias, chamaria-se de dia-trinta. 

Um exemplo de um ataque dia-zero que ocorreu no Java da Oracle, permitia aceder remotamente sem a necessidade de se autenticar com o seu username e password. Isto fez com que, por exemplo, esta vulnerabilidade recebesse o maior valor possível na escala de impacto da Oracle.
