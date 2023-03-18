from dotenv import dotenv_values
import os



class Protect:
        
    def __init__(self) -> None:
        self.config_ = ''
           
    def key_database(self, key=str):
        self.config_ = os.path.expanduser('~/app/connection/security/db.env')
        info = dotenv_values(self.config_, encoding="utf-8")  
        if info != None:
            return info[key]
        else :
            return 
        
    def folder_api(self):
        
        self.config_ = os.path.expanduser('~\\OneDrive\\Faculdade\\Projeto Integrador III\\app\\folder_api')
        
        if self.config_ != '':
            return self.config_