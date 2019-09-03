#!/usr/bin/python
#-*- coding:utf-8 -*-

__author__ = 'zhouqin'

import requests
import os
import re
import json
import time
import socket
from random import randrange
from collections import OrderedDict

raw_log_path = './syslog_sample/'

def set_enterprise_ip():
    while True:
        host_ip = raw_input("请输入enterprise地址：")
        if re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", host_ip):
            return host_ip
            break

#发送数量设置
def set_log_number():
    while True:
        a = raw_input("发送logs的数量：")
        if a.isdigit():
            if int(a) > 0:
                return int(a)
                break

#内网设置
def set_intranet_ip():
    intraip = [172.16, 192.168]
    prefixIP = intraip[randrange(0, 2)]
    ip = ".".join((str(prefixIP), str(randrange(1, 256)), str(randrange(1, 256))))
    return ip

#外网设置
def set_internet_ip():
    while True:
        ip = ".".join((str(randrange(1, 256)), str(randrange(1,256)), str(randrange(1,256)), str(randrange(1,256))))
        return ip
        break

#高置信ioc设置
def set_ioc(host, type):
    url = 'http://' + host + ':9200/threat_intelligence_credibility/_search?pretty'
    payload = {"query": {"match": {"type": type}}, "sort": {"timestamp": "desc"}, "size": 10}
    response = requests.Session().post(url, json=payload)
    response_content = json.loads(response.content)
    if response.status_code == 200:
        #print response_content['hits']['hits'][0]['_source']['ioc']
        list_ioc = []
        for item in response_content['hits']['hits']:
            list_ioc.append(item['_source']['ioc'])
        #print list_ioc[randrange(1, 10)]
        return list_ioc[randrange(1, 10)]

#漏洞id设置
def set_vulid():
    pass

#更新syslog
def parse_json(raw_log_file):
    with open(raw_log_file,'r') as f:
        json_log = ''
        for line in f.readlines():
            line = line.strip("    ")
            line = line.strip('\r\n')
            json_log = json_log + line

        return json_log

def update_json_log(host, raw_log_file):

    data = []
    update_json = json.loads(parse_json(raw_log_file), 'utf-8', object_pairs_hook=OrderedDict)
    update_json['src'] = set_ioc(host=host, type="ip")
    update_json['dst'] = set_internet_ip()
    data = json.dumps(update_json)
    data = data.strip("{")
    data = data.strip("}")

    return data

#迭代多次方式
def send_json(raw_log_file, host, iter_times):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        HOST = host
        PORT = 514
        s.connect((HOST, PORT))

        count = 0
        # print send_json_log

        for i in range(int(iter_times)):
            send_json_log = update_json_log(host, raw_log_file)
            print send_json_log
            s.sendall(send_json_log)

            count = count + 1
            if count % 1000 == 0:
                time.sleep(1)

        print "Send '%s' file '%s' times success." % (raw_log_file, count)
    except BaseException as err:
        print "Send '%s' file failed, check it please!" % raw_log_file
    finally:
        s.close()

def start():
    host = set_enterprise_ip()

    iter_times = set_log_number()
    print iter_times

    starttime = time.time()
    print "Start time: " + str(starttime)

    for log_file in os.listdir(raw_log_path):
        print "Start send %s" % log_file
        send_json(raw_log_path + log_file, host, iter_times)

    endtime = time.time()
    print "End time: " + str(endtime)

    costtime = float(endtime) - float(starttime)
    print "Cost time: %s" % costtime


if __name__ == "__main__":
    start()


