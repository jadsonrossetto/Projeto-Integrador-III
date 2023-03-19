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
        
        self.config_ = os.path.expanduser('~\\OneDrive\\Faculdade\\Projeto Integrador III\\app\\view\\static_request_api')
        
        if self.config_ != '':
            return self.config_
        
    def query_sql(self, file_query):
        '''
        Função que busca a query no arquivo informado.
        @self.config_ : local aonda se enconrar os aquivos slq
        return query -> que tem nesse aquivo.
        '''
        self.config_ = os.path.expanduser('~\\Daniel\\OneDrive\\Faculdade\\Projeto Integrador III\\sql')
        
        with open(self.config_+file_query+'.sql') as query_read:
            query = query_read.read()
            
            if query != None:
                return query