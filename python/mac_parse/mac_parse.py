#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

def mac_parse(mac_input, vendor='all'):
    mac_input = list(mac_input.strip().lower())
    mac = []
    for i in mac_input:
        if i.isalnum():
            mac.append(i)
    mac = ''.join(mac)
    MAC = mac.upper()
    mac_default = '{}:{}:{}:{}:{}:{}'.format(mac[0:2],mac[2:4],mac[4:6],mac[6:8],mac[8:10],mac[10:12])
    mac_mikrotik = '{}:{}:{}:{}:{}:{}'.format(MAC[0:2],MAC[2:4],MAC[4:6],MAC[6:8],MAC[8:10],MAC[10:12])
    mac_edge_core = '{}-{}-{}-{}-{}-{}'.format(mac[0:2],mac[2:4],mac[4:6],mac[6:8],mac[8:10],mac[10:12])
    mac_cisco = '{}.{}.{}'.format(MAC[0:4],MAC[4:8],MAC[8:12])
    mac_huawei = '{}-{}-{}'.format(MAC[0:4],MAC[4:8],MAC[8:12])
    if vendor == '-d':
        return mac_default
    elif vendor == '-m':
        return mac_mikrotik
    elif vendor == '-e':
        return mac_edge_core
    elif vendor == '-c':
        return mac_cisco
    elif vendor == '-h':
        return mac_huawei
    else:
        return mac_default, mac_mikrotik, mac_edge_core, mac_cisco, mac_huawei
