#!/usr/bin/python3
#
# main.py
#
# central launcher that processes commandline arguments and selects interface.
#
# Here's your stinkin' licence: http://unlicense.org/
#
# - l0k1
#
# Contact details for l0k1
# steemit.com - https://steemit.com/@l0k1
# bitmessage - BM-2cXWxTVaXJbNyMxv5tAjNg87xS98hrAg8P
# torchat - xq6xcvqc2vy34qtx
# email - l0k1@null.net

"""
Main interface that works with the commandline interface, imports the 
user selected interface module, and launches the core module
"""

debugflag = True

import sys, os, argparse

parser = argparse.ArgumentParser(description="Steem Blockchain Interface")
parser.add_argument ('frontend', metavar='FRONTEND', type=str, nargs="?", default="gtk3", help="Interface frontend library to use, defaults to gtk3")
args = parser.parse_args()

print ("Interface chosen: " + args.frontend + "; importing " + args.frontend + ".py")

frontend_obj = __import__ (args.frontend)
globals () [args.frontend] = frontend_obj

if debugflag: frontend_obj.printmodulename ()

coremodule_obj = __import__ ("core")
globals () ["core"] = coremodule_obj
