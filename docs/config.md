Explorando o Flask-login

Um dos recursos mais comuns de uma aplicação web é permitir que o usuário faça login. 
Com o pacote flask_login (uma extensão do Flask) é possível realizar autenticação de usuário, gerenciamento de sessões, proteção de rotas entre outras funcionalidades.

- LoginManager:

Essa classe configura e gerencia autenticação de usuário permitindo que os usuários façam login e permaneçam autenticados enquanto navegam pelo aplicativo.

- current_user:

Essa função tem o papel de exibir informações específicas do usuário autenticado em uma página, verificar se um usuário está autenticado antes de permitir o acesso a determinadas rotas ou simplesmente acessar os dados do usuário durante o processamento de uma solicitação;

- @login_required: 

Decoradores de rota usados para proteger rotas específicas;

- Métodos de usuário: is_authenticated, is_active, get_id;

Esses métodos ajudam a determinar o estado e as permissões do usuário durante o processo de autenticação;

- Gerenciamento de sessão:

 O Flask-Login gerencia automaticamente a sessão do usuário, armazenando e recuperando informações de usuário durante o ciclo de vida da sessão. Isso inclui o armazenamento seguro do ID do usuário na sessão do navegador do cliente.

- Logout_user (Recursos de desautenticação): 

O Flask-Login oferece métodos para desautenticar usuários, como logout_user, que podem ser usados para encerrar a sessão do usuário e remover suas informações de autenticação da sessão.

- Integração com Outros Pacotes: 
O Flask-Login se integra bem com outros pacotes Flask, como Flask-SQLAlchemy, Flask-WTF (para formulários), Flask-Mail (para recuperação de senha por e-mail), entre outros.

- Flask-Bcrypt: utilitário Flask integrado para hash de senhas.

Bcrypt: Esta é a classe principal do Flask-Bcrypt. Ela é usada para hashear e verificar senhas. As principais funções fornecidas por esta classe são:

 O 'generate_password_hash' e o 'check_password_hash',  são funções integradas ao pacote Flask-Bcrypt, usado para hash de senhas em aplicativos Flask.

 - generate_password_hash: Esta função é usada para criar um hash seguro de uma senha. Ela aceita a senha como entrada e retorna uma string contendo o hash gerado. O objetivo é armazenar esse hash seguro no banco de dados, em vez da própria senha, para garantir a segurança dos dados do usuário.

 - check_password_hash: Esta função é usada para verificar se uma senha fornecida corresponde ao hash armazenado no banco de dados. Ela aceita o hash armazenado e a senha fornecida como entrada e retorna True se a senha estiver correta e False caso contrário.

- SAL:

Além dessas funções principais, o Flask-Bcrypt também fornece algumas outras funcionalidades úteis, como a capacidade de configurar o prefixo de hash e a geração automática de **sal** para aumentar a segurança dos hashes de senha.

uando você armazena senhas em um banco de dados, é uma prática recomendada não armazená-las diretamente como texto simples. Em vez disso, você deve hashear as senhas antes de armazená-las. O hashing é um processo irreversível que transforma a senha em uma sequência de caracteres aparentemente aleatórios, conhecida como hash. Isso torna as senhas seguras, mesmo se o banco de dados for comprometido, pois é computacionalmente inviável reverter o hash para obter a senha original.

No entanto, apenas hashear as senhas pode não ser suficiente. Isso ocorre porque duas senhas idênticas terão o mesmo hash, o que poderia permitir a identificação de usuários que usam senhas comuns. Para mitigar esse problema, é comum adicionar um "sal" às senhas antes de hasheá-las.

O "sal" é uma sequência aleatória de caracteres que é adicionada à senha antes do hashing. Isso significa que duas senhas idênticas terão hashes diferentes devido à inclusão de sals diferentes. O sal é armazenado junto com o hash da senha no banco de dados.

A geração automática de sal é um recurso em muitas bibliotecas de hash, como o Bcrypt, que gera automaticamente um sal aleatório para cada senha antes de hasheá-la. Isso simplifica o processo para os desenvolvedores, pois eles não precisam gerenciar a geração e o armazenamento de sals separadamente.

Em resumo, a geração automática de sal é uma prática recomendada ao hashear senhas para aumentar a segurança, garantindo que mesmo senhas idênticas tenham hashes diferentes, dificultando a identificação de padrões de senha no banco de dados.

