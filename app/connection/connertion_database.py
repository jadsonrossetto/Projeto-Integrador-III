###########################################################################
# Author: Daniel Marinho Ferreira de Souza
# Created: 11/03/2023
# Last Update: 
#
# Essa classe auxilia na conexão com o Banco de Dados MySql
# pip install mysql-connector-python==8.0.32
# Documentação base: 
#                  1° https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
#                  2° https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
#                  3°
###########################################################################

from connection.security.protect_database  import Protect
from mysql.connector import errorcode
import mysql.connector



class MySqlQuary : #Class que realizar conexão com bando Mysql
    
    def __init__(self, use_pure:bool=False, host=str, port=str, database=str, user=str, password=str) -> None:
        '''
        Construtor da class
        
        @use_pure : A configuração use_pure=False faz com que a conexão use a extensão C se sua instalação do Connector/Python a incluir, 
                    enquanto use_pure=True significa False que a implementação do Python é usada, se disponível.
        @host : varivael recebe host de conexão com banco
        @port : variavel recebe port de conexão com banco
        @database : variavel recebe nome do banco 
        @user : variavel recebe usuário do banco
        @password : variavel recebe senha do banco
        '''
        self.use_pure = use_pure
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        
        
        def __del__(self) -> None:
            if self.cursor:
                self.close() 
            
    def connect(self) -> None:
        '''
        Esse método realiza a conexão com o banco de dados MySql
            
        Parameters:
        @user : variavel do construtor com informação do usuario
        @password : variavel do construtor com informação da senha
        @host : variavel do construtor com informação host do banco
        @database : variavel do construtor com informação o nome do banco
        @use_pure : variavel dp construtor com a informação booll conexão de extenção com LP 'C' se sua instalação do Connector/Python a incluir.
        @use_unicode = Se deve usar Unicode (TRUE) -> Por padrão, as strings provenientes do MySQL 
        são retornadas como literais Python Unicode.Como prevenção está informado como verdadeiro
        '''
        try:
            self.connection = mysql.connector.connect( host=Protect.key_database('HOST'), 
                                                       user=Protect.key_database('USER'),
                                                       password=Protect.key_database('PASSWORD'),                                      
                                                       database=Protect.key_database('DATABASE'))
            return self.connection
        
        except mysql.connector.Error as error:
            
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database não existe")
            
            if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Usuáro ou  senha  está errado")
                print(error)       
        return 
        
    def sqltoQuery(self, query=str):
      
        if self.connect() != None:
            self.cursor = self.connection.cursor()
            self.cursor.execute(query)
            print(self.cursor.fetchone())
            
        else:
            print("Erro conexão com banco")