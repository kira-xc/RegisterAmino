#!/usr/bin/python3
#script by kira_xc
#youtube : https://www.youtube.com/kiraxc
#instagram : kira_xc
#github : kira-xc
import json
import requests
from os import path
from time import timezone
import importlib

def deviceaoss():
    return requests.get("https://www.deviceramino.tk/deviceId").text
device=deviceaoss()
print("the new device id : ",device)


from os import _exit,system

def koj(yako):
    ro=yako
    vvk=list(ro)
    vvk[1]=str(99169-99162)
    vvk[0]= str(99999999-99999998)
    return "".join(vvk)
def soko():
    return koj(deviceaoss())
def sodo(w):
    return koj(w)
device=sodo(device)
def deviceido(device):
    dvvv='{\n\"device_id\": \"'+device+'\", \n\"device_id_sig\": \"AaauX/ZA2gM3ozqk1U5j6ek89SMu\", \n\"user_agent\": \"Dalvik/2.1.0 (Linux; U; Android 7.1; LG-UK495 Build/MRA58K; com.narvii.amino.master/3.3.33180)\"\n}'
    fdev=open("device.json","w+")
    fdev.write(dvvv)
    fdev.close()
try:
    import aminofix as amino
except:
    print("connect to network for run !\or update the amino to last upadate  ")
    deviceido(device)
    amino.device.DeviceGenerator(deviceId=device)
    _exit(1)
from os import system
from random import randint
from ast import literal_eval

password=input("your initial password : ")
nicko=str(input("your name : "))
cpt3=0
while True:
    importlib.reload(amino)
    amino.device.DeviceGenerator(deviceId=device)
    deviceido(device)
    if cpt3==3:
        device=soko()
        cpt3=0
    cpt3+=1
    client=amino.Client(deviceId=device)
    client.device_id=device
    nickname=nicko+str(randint(1,99999999))
    rrr=False
    while rrr==False:
        try:
            email=input("give me \"email\" for new sign up  : ")
            cccccw=client.request_verify_code(email=email)
            if cccccw==200:
                rrr=True
        except Exception as e:
            mess=str(e)
            dcc=literal_eval(mess)
            messo=dcc.get("api:message")
            print("\n"+str(messo)+"\n")
        
    code=input("i need the code in your email : ")
    kkkkk=False
    while kkkkk==False:
        try:
            z=client.register(nickname=nickname, email=email, password=password,verificationCode=code, deviceId=device)
            if z==200:
                kkkkk=True
        except Exception as e:
            mess=str(e)
            dcc=literal_eval(mess)
            messo=dcc.get("api:message")
            print("\n"+str(messo))
            dc=literal_eval(mess)
            if dc.get("api:statuscode")==219:
                device=soko()
                cpt3=0
                print("the device id changed to : ",device)
            dfg=input("false !!!!\n resend new code r ?   or change email e : \n    r/e ? : ")
            if dfg=="r":
                client.request_verify_code(email=email)
                code=input("i need the code in your email : ")
            if dfg=="e":
                 email=input("give me \"email\" for new sign up  : ")
                 client.request_verify_code(email=email)
                 code=input("i need the code in your email : ")
   
    
        
    if z==200:
        client.login(email=email,password=password)
        aminoId=str(client.profile.aminoId)
        #client.activate_account(email=email,code=code)
        print("👌")
        print("your name ",nickname)
        print("your user : @"+aminoId)
        print("email : ",email)
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

    