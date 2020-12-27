#!/usr/bin/python3
#script by kira_xc
#youtube : youtube.com/kira_xc
#insta : kira_xc
#github : kira-xc
from os import _exit
try:
    import amino
except:
    print("connect to network for run !  ")
    _exit(1)
from os import system
from random import randint
from ast import literal_eval
client =amino.Client()
password=input("your initial password : ")
nicko=str(input("your name : "))
try:
    deviceids=open("deviceid.txt")
    deviceId=str(deviceids.readline()).strip()
    df=True
    print("\"deviceid.txt\" yes found 👌")
except:
    df=False
    deviceId='01B7AA1CF76DE9FCF8E11AC71E62B2FE54D66E376637B0C9FC4A50D1115FAD5F8F27C7ED2CF28DBCE0'
while True:
    nickname=nicko+str(randint(1,99999999))
    email=input("give me \"email\" for new sign up  : ")
    try:
        z=client.register(nickname=nickname, email=email, password=password, deviceId=deviceId)
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
                if df==True:
                    deviceId=(deviceids.readline()).strip()
                    if deviceId!="\n" and deviceId!="":
                        print ("new device id :" +str(deviceId))
                    else:
                        print("\nrenew your deviceid.txt file")
                        _exit(1)
                else:
                    print("\n \n\"deviceid.txt\" not faund ")
                    _exit(1)
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
        client.logout()
        print("\n\n\n")
        saveemail="echo "+email+">>email.txt"
        system(saveemail)
    
