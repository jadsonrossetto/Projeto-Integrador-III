###########################################################################
# Author: Daniel Marinho Ferreira de Souza
# modification: 26/03/2023 
#
# 
# 
# 
# Documentação base: 
#                  1° 
#                  2° 
#                  3° 
###########################################################################


from connection.connertion_database import MySqlQuary
from bs4 import BeautifulSoup

class DatabaseParser:
    
    
    def __init__(self, debug:bool, base_dados:str) -> None:
        self.debug = debug
        self.base_dados = base_dados
        
      
    def isDatabasePageAvailable(self, query:str) -> bool:
        '''
        Função tem o proposito de verificar se existe no banco de dados o page salva no log api.
        '''
        if query != None:
            
            db = MySqlQuary(True)
            sucess = db.run_query(query)
            
            if len(sucess) == 0:
                return False
            else:
                return True
        
        
        
    
    def from_database(self, tupla):
      success=False 
      soup=BeautifulSoup
      return success, soup
      
    def actual(self, val):
   
        if val != None and val != '':
            return True
        else:
            return False    