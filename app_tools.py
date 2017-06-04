import base64
import os
import traceback
from app_config import config



def saveFile(name, data):
    try:
        temp, ext = os.path.splitext(name)
        newname = genUniqStr  + ext
        fh = open(config["path"] + "/" + newname, "wb")
        fh.write(base64.b64decode(data.encode('utf-8')))
        fh.close()
        return newname
    except:
        return None
        
def parsw_w2ui_json(json):
    try:
        result = {}
        for r in json:
            if (r == 'recid' and json[r] > 0):
                if json[r] != '':
                    result[r] = json[r]
            elif (r == 'record'):
                for rec in json[r]:
                    if isinstance(json[r][rec], dict):
                        result[rec] = json[r][rec]['recid']
                    elif isinstance(json[r][rec], list):
                        if json[r][rec][0]['content']:
                            result[rec] = saveFile(json[r][rec][0]['name'], json[r][rec][0]['content'])
                    else:
                        if json[r][rec] != '':    
                            result[rec] = json[r][rec]
        return result
    except:
        traceback.print_exc()
        return False
        
def sendMail(fromaddr, message, sendlist):

    msg = "\r\n".join([
                      "From:" + fromaddr,
                      "To:" + ", ".join(sendlist),
                      "Subject: " + message.subject,
                      "",
                      message.text
                      ])
    server = smtplib.SMTP(config['mail_server'], config['mail_server_port'])
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(config['mail_username'], config['mail_password'])
    server.sendmail(config['mail_username'], sendlist, msg.encode('utf-8'))
    server.quit()