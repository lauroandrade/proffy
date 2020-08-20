# Proffy Discovery
<hr />

## Sobre ##
Projeto desenvolvido durante a <i>Next Level Week (NLW)</i>, na Trilha Discovery, durante a semana dos dias 03 a 09 de Agosto de 2020 e organizado pela <a href="https://github.com/Rocketseat/">Rocketseat</a>.

O objetivo da plataforma é conectar alunos e professores de forma rápida e simples. 

<hr />

## Tecnologias utilizadas ##
<ul>
  <li>Front-end: CSS, HTML, Javascript;</li>
  <li>Back-end: <a href="https://flask.palletsprojects.com/en/1.1.x/">Flask</a>, um micro-framework para aplicações web baseado em Python;</li>
  <li>Banco de Dados: SQLite3.</li>
</ul>

No projeto original da Rocketseat, a tecnologia utilizada no back-end foi o Node.js. Escolhi o Flask, pois tenho mais familiaridade com Python.

<hr />

## Execução do projeto ##

#### Antes de começar, certifique-se de que o Python 3 e o virtualenv estão instalados em sua máquina. ####

Crie um diretório para receber a aplicação:

```
mkdir proffy-discovery
```

No diretório, crie um ambiente virtual e o ative para isolar as dependências do projeto das dependências já instaladas em sua máquina:

```
sudo pip install virtualenv
which python3   # copie o retorno deste comando!
virtualenv -p '/path/to/python3' ENV  # cole o retorno no lugar de '/path/to/python3'
source ENV/bin/activate
```

Ainda na pasta raíz do diretório, clone a aplicação e instale as dependências:

```
git init
git clone https://github.com/lauroandrade/proffy.git
pip install -r proffy/requirements.txt
```

Execute a aplicação:

```
python proffy/mainapp/mainapp.py
```

Tudo pronto! Agora, basta entrar no navegador e acesso a rota do <a href="http://localhost:5500">LocalHost</a>. 


