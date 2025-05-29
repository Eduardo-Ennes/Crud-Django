# Crud-Django

Este projeto teve a finalidade de praticar as operações básicas (CRUD). É um projeto simples onde se cadastra um país e uma cidade de destino.

## Funcionalidades
- Criação 
- Atualização
- Leitura
- Exclusão


## Tecnologias 
- Python
- Django
- Django RestFramework
- Mysql


## Instruções para rodar o projeto localmente

### Pré-requisitos
Ter instalado:
- Python
- Mysql
- Pip


### 1°: Instalar o dotenv
```bash
pip install python-dotenv
```
📝 É uma biblioteca que carrega variáveis de ambiente de um arquivo .env para o ambiente do sistema.


### 2°: Criar um ambiente virtual
```bash
python -m venv venv
```
📝 Cria a pasta venv do ambiente virtual, nela estará todas as instalações e suas respectivas versões.

▶️ Executar este código para ativar o ambiente virtual:
```bash
venv/scripts/activate
```

❗Ao executar este código você deverá observar algo como:
```bash
(venv) caminho/arquivo/do/seu/projeto.py
```
ℹ️ (venv) -> Significa que o seu ambiente virtual está ativo

⚠️ Se o ambiente virtual não estiver ativo, os comandos que você executar usarão o Python e os pacotes do sistema operacional, e não os pacotes isolados do seu projeto.


### 3°: Executar os comandos de instalação das dependências
```bash
pip install django mysqlclient djangorestframework
``` 


### 4°: Criar um arquivo .env na RAIZ do projeto com as seguintes informações
```env
 DATABASE_NAME='Seu_nome_no_banco_de_dados'
 DATABASE_USER='Seu_nome_de_usuário_no_banco_de_dados'
 DATABASE_PASSWORD='Sua_senha_do_banco_de_dados'
 KEY_SECRET='Sua_SECRET_KEY_do_settings.py'
```
🔐 Essas variáveis contêm informações sensíveis, como as credenciais para conexão com o banco de dados e a chave secreta usada pelo Django. Devem ser armazenadas com segurança e nunca compartilhadas publicamente.

⚠️ Ao preencher o arquivo .env, você estará configurando a conexão com o banco de dados.
A biblioteca 'python-dotenv' será responsável por carregar essas variáveis de ambiente.
No 'settings.py', foi utilizada uma função para carregar as credenciaís para seus respectivos campos, se as variáveis não estiverem declaradas a função levantará um erro personalizado de facíl compreendimento de onde está o erro.

📌 Para entender melhor, consulte o settings.py e leia os comentários explicativos no código.


### 5°: Aplicar as migrações para o banco de dados
```bash
python manage.py makemigrations
python manage.py migrate
```
📝 Primeiro comando: Gera arquivos de migração a partir das alterações feitas nos modelos

📝 Segundo comando: Aplica as alterações no banco de dados, executando as mudanças definidas pelos arquivos gerados.


### 6°: Rodar o projeto

⚠️ Se NÃO ativou o ambiente virtual:
```bash
venv/scripts/activate
```

▶️ Em seguida: executar este código para iniciar o projeto
```bash
python manage.py runserver
```