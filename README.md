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


1°: Instalar o dotenv
```bash
pip install python-dotenv
```
📝 É uma biblioteca que carrega variáveis de ambiente de um arquivo .env para o ambiente do sistema.


2°: Criar um ambiente virtual
```bash
python -m venv venv
```
📝 cria a pasta venv do ambiente virtual, nela estará todas as instalações e suas respectivas versões.

Rodar este código para ativar o ambiente virtual:
```bash
venv/scripts/activate
```

Ao rodar este código você deverá ver algo como:
```bash
(venv) caminho/arquivo/do/seu/projeto.py
```
(venv) -> Significa que o seu ambiente virtual está ativo

📝 Se o ambiente virtual não estiver ativo, os comandos que você executar usarão o Python e os pacotes do sistema operacional, e não os pacotes isolados do seu projeto.


3°: Rodar os comando de instação das dependências
```bash
pip install django mysqlclient djangorestframework
``` 


4°: Criar um arquivo .env na RAIZ do projeto
Em seguida: 
```env
 DATABASE_NAME='Seu_nome_no_banco_de_dados'
 DATABASE_USER='Seu_Nome_de_user_no_banco_de_dados'
 DATABASE_PASSWORD='Sua_senha_no_banco_de_dados'
 KEY_SECRET='SECRET_KEY_no_settings.py'
```
Essas variáveis são informações sigilosas, como credenciaís para a conexão do banco de dados e a chave secreta para requisições no django. 
❗Devem ser guardadas a sete chaves. 

⚠️ Preenchendo com as informações no arquivo .env, você já está configurando a conexão com o database. A biblioteca dotenv carrega essas variáveis de ambiente e no settings.py usei uma função que trata essas variáveis, para uma melhor explicação acessar o settings.py e ler a função comentada.


5°: Aplicar as migrações do banco de dados
```bash
python manage.py makemigrations
python manage.py migrate
```
1 - Primeiro comando: Gera arquivos de migração a partir das alterações feitas nos modelos
2 - Segundo comando: Aplica as alterações no banco de dados, executando as mudanças definidas pelos arquivos gerados.


6°: Rodar o projeto
Se NÃO ativou o ambiente virtual:
```bash
venv/scripts/activate
```

Em seguida:
```bash
python manage.py runserver
```