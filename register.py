#!/usr/bin/python3
#script by kira_xc
#youtube : https://www.youtube.com/kiraxc
#instagram : kira_xc
#github : kira-xc
import json
import base64
import requests
from uuid import UUID
from os import urandom,path
from time import timezone
from typing import BinaryIO
from binascii import hexlify
from time import time as timestamp
from locale import getdefaultlocale as locale

from amino.lib.util import exceptions, headers, device, objects, helpers
from amino.socket import Callbacks, SocketHandler
import random,string,hashlib,base64,importlib
def deviceaoss():
    return str('01' + (hardwareInfo := hashlib.sha1(''.join(random.choices(string.ascii_uppercase + string.digits, k = 1000)).encode("utf-8"))).hexdigest() + hashlib.sha1(bytes.fromhex('01') + hardwareInfo.digest() + base64.b64decode("6a8tf0Meh6T4x7b0XvwEt+Xw6k8=")).hexdigest()).upper()
device=deviceaoss()
print("the new device id : ",device)
from os import _exit,system
def deviceido(device):
    dvvv='{\n\"device_id\": \"'+device+'\", \n\"device_id_sig\": \"AaauX/ZA2gM3ozqk1U5j6ek89SMu\", \n\"user_agent\": \"Dalvik/2.1.0 (Linux; U; Android 7.1; LG-UK495 Build/MRA58K; com.narvii.amino.master/3.3.33180)\"\n}'
    fdev=open("device.json","w+")
    fdev.write(dvvv)
    fdev.close()


try:
    import amino
except:
    print("connect to network for run !\or update the amino.py to last upadate  ")
    deviceido(device)
    amino.device.DeviceGenerator(deviceId=device)
    _exit(1)
class newk(amino.Client):
   
    def register(self, nickname: str, email: str, password: str, deviceId: str = device):
            """
            Register an account.

            **Parameters**
                - **nickname** : Nickname of the account.
                - **email** : Email of the account.
                - **password** : Password of the account.
                - **deviceId** : The device id being registered to.

            **Returns**
                - **Success** : 200 (int)

                - **Fail** : :meth:`Exceptions <amino.lib.util.exceptions>`
            """
            data = json.dumps({
                "secret": f"0 {password}",
                "deviceID": deviceId,
                "email": email,
                "clientType": 100,
                "nickname": nickname,
                "latitude": 0,
                "longitude": 0,
                "address": None,
                "clientCallbackURL": "narviiapp://relogin",
                "type": 1,
                "identity": email,
                "timestamp": int(timestamp() * 1000)
            })

            response = requests.post(f"{self.api}/g/s/auth/register", data=data, headers=headers.Headers(data=data).headers, proxies=self.proxies, verify=self.certificatePath)
            if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
            else: return response.status_code
        
def renew():
    class newk(amino.Client):
   
        def register(self, nickname: str, email: str, password: str, deviceId: str = device):
                """
                Register an account.

                **Parameters**
                    - **nickname** : Nickname of the account.
                    - **email** : Email of the account.
                    - **password** : Password of the account.
                    - **deviceId** : The device id being registered to.

                **Returns**
                    - **Success** : 200 (int)

                    - **Fail** : :meth:`Exceptions <amino.lib.util.exceptions>`
                """
                data = json.dumps({
                    "secret": f"0 {password}",
                    "deviceID": deviceId,
                    "email": email,
                    "clientType": 100,
                    "nickname": nickname,
                    "latitude": 0,
                    "longitude": 0,
                    "address": None,
                    "clientCallbackURL": "narviiapp://relogin",
                    "type": 1,
                    "identity": email,
                    "timestamp": int(timestamp() * 1000)
                })

                response = requests.post(f"{self.api}/g/s/auth/register", data=data, headers=headers.Headers(data=data).headers, proxies=self.proxies, verify=self.certificatePath)
                if response.status_code != 200: return exceptions.CheckException(json.loads(response.text))
                else: return response.status_code
            
from os import system
from random import randint
from ast import literal_eval

password=input("your initial password : ")
nicko=str(input("your name : "))
cpt3=0
while True:
    importlib.reload(amino)
    deviceido(device)
    amino.device.DeviceGenerator(deviceId=device)
    renew()
    amino.device.DeviceGenerator(deviceId=device)
    deviceido(device)
    if cpt3==3:
        device=deviceaoss()
        cpt3=0
    cpt3+=1
    client=newk(deviceId=device)
    client.device_id=device
    nickname=nicko+str(randint(1,99999999))
    email=input("give me \"email\" for new sign up  : ")
    try:
        z=client.register(nickname=nickname, email=email, password=password, deviceId=device)
    except Exception as e:
        z=0
        if hasattr(e, 'message'):
            mess=str(e.message)
            print(e.message)
        else:
            mess=str(e)
            dcc=literal_eval(mess)
            messo=dcc.get("api:message")
            print("\n\n\n"+str(messo)+"\n\n\n")
            dc=literal_eval(mess)
            if dc.get("api:statuscode")==219:
                device=deviceaoss()
                cpt3=0
                print("the device id changed to : ",device)
        continuee=input("to by continue y/n : ")
        if continuee=="n":
            _exit(1)
    if z==200:
        client.login(email=email,password=password)
        aminoId=str(client.profile.aminoId)
        client.request_verify_code(email=email)
        kkkkk=False
        while kkkkk==False:
            try:
                code=input("verify code in your email : ")
                verr=client.verify(email=email,code=code)
                if verr==200:
                    kkkkk=True
            except:
                dfg=input("false !!!!\n\nto be repeat?  y . or resend new code n ?  y/n chousse y : ")
                if dfg=="n":
                    client.request_verify_code(email=email)
        client.activate_account(email=email,code=code)
        print("👌")
        print("your name ",nickname)
        print("your user : @"+aminoId)
        print("email : ",email)
        #client.join_community("3")
        client.logout()
        print("\n\n\n")
        saveemail="echo "+email+">>email.txt"
        system(saveemail)
        if path.exists("email.json")==False:
            data=[]
        else:
            with open('email.json') as json_file:
                data = json.load(json_file)
        data.append({
            'email': email,
            'password': password,
            'device': device
            })
        try:
            with open('email.json', 'w') as outfile:
                json.dump(data, outfile)
        except:
            print("cant save email.json")    
    