# DesenvolvimentoBancoCarros
Desenvolvimento para a matéria de Banco de dados 2


Seguindo o modelo provido pelo professor Lucas Debatin aqui estamos realizando o 
desenvolvimento de uma aplicação a qual utiliza um Bando de dados não relacional para manipular dados de Carros, suas marcas e modelos.
Nossa linguagem de programação escolhida foi Python e o banco de dados não relacional escolhido foi o MongoDB


Descrição breve do banco: 
 O MongoDB é um banco de dados NoSQL orientado a documentos, o que significa que ele armazena dados em documentos flexíveis semelhantes a JSON, 
 em vez de tabelas e linhas como em bancos de dados relacionais.

Descrição breve de Python:
Python é uma linguagem versátil, poderosa e popular, adequada para uma ampla gama de aplicações. Seu foco na legibilidade do código e na produtividade do desenvolvedor tornam-no uma excelente escolha para iniciantes e profissionais de programação.

Descrição breve do por quê utilizar python e MongoDB:

    PyMongo: É o driver oficial do MongoDB para Python, permitindo a interação entre a linguagem e o banco de dados.
    Conexão: MongoClient do PyMongo para estabelecer a conexão com o MongoDB, fornecendo a URL de conexão correta.
    Operações CRUD: Utilizar os métodos fornecidos pelo PyMongo, como insert_one(), insert_many(), find(), update_one(), update_many(), delete_one(), e delete_many(), para executar operações CRUD (Create, Read, Update, Delete) no banco de dados.
    Consultas: Construir consultas usando operadores de consulta para recuperar documentos com base em critérios específicos.
    Manipulação de documentos: Acessar e modificar campos de documentos BSON, adicionando novos campos ou removendo campos existentes.
    Índices: Criar índices para melhorar o desempenho das consultas, usando a função create_index() do PyMongo.
    Gerenciamento de erros: Tratar e gerencie exceções que podem ocorrer durante a interação com o MongoDB, garantindo o tratamento adequado de erros de conexão e consultas.
    Funcionalidades avançadas: O PyMongo oferece recursos avançados, como agregação de dados, transações e controle de concorrência.

    
