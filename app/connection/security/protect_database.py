from dotenv import dotenv_values
import os



class Protect:
           
    def key_database(key=str):
        config_ = os.path.expanduser('~/OneDrive/Faculdade/Projeto Integrador III/app/connection/security/db.env')
        info = dotenv_values(config_, encoding="utf-8")  
        if info != None:
            return info[key]
        else :
            return 