## Aula 9

### Pergunta P1.1

No exemplo apresentado o nível maior de risco por norma estará do lado do PC doméstico. No entanto não havendo informações específicas sobre qualquer um dos sistemas, não conseguiremos precisar com certeza absoluta qual dos dois estará mais vulnerável. Recorrendo à fórmula do risco, ``` risco = probabilidade do ataque ter sucesso * impacto ```, sendo que ``` probabilidade do ataque ter sucesso = nível da ameaça * grau da vulnerabilidade ``` , percebemos que o fator mais controlável por um desenvolvedor de software é o grau de vulnerabilidade, dado que os restantes fatores são um pouco variáveis. 
Os fatores mais notórios que influenciam este grau são por exemplo:
- Os mecanismos de controlo aplicados.
- A existência de vulnerabilidades no *design* do projeto.
- O nível de maturidade do *software*.
- A linguagem de programação utilizada.
- Código fechado em comparação com o código aberto.

No que toca á formúla geral do risco tendo em conta os fatores anteriormente referidos, podemos inequivocamente dizer que o maior grau de impacto se encontra no lado do *homebanking* de um Banco, pois podem ser afetados milhares ou mesmo milhões de utilizadores, enquanto que no lado do PC doméstico apenas afetará os utilizadores desse mesmo PC.

### Pergunta P1.2

#### 1.

Dada a descoberta e encarceramento dos cibercriminosos que ameaçavam a aplicação, caso esta vulnerabilidade não tenha sido tornada pública, o nível da ameaça passará a ser 0 nesse momento o que causaria que a probabilidade do ataque ter sucesso passe também a ser 0 e como tal o risco deixará de ser R.

#### 2.

Este cenário causaria uma diminuição no fator do grau de vulnerabilidade, alterando consequentemente a probabilidade do ataque ter sucesso, e por consequência a alteração do fator de risco para um valor diferente de R. Também é importante referir que dependendo das vulnerabilidades que forem resolvidas o impacto poderá também mudar assim como o nível da ameaça pois existem vulnerabilidades mais graves do que outras.

### Pergunta P2

#### 1.
De modo a implementar as normas estabelecidas pelo regulamento europeu RGPD no modelo em cascata, estas têm de ser consideradas na fase de requisitos, de modo a garantir a sua correta aplicação no projeto.

#### 2.
No caso do modelo *Microsoft Security Development Lifecycle*, dependendo da formação dos membros da equipa de desenvolvimento, pode ser necessário ou não introduzir o regulamento na fase de formação. A semelhança do modelo em cascata é necessário identificar os requisitos de segurança necessários para cumprir o regulamento europeu RGPD, assim sendo na fase de requisitos é essencial ter em linha de conta o regulamento.
