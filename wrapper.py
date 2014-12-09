#! /usr/bin/env python
# coding:utf-8

'''
ぱいてょんよくわかんない
'''

import sys
import os
import subprocess

def kovlive(ja_JP):
    python_path = sys.executable    
    kovlive_path = os.path.abspath('./kovlive/kovlive.py')
    
    p = subprocess.Popen([python_path, kovlive_path], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    
    p.stdin.write(bytes(ja_JP, 'utf-8'))
    kv_JP = p.communicate()[0]

    return str(kv_JP, 'utf-8')

#test
if __name__ == '__main__':
    a = kovlive('エナジードリンク')
    print(a)
