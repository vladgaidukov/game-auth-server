
config = {
#database
    'host': '127.0.0.1',
    'user': 'rbapp',
    'password': 'password',
    'database': 'robotsbattle',
#wsgiserver
    'server_port': 84,
    'server_host': '0.0.0.0',
#file
    'path': './uploads',
    'size': 5242880,
#adminsite
    'admlogin': 'admin',
    'admpass': 'admin',
#errortext
    'error': {
        'fuck': {'err': -1},
        'decode': {'err': 0},
        'login': {'err': 1},
        'auth': {'err': 2},
        'params': {'err': 3},
        'encode': {'err': 4}
    }
}
