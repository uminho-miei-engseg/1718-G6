## Aula 4

### Pergunta 1

#### Alínea 1
Executando o comando ``` sudo anonsurf change ``` não podemos garantir que a nossa localização seja os EUA, pois a escolha da mesma depende do TOR. Contudo, existem mecanismos disponíveis para que um utilizador especifique qual o país do último nodo (*Onion Router*).

#### Alínea 2
Analisando o protocolo do TOR, denota-se que este receberá uma lista de nodos TOR de um DS (*directory server*). O cliente que utiliza o TOR, passa então a escolher aleatoriamente uma série de nodos TOR para chegar ao servidor destino.



### Pergunta 2

#### Alínea 1

#### Alínea 2
Como referido no protocolo do TOR, para se poder aceder ao servidor é necessário fazer três saltos já estipulados pelo mesmo, dos quais o cliente não tem conhecimento prévio. Da mesma forma, o cliente para garantir o anonimato terá também de escolher três saltos da lista de saltos possíveis, que lhe foi fornecida pelo directory server. 
