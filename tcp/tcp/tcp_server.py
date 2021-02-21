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
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 55555))
        s.listen(1)
        while True:
            print('Waiting ...')
            conn,addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    
                    # End if data==None
                    if not data:
                        break
                    
                    data = data.decode()
                    print('Data : {} (addr : {})'.format(data, addr))
                    
                    """
                    Put some process here
                    """
                    
                    output = 'Received successfully.'
                    
                    conn.sendall(output.encode())    
    
if __name__ == '__main__':
    main()

