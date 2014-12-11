#! /usr/bin/env python
# coding:utf-8

'''
ぱいてょんよくわかんない
'''

import sys
import os
import subprocess

BASEDIR = os.path.dirname(os.path.abspath(__file__))

def kovlive(ja_JP):
    python_path = sys.executable    
    kovlive_path = os.path.join(BASEDIR, './kovlive/kovlive.py')
    
    p = subprocess.Popen([python_path, kovlive_path], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    
    p.stdin.write(bytes(ja_JP, 'utf-8'))
    kv_JP = p.communicate()[0]

    return str(kv_JP, 'utf-8')

#test
if __name__ == '__main__':
    a = kovlive('エナジードリンク')
    print(a)
