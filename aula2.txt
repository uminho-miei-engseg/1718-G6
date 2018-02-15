1.3) O algoritmo de geração consiste em dois ciclos. O ciclo exterior executa enquanto o segredo a construir não possua o tamanho pretendido (passado como argumento). Dentro deste ciclo é invocada uma função para gerar dados aleatórios, do módulo utils do python. Contudo, inicia-se um segundo ciclo para escolher desses dados aleatórios apenas os caracteres que correspondem a letras (ASCII_letters) ou dígitos (string_digits);


2.1)
A)
	Como a chave privada faz parte dos argumentos do programa, é necessária a sua geração antes da execução. Para isso, utilizamos o comando 'openssl genrsa -aes128 -out mykey.pem 1024', que gerou 'mykey.pem'. Depois foi só executar o comando, no nosso caso 'python createSharedSecret-app.py 7 3 1 mykey.pem'.		Para verificar se 3 partes conseguem recuperar o segredo, criámos primeiro o certificado correspondente à chave privada que foi utilizada para gerar o segredo com o comando 'openssl req -key mykey.pem -new -x509 -days 365 -out cert.pem'. Após este passo, fizemos 'python recoverSecretFromComponents-app.py 3 1 cert.pem'.
	Chave privada e certificado: ...

B) 
	A diferença entre os dois programas encontra-se no número necessário de partes para reconstruir o segredo. Enquanto que no recoverSecretFromAllComponents o segredo só é reconstruído se todos os componentes colocarem corretamente a sua parte, no recoverSecretFromComponents apenas são necessários alguns componentes do número total (quorum). Neste último caso, para qualquer número de componentes igual ao quorum, é possível recuperar o segredo original independentemente da ordem (pela qual inserem a sua parte) ou das componentes envolvidas.
	O exemplo mais comum são situações de trabalho profissional. Exemplos: i) numa empresa de horário fixo deve ser utilizado o AllComponents porque é necessária a validação de todos os envolvidos da empresa. Numa empresa com horários em turnos é preferível apenas o Components, sendo que o valor do quorum neste caso seria o número de funcionários em cada turno e o total seriam todos os funcionários dos vários turnos.

3)
Cifra)
	str = cifra(segredo);
	tag = hmac(key, str);
	send(str:tag);
Decifra)
	recieve(final);
	str,tag = final;
	if (hmac(k, str) == tag)
		decifra(str);
	else
		erro;
