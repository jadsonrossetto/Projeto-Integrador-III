import time
import requests

#https://liquipedia.net/counterstrike/Portal:

class Api_liquipedia:
    
    
    def __init__(self, endpoint=str, time=3.05) -> None:
        self.endpoint = endpoint
        self.time = time
        
    '''   
    def player_v1(self):
        player = {}
    '''    
        

    def query_params(self, action=str, format=str, list=str, srsearch=str) -> None:
        
        if action != None and format != None and list != None and srsearch != None:
            
            self.params = {
                "action": action,
                "format": format,
                "list": list,
                "srsearch": srsearch
            }
        elif action != None and format != None:
             
            self.params = {
                "action": action,
                "format": format,
             } 
        else:
            return self.params
        
        return self.params 
    
    def api_get(self):
        
        api_session = requests.Session()
        
        if (self.endpoint != None and self.params != None):
            api_return = api_session.get(url=self.endpoint, params=self.params, timeout=self.time)
       
        if api_return.status_code == 200:
            return api_return.json(['query']['search'][0]['title'])
    
    
    