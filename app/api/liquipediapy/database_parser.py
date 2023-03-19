from connection.connertion_database import MySqlQuary


class DatabaseParser:
    
    
    def __init__(self,  config_folder: str) -> None:
        self.__folder_path = config_folder
        self.appname = None
        self.game = None
        self.base_url = None
        
    def isDatabasePageAvailable(self, endpoint:dict) -> bool:
        '''
        Função tem o proposito de verificar se existe no banco de dados o page salva no log api.
        '''
        for i in endpoint:
            self.appname = i['appnome'],
            self.game = i['base_url'],
            self.base_url = i['base_url']
              
        query = f"SELECT ApiJson FROM TESTE.API_LOG "
        match query != '':
            case self.actual(self.appname): 
                query = query+f"WHERE PAGE='{self.appname}' "
            case self.actual(self.game):
                query = query+f"AND Gema='{self.game}'"
            case self.actual(self.base_url):
                query = query+f"AND BaseUrl='{self.base_url}'"    
        connect = MySqlQuary().sqltoQuery(query)
        return  connect     
                
        
    def actual(self, val):
   
        if val != None:
            return True
        elif val == '':
            return False
        else: False
        