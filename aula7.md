# ISO 27552 - 6.9 (Operations Security)

#### 6.9.1

#### 6.9.2

#### 6.9.3 - Event logging
Este ponto introduz a necessidade de registar eventos aquando do acesso, modificação ou alteração de alguma informação pessoal (**PII**) através da monitorização e/ou geração de alertas. Dependendo do contexto, este processo pode ser automático ou manual, sendo possível saber a entidade responsável por tais ações. Refere-se também que cabe às organizações decidir quando as **PII** podem ser acedidas pelo cliente, devendo essa informação ser transmitida aos mesmos. Nenhuma informação de outro cliente que não o próprio deve ser disponibilizada.


#### 6.9.4 Protection of log information

Este sub-ponto acaba por ser um complemento a tudo o que foi referido anteriormente. Este diz respeito à informação dos acessos realizados no software. 
Como sabemos, a maioria do software existente hoje em dia terá sempre que ter *log information* tanto para fazer a monitorização do sistema, para garantir a sua segurança, assim como para efetuar diagnósticos à *boa saúde* do sistema.
Este tipo de informações contém por vezes dados sensíveis dos utilizadores, entre outros, e como tal é também necessário que estes dados sejam apenas utilizados para o propósito a que se proposeram.
Como referido na norma o ideal será que estes dados sejam, através de um procedimento automático, apagados ou anonimizados ao fim de um certo período de tempo.

#### Conclusão 
Do ponto de vista do desenvolvimento de software, os três últimos pontos acrescentam complexidade. Isto porque começa a ser necessário o acréscimo de mecanismos/funcionalidades para permitir à organização - que utiliza o software - manipular os seus dados. Por outras palavras, o controlo de quem acede e a que tipo de informação acede é efetuado pela organização através dos mecanismos que o software disponibiliza.
Pelo termo *operação do software*, entendemos a forma como o software produzido pode ser utilizado. Normalmente a entidade responsável pela operação do software é a organização que o adquire. Por esse motivo, a organização tem o controlo das permissões sobre os dados que armazena (gerados por si ou pelos clientes) e pode utilizar os mecanismos disponibilizados pelo software adquirido para qualquer tipo de ação sobre esses dados. Por isso, apesar de 
