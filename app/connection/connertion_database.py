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
    
    def __init__(self, use_pure:bool=False,) -> None:
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
        self.host =     Protect(True).key_database('HOST')
        self.port =     Protect(True).key_database('PORT')
        self.database = Protect(True).key_database('DATABASE')
        self.user =     Protect(True).key_database('USER')
        self.password = Protect(True).key_database('PASSWORD')
        
    
    def connect(self) -> bool:
        '''
        Esse método realiza a conexão com o banco de dados MySql retorna se teve sucesso.
            
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
            self.connection = mysql.connector.connect( host=self.host,               #Protect(True).key_database('HOST'), 
                                                       database=self.database,       #Protect(True).key_database('DATABASE'))
                                                       user=self.user,              #Protect(True).key_database('USER'),
                                                       password=self.password      #Protect(True).key_database('PASSWORD'),                                      
                                                    )
            if self.connection != None:
                return True 
            
        except mysql.connector.Error as error:
            
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database não existe")
                
            if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Usuáro ou  senha  está errado")
                print(error)       
        return False
    
        
    def run_query(self, query:str, data:tuple=''):
        '''
        Função realizar Insert e select no banco
        
        @para inserir informar os dois metodo
           >>> run_query(query, data)
            
        @para realizar select informar somente o metodo query
          >>> run_query(query)
        '''
        
        
        try:
            if self.connect() != False:
                cursor = self.connection.cursor()
                if data != '':
                    cursor.execute(query, data)
                    result = cursor.fetchall()
                    self.connection.commit()
                else: 
                    cursor.execute(query)
                    result = cursor.fetchmany()
                    self.connection.commit()
                    
                return result 
        except mysql.connector.Error as error:
            return "Erro: {}".format(error.msg)
        finally:
            if self.connection.is_connected:
                self.connection.close()