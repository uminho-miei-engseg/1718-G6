## Aula 2

### Questão 1

#### 1.1
Na execução do primeiro comando  ```head -c 1024 /dev/random | openssl enc -base64```, é necessário criar entropia de forma a que sejam gerados os 1024 bytes pseudoaleatórios. Esta entropia baseia-se em eventos, como por exemplo, o mover do cursor. No segundo comando ```head -c 1024 /dev/urandom | openssl enc -base64```, já não é necessário criar entropia pois a aplicação *urandom* utiliza uma pool interna para produzir mais bits pseudoaleatórios.

#### 1.2
A execução dos dois comandos é similar. A única diferença é que o programa *random* já não necessita de eventos maiores de entropia, como por exemplo o mover do cursor. Este efeito é conseguido com recurso aos efeitos indiretos de eventos no hardware (estados escondidos do processador - caches, branch predictors, memory translation tables, etc).

#### 1.3
Para responder à questão é melhor proceder à explicação do comportamento da função de geração. Assim, o algoritmo consiste em dois ciclos. O ciclo exterior executa enquanto que o segredo a construir não possua o tamanho pretendido (passado como argumento). Dentro deste ciclo é invocada uma função para gerar dados aleatórios, do módulo *utils* do *python*. Contudo, inicia-se um segundo ciclo para escolher, desses dados aleatórios, apenas os caracteres que correspondem a letras (*ASCII_letters*) ou a dígitos (*string_digits*).

### Questão 2

#### 2.1

##### A
Como a chave privada faz parte dos argumentos do programa, é necessária a sua geração antes da execução. Para isso, utilizamos o comando ```openssl genrsa -aes128 -out mykey.pem 1024```, que gerou a chave com nome e formato ```mykey.pem```. Depois foi só executar o comando, no nosso caso ```python createSharedSecret-app.py 7 3 1 mykey.pem```.
Para verificar se as 3 partes conseguem recuperar o segredo original, criámos primeiro o certificado correspondente à chave privada (que foi utilizada para gerar o segredo) com o comando ```openssl req -key mykey.pem -new -x509 -days 365 -out cert.pem```. Após este passo, executamos o comando ```python recoverSecretFromComponents-app.py 3 1 cert.pem```.

##### B
A diferença entre os dois programas encontra-se no número necessário de partes para reconstruir o segredo. Enquanto que no *recoverSecretFromAllComponents* o segredo só é reconstruído se todos os componentes colocarem corretamente a sua parte, no *recoverSecretFromComponents* apenas são necessários alguns componentes do número total (*quorum*). Neste último caso, para qualquer número de componentes igual ao *quorum*, é possível recuperar o segredo original independentemente da ordem (pela qual inserem a sua parte) ou das componentes envolvidas.
O exemplo mais ilustrativo aplica-se nas situações de trabalho profissional.
- Numa empresa de horário fixo deve ser utilizado o *AllComponents* porque é necessária a validação de todos os envolvidos da empresa.
- Numa empresa com horários em turnos é preferível apenas o *Components*, sendo que o valor do *quorum* neste caso seria o número de funcionários em cada turno e o total seriam todos os funcionários dos vários turnos.

### Questão 3
##### Cifrar
```
segredo = cifra(mensagem, chave_cifra); // chave privada dia.mes.ano
etiqueta = HMAC_SHA256(mac_key, segredo);
send(etiqueta:segredo);
```
##### Decifrar
```
recieve(cifrado);
etiqueta, mensage_cifrada = separa(cifrado) // separa através do tamanho fixo do HMAC_256
if (HMAC_SHA256(mac_key, mensagem_cifrada) == etiqueta)
	decifra(mensagem_cifrada, chave_cifra);
else
	erro;
```

### Questão 4
Das três entidades de certificação de confiança da Lituânia que disponibilizam serviços de “QCert for ESig”, duas destas usam o algoritmo SHA256 (função de hash criptográfica) para assinar digitalmente o conteúdo dos certificados e o algoritmo de chave pública RSA com chaves de 2048 bits (normalmente é utilizado numa fase de handshake para atribuir uma chave de sessão para um algoritmo de chave simétrica). 

- ADIC_Qualified certificates for electronic signature-2 (ADIC CA-A)
- SSC_Qualified certificates for electronic signature-6 (SSC GDL VS Class 2-4 QCA)

Para estes casos a segurança fornecida pelos algoritmos é a recomendada atualmente.

A terceira entidade, usa oo algoritmos SHA1 e RSA com chaves de 2048 bits.

- RC_Qualified certificates for electronic signature-5

Neste caso, o algoritmo utilizado atualmente para a assinatura (SHA1) já não é considerado seguro pela BSI (Alemanha), sendo aconselhado no mínimo o SHA256.



