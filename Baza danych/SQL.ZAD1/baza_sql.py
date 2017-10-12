#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dane.py
#  

#  
import sqlite3

def main(args):
    
    con = sqlite3.connect(':memory:')
    cur = con.cursor()   #utworzenie kursora
    
    with open('pracownicy.sql', 'r') as plik:
            cur.executescript(plik.read())
    
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
