from connection.security.protect_database import Protect
from api.liquipediapy import liquipediapy
import time

class LiquiApi:

    def __init__(self, app_nome=str, game=str, debug_folder=str):
        self.app_nome = app_nome
        self.game = game
        self.debug_folder = debug_folder
        
        
    def timer(self, seg=30):
        
        if seg != 0:
                while seg:
                    time.sleep(1)
                    seg = seg - 1
        else:
            return False
        return True
        

    def get_cs_players(self):
     
        if (self.timer()):
            
            folder = Protect()
            self.folder = folder.folder_api()
            liquipy_object = liquipediapy(self.app_nome, self.game, self.debug_folder) 
            
            if liquipy_object != None:
                listObj = liquipy_object.parse('Main_Page')
                
                return listObj
            else:
                return
        
    