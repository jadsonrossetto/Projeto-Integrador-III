#from connection.connertion_database import MySqlQuary
#from controller.api_liquipedia import Api_liquipedia
#sql = MySqlQuary()
#sql.sqltoQuery('SELECT * FROM USUARIO')
'''api = Api_liquipedia('http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/')
api.query_public(730,1,'json')
#api.query_params('query','json','search', 'Daniel%20Marinho')
data = api.api_get()
print(data.)
'''
from controller.get_api_player import LiquiApi


api = LiquiApi('Analyst', 'counterstrike')

list_api = api.get_cs_players()

for i in list_api:
    print(list_api[i])