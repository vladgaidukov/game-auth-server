from app_config import config
from app_tools import *
from application import *
import json
import bottle as btl

## TODO remove
from urllib.parse import quote

btl.BaseRequest.MEMFILE_MAX = config['size']

app = Application()

##############################################################################
#admin routes
##############################################################################

@btl.get('/userAuth')
def userAuth():
    try:
        data = btl.request.query['data']
        return app.userAuth(data)
    except:
        return ""
        
@btl.get('/userData')
def userData():
    #try:
        data = btl.request.query['data']
        print(data)
        return app.userData(data)
    #except:
        #return config['error']['fuck']
    
@btl.get('/decode')
def decode():
    data = btl.request.query['data']
    data = base64.b64decode(data)
    data = acrypt.crypt_rc4(str(data,'utf-8'), acrypt.key)
    return data

@btl.get('/encode')
def encode():
    data = btl.request.query['data']
    data = acrypt.crypt_rc4(data, acrypt.key)
    data = base64.b64encode(bytes(data, 'utf-8'))
    data = quote(data, safe='')
    return data

    
##############################################################################
#error routes
##############################################################################
@btl.error(404)
def error404(error):
    return ''

@btl.error(405)
def error405(error):
    return ''


btl.run(host=config['server_host'],
	server = 'tornado',
	port=config['server_port']
)
