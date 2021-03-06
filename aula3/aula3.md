## Aula 3

### Questão 2

#### 2.2
Os sites para o departamento do Tesouro assim como o departamento da Defesa apresentam um *rating*, segundo o ```SSL Server Test```, de A. Na realidade este rating representa que na realidade ambos os sites são bastante seguros. 
Analisando os detalhes do protocolo utilizado, observamos que as vulnerabilidades mais conhecidas de implementação como o ```Heartbleed```, ```TicketBleed```, ```ROBOT```, assim como no ```OpenSSL```, etc. estão resolvidas e como tal não oferecem qualquer tipo de ameaça a este tipo de protocolo. 
Outros fatores importantes que contribuem para que seja garantida a segurança deste servidor é por exemplo garantir a *Forward Secrecy*, apesar de apenas acontecer em *browsers* recentes. No entanto é um pormenor diminuto, pois hoje em dia todos os *browsers* utilizados incluem-se nessa categoria. 
Também apresenta segurança face a ataques de Downgrade attack, através do uso do TLS_FALLBACK_SCSV, não permitindo que um atacante possa passar de um modo de operação de muita qualidade (por exemplo conexão encriptada) para um modo mais fraco (por exemplo texto limpo).
Apresenta também Secure Renegotiation, assim como OCSP Stapling o que permite verificar o estado de revogação dos certificados que sejam apresentados ao servidor.
	
#### 2.3
Neste caso como este servidor não suporta SSL 3, não existe a possibilidade de de sofrer um ataque *man-in-the-middle* e como tal não existe a possibilidade de serem decifrados *bytes* das mensagens encriptadas.

### Questão 3

#### 3.1
Os servidores *ssh* que escolhemos, de empresas comerciais em Lisboa, forma ```cb.com.pt``` e ```gropius.dessau.pt```.
Os testes efectuados com a ferramenta *ssh-audit* são apresentados a seguir.

![Screenshot1](https://github.com/uminho-miei-engseg/1718-G6/tree/master/aula3/Pergunta3/cb.com.pt.PNG)

![Screenshot2](https://github.com/uminho-miei-engseg/1718-G6/tree/master/aula3/Pergunta3/gropius.dessau.pt.PNG)

#### 3.2
Como podemos observar o servidor *ssh* do site gropius.dessau.pt usa um software mais recente, o ```OpenSSH-7.2p2```.
Enquanto que o site cb.com.pt usa o ```OpenSSH-5.3```.

#### 3.3
A versão ```5.3``` apresenta mais vulnerabilidades conhecidas, uma vez que está tem 10 e a versão ```7.2p2``` tem 6.

#### 3.4
As vulnerabilidades mais graves, de acordo com o rank CVSS, são da versão ```7.2p2``` com uma pontuação de 7.8. Ambas as vulnerabilidades permitem um ataque de *DoS* ao servidor *ssh*. A vulnerabilidade descoberta mais recentemente (CVE-2016-8858) permite que um atacante estabeleça várias conexões com o servidor sem restrições, implicando uma alocação de memória por cada conexão, sendo possível ocupar a memória total do servidor.
A segunda vulnerabilidade (CVE-2016-6515) esta relacionada com a função de autenticação da palavra-chave, a função *auth_password*, esta não define um limite para o comprimento da palavra-chave que vai processar, sendo possível causar um *DoS* pela utilização excessiva do CPU.

#### 3.5
São graves, uma vez que se não houver restrições de modo a controlar a quantidade de recursos usados por cada utilizador do serviço corremos o risco de ter um ataque de *DoS*.
