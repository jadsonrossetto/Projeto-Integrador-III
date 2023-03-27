###########################################################################
# Author: Daniel Marinho Ferreira de Souza
# modification: 26/03/2023 
#
# Essa classe utilizada para realizar pesquisa no Banco MySql sobre dados fornecido 
# se não tive, realizar busca pela APi da liquipidia e gravar os dados de retorno no banco
# 
# Documentação base: 
#                  1° 
#                  2° 
#                  3° https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
###########################################################################

import requests
import api.liquipediapy.exceptions as ex
from connection.connertion_database import MySqlQuary
from api.liquipediapy.database_parser import DatabaseParser
from bs4 import BeautifulSoup
from urllib.request import quote
import json as _json


class liquipediapy:

    
    def __init__(self, appname=str, game=str , base_dados:str='', debug_database:bool=False) -> None:
        '''
        Construtor da class
        '''
        self.appname=appname
        self.game=game
        self.__headers={'User-Agent': appname, 'Accept-Encoding': 'gzip'}
        self.__base_url='https://liquipedia.net/'+game+'/api.php?'
        self.__base_dados=base_dados
        self.__debug=False
        self.dabug_database=debug_database #passar valor True para verficar se existe essa pagina na tebale
        self.devparser:DatabaseParser
        self.__debug:bool
        
    def check_dabug_database(self):
        #Metodo de verificação se vai utilizar base de dados para armazenar pagina pesquisada
        #Se não somente faz a pesquisa
        if self.dabug_database == False:
            return 
        else:
            self.devparser = DatabaseParser(self.dabug_database, self.__base_dados)
            self.__debug = True
        return
    
    def parse(self,page):
        # Metodo que realizar pesquisar da pagina 
        # executando primeiramente o "Metodo: check_dabug_database "
        self.check_dabug_database();
        success=False
        select ="""SELECT Html FROM LOGRESTAPI """
        data = f"WHERE Page_='{page}' AND BaseUrl='{self.__base_url}' AND Game='{self.game}' " 
        query = select + data 
                    
        
        if self.__debug and self.devparser.isDatabasePageAvailable(query): #Melhorar generalidade
            print('Já existe aquivos pagina do banco')
            success = True
           # success, page_html = self.devparser.from_database()
        else:
            url = self.__base_url+'action=parse&format=json&page='+page
            response = requests.request('Get', url, headers=self.__headers, timeout=120)
            
            if response.status_code == 200:
                try:
                    page_html = response.json()['parse']['text']['*']
                    # Tratamento page_html
                    page_html = page_html.replace(' ', '')
                    page_html = page_html.replace('/', f'\\')
                    page_html = page_html.replace('"', "'")
                except KeyError:
                    raise ex.RequestsException(response.json(),response.status_code)
            else:
                raise ex.RequestsException(response.json(),response.status_code)
        
            if success == False:
                # Tratamento headers
                headers =  _json.dumps(self.__headers)
                headers = headers.replace('"',"")
                
                insert = """INSERT INTO LOGRESTAPI (IdApi, Url, Page_, Headers, BaseURL, Html, Game) VALUES (%s, %s, %s, %s, %s, %s, %s) """ 
                data = (None, url , page, headers, self.__base_url, page_html, self.game)
                
                db = MySqlQuary()
                sucess = db.run_query(insert, data)
                return sucess