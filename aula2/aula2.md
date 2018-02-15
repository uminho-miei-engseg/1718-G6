## Aula 2

### Questão 1

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
etiqueta = hmac(HMAC_SHA_256_key, segredo);
send(segredo:etiqueta);
```
##### Decifrar
```
recieve(cifrado);
etiqueta, mensage_cifrada = separa(cifrado) // separa através do tamanho fixo do HMAC_256
if (hmac(HMAC_SHA_256, mensagem_cifrada) == etiqueta)
	decifra(mensagem_cifrada, chave_cifra);
else
	erro;
```
