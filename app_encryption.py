import uuid, hashlib, base64, traceback
from urllib.parse import quote
import json
from app_config import config

__author__ = "Vlad"
__date__ = "$14.10.2016 12:44:09$"


class App_Encryption:
    
    def __init__(self,secret):
        self.key = secret
        
        
    def is_json(self, jsondata):
        try:
            json.loads(jsondata)
        except ValueError:
            traceback.print_exc()
            return False
        return True
    
    def crypt_rc4(self, data, key):
        c = 0
        box = list(range(256))
        for i in list(range(256)):
            c = (c + box[i] + ord(key[i % len(key)])) % 256
            box[i], box[c] = box[c], box[i]
        c = 0
        y = 0
        out = []
        for char in data:
            c = (c + 1) % 256
            y = (y + box[c]) % 256
            box[c], box[y] = box[y], box[c]
            out.append(chr(ord(char) ^ box[(box[c] + box[y]) % 256]))

        return ''.join(out)

    def crypt_sha256(self, data):
        data = bytes(data, 'utf-8')
        hash_object = hashlib.sha256(data)
        hex_dig = hash_object.hexdigest()
        return hex_dig
    
    def encryption(self, fn):
        def encoded(link=None, data=None):
            if link and data:
                try:
                    if len(data)>3:
                        data = self.decodeJSON(data)
                    else:
                        return self.encodeJSON(config['error']['decode'])
                except:
                    traceback.print_exc()
                    return self.encodeJSON(config['error']['decode'])
                data = fn(link, data)
            else:
                data = fn()
            if data:
                data = self.encodeJSON(data)
            else:
                return self.encodeJSON(config['error']['decode'])
            return data
        return encoded

    def genUniqStr(self):
        return str(uuid.uuid4())
        
    def encodeJSON(self,data):
        data = json.dumps(data)
        data = self.crypt_rc4(data, self.key)
        data = base64.b64encode(bytes(data, 'utf-8'))
        data = quote(data, safe='')
        return data
        
    def decodeJSON(self,data):
        data =  base64.b64decode(data)
        data = self.crypt_rc4(str(data,'utf-8'), self.key)
        data = json.loads(data)
        return data


if __name__ == "__main__":
    print (__author__, __date__)


