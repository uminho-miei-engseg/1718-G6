## Aula 11

### 1. Injection

#### Pergunta 1.1 - String SQL Injection

#### Pergunta 1.2 - Numeric SQL Injection

#### Pergunta 1.3 - Database Backdoors

### 2. XSS

#### Pergunta 2.1 - Reflected XSS

### 3. Quebra na Autenticação

#### Pergunta 3.1 - Forgot Password

**1 -** Após a inserção do username **webgoat** e da resposta **red**, conforme indicado no enunciado do problema, foi devolvida a palavra-chave **webgoat**.

**2 -** Alguns exemplos de utilizadores habituais num sistema são: *user, guest, admin, root*. A conta que qualquer atacante gostaria de aceder seria a correspondente ao *admin/root* para possuir privilégios especiais sobre o sistema alvo.

**3 -** Uma vez que não temos nenhuma informação sobre outros utilizadores do sistema, a primeira tentativa foi efetuada sobre o username **admin**. Através de força bruta foi possível acertar na pergunta específica do administrador do sistema, como a seguinte imagem mostra.

![Figura 5](https://github.com/uminho-miei-engseg/1718-G6/blob/master/aula14/imagens/forgot_password.png "Figura 5")
