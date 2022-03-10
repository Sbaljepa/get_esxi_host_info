from pyvim import connect
import json
def get_hostinfo():
    with open('cred.json') as data_file:
        global hosts,user,pwd
        data = json.load(data_file)
        user = data['username']
        pwd = data['password']
        #host =  data['host']
        hosts =[data['host']]
    #return host,user,pwd
   # return hosts,user,pwd
def connect_to_host():
    get_hostinfo()
    for host in hosts:
        try:
            si = connect.SmartConnectNoSSL(host=host, user=user, pwd=pwd)
            print("Connected to {}".format(host))
        except:
            print("Failed to connect to {}".format(host))
        return si