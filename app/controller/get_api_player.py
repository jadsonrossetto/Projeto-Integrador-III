from connection.security.protect_database import Protect
from api.liquipediapy import liquipediapy
import time

class LiquiApi:

    def __init__(self):
        """
        Contrutor da class
        """
        self.app_nome = 'Analyst'
        
    def timer(self, seg=30):
        if seg != 0:
                while seg:
                    time.sleep(0.03)
                    seg = seg - 1
        else:
            return False
        return True
        

    def get_cs_page(self, page=str, table=str, debug_database:bool=False):
        """
        Função que realizar bunca pela API(liquipediapy).
        
        """
        if (self.timer()):
            liquipy_object = liquipediapy(self.app_nome,'counterstrike', table , debug_database) 
            
            if liquipy_object != None:
                listObj = liquipy_object.parse(page)
                
                return listObj
            else:
                return
        
    