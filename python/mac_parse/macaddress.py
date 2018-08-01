#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from sys import argv
from mac_parse import mac_parse

if len(argv) > 2:
    print('\n{}\n'.format(mac_parse(argv[1],argv[2])))
else:
    print('\n{}\n'.format(mac_parse(argv[1])))
