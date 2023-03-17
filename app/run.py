from connection.connertion_database import MySqlQuary
#from controller.api_liquipedia import Api_liquipedia


sql = MySqlQuary()
sql.sqltoQuery('SELECT * FROM USUARIO')



#api = Api_liquipedia('https://liquipedia.net/counterstrike/Main_Page')
#api.query_params('query','json','search', 'Daniel%20Marinho')
#data = api.api_get()
#print(data)
