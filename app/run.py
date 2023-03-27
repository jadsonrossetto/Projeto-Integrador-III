from controller.get_api_player import LiquiApi



api = LiquiApi()
list_api = api.get_cs_page('ESL/Pro League','LOGRESTAPI',True)
print(list_api)