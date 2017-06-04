import sqlgen
from app_config import config
from app_encryption import App_Encryption
from app_tools import *
import time
import json



db = sqlgen.SqlGen({
        'host': config[ 'host'],
        'user': config[ 'user'],
        'password': config[ 'password'],
        'database': config[ 'database']})
        
acrypt = App_Encryption(db.select('params',param = {'name': 'crypt_code'})['data'][0]['value'])

class Application:

    def getUser(self, data):
        if 'sid' in data:
            user_data = db.select('user',
                param = {
                        'sid': data['sid'],
                }
            )
            if user_data['status'] == 'success' and len(user_data['data'])>0:
                return user_data['data'][0]
            else:
                return config['error']['auth']
        else:
            return config['error']['params']

        
    @acrypt.encryption
    def userAuth(self, data):
        if 'name' in data and 'pass' in data:
            user_hash = data['name'] + data['pass']
            user_hash = acrypt.crypt_sha256(user_hash)
            
            user_data = db.select('user',
                param = {
                        'name': data['name'],
                        'pass': user_hash
                }
            )
            
            if user_data['status'] == 'success' and len(user_data['data'])>0:
                sid = acrypt.genUniqStr()
                set_sid = db.update('user', 
                    columns = {
                        'sid': sid,
                        'user_status_recid': 1,
                        'login_date': time.time()
                    }, 
                    param = {
                        'recid': user_data['data'][0]['recid']
                    }
                )
                if set_sid['status'] == 'success':
                    return {'sid': sid}
            else:
                return config['error']['login']
        else:
            return config['error']['params']
                    
    @acrypt.encryption
    def userData(self, data):
        user = self.getUser(data)
        if user and ('err' not in user):
            robots = db.select('robot',
                param = {
                        'user_recid': user['recid'],
                }
            )
            if robots['status'] == 'success':
                data = {
                    'user': user['name'],
                    'robot': robots['data']
                }
                return data
        else:
            return user
        
    
        
        
