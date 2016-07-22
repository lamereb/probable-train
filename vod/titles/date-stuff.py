#!/usr/bin/python2.7
from datetime import date
import sys

mo = str(date.today().month).zfill(2)
yr = str(date.today().year)
dy = str(date.today().day - 1).zfill(2)

yymmdd = yr + mo + dy
print yymmdd
print sys.argv
args = [sys.argv[0], yymmdd]
print args

