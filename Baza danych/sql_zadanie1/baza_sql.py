#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  baza_sql.py

import sqlite3


def main(args):
    con = sqlite3.connect(':memory:')
    cur = con.cursor()  # utworzenie kursora
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
