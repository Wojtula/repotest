#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dane.py

import csv
def dane_z_pliku(plik):
    dane = [] #pusta lista
    with open(plik, newline = '', encoding = 'utf8')as plikcsc:
        tresc = csv.reader(plikcsv, delimiter = '\t')
        for record in tresc:
            dane.append(rekord)
    return dane
        

def main(args):
    premia = dane_z_pliku('premia.txt')
    print (premia)
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
