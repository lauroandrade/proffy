# Proffy Discovery

Projeto desenvolvido durante a <i>Next Level Week (NLW)</i>, na Trilha Discovery. O evento é organizado pela <a href="https://github.com/Rocketseat/">Rocketseat</a>.

<hr />

<h2>Tecnologias utilizadas</h2>
<ul>
  <li>Front-end: CSS, HTML, Javascript;</li>
  <li>Back-end: <a href="https://flask.palletsprojects.com/en/1.1.x/">Flask</a>, um micro-framework para aplicações web baseado em Python;</li>
  <li>Banco de Dados: SQLite 3.</li>
</ul>

No projeto original da Rocketseat, a tecnologia utilizada no back-end foi o Node.js. Escolhi o Flask, pois tenho mais familiaridade com Python.

<hr />

<h2>Execução do projeto</h2>

```
crie um diretório para receber a aplicação
$ mkdir proffy-discovery

no diretório, crie e ative um ambiente virtual para isolar as dependências do projeto das dependências já instaladas em sua máquina.
$ sudo pip install virtualenv
$ which python3   # copie o retorno deste comando!
$ virtualenv -p '/path/to/python3' ENV  # cole o retorno no lugar de '/path/to/python3'
$ source ENV/bin/activate

ainda na pasta raíz do diretório, clone a aplicação e instale as dependências:
$ git init
$ git clone https://github.com/lauroandrade/proffy.git
$ pip install -r proffy/requirements.txt

agora, basta executar a aplicação:
$ python proffy/mainapp/mainapp.py

```




