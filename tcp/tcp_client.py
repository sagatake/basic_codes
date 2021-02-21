#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:54:02 2021

@author: takeshi-s
"""
import numpy as np
import shutil
import pprint
import sys
import os

import socket

def main():
    "Main function"
    
    text = input('Put text : ')
    output = tcp_client(text)
    print('Text : ', output)
    
def tcp_client(text):
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 55555))
        s.sendall(text.encode())
        data = s.recv(1024)
        data = data.decode()
    
    return data
        
if __name__ == '__main__':
    main()

