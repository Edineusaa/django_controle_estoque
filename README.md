# Projeto Django: Controle de Estoque
Descrição: Processo para criação de um projeto de controle de estoque contendo apps de produtos, 
## Prerequisitos
- VSCODE
- Python 3.8 ou superior

### Steps para criação de um projeto
01. Criação do repositorio
> mkdir nome_da_pasta

02. Acessar o Repositorio
> cd nome_da_pasta

03. Criar o ambiente virtual
> python - m venv nome_ambiente_virtual

04. Acessar o ambiente virtual
- windows:
> .\nome_ambiente_virtual\Scripts\activate
- linux ou mac:
> source nome_ambiente_virtual/bin/activate

05. Instalar os pacotes(django,...)
> pip install django
- Instalando uma lista de pacotes:
> pip install -r requeriments.txt

06. Criação do projeto
> django-admin startproject nome_projeto .

07. Criação do app
> django-admin startapp nome_app

08. Criação do model.py [nome_app/models.py] e configuração no arquivo settings.py [nome_projeto/setting.py]

09. Realizar as migrações no banco de dados
- criar as migrações dos models
> python manage.py makemigrations
- aplicar as migrações no banco de dados
> python manage.py migrate

10. Criação do Super Usuario
> python manage.py creatsuperuser

11. startar o servidor de desenvolvimento
> python manage.py runserver