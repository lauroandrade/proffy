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

<h2>Prepararação para a execução do projeto</h2>
<ul>
  <li>Certifique-se de que o python3.6 está instalado em sua máquina;</li>
  <li>Crie e ative um <a href="https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais">ambiente virtual</a> em Python para isolar as dependências do projeto das dependências instaladas em sua máquina. Você também pode conferir a <a href="https://docs.python.org/3.6/library/venv.html">documentação oficial</a>, se preferir;</li>
  
  ```
  $ sudo pip install virtualenv
  $ which python3.6
  !* copie o retorno do comando dado *!
  $ virtualenv -p '/path/to/python3.6' ENV
  $ source ENV/bin/activate
  ```
 
  <li>Dentro do diretório onde está o ENV, clone o repositório:</li>
  
  ```
  $ git init
  $ git clone https://github.com/lauroandrade/proffy.git 
  ```
  
  <li>Instale as dependências do projeto:</li>
  
  ```
  $ pip install -r requirements.txt
  ```
  <li>Execute a aplicação:</li>
  
  ```
  $ python mainapp/mainapp.py
  ```
  
</ul>



