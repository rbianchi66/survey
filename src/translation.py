#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import os

translations = {}
lines = []

def loadFile(filename):
    i = 0
    for L in open(filename):
        if L.strip() and L[0] != "=" and "=" in L:
            c, m = L.split("=", 1)
            m = m.rstrip("\r\n")
            if m[0] == '[' and m[-1] == ']':
                m = m[1:-1]
                translations[c.strip()] = [e.strip().decode("utf-8", "replace") for e in m.split(",")]
            else:
                translations[c.strip()] = m.strip().decode("utf-8", "replace")
            lines.append(c.strip())
        i += 1

def loadTranslation(lang):
    if not hasattr(sys, 'frozen'):
        path = os.path.dirname(__file__)
    else:
        path = os.path.dirname(sys.argv[0])

    try:
        loadFile(os.path.join(path, "translations/default.txt"))
        loadFile(os.path.join(path, "translations/msg_%s.txt" % lang))
        if os.path.exists(os.path.join(path, "translations/custom_%s.txt" % lang)):
            loadFile(os.path.join(path, "translations/custom_%s.txt" % lang))
    except:
        pass

def saveTranslation(lang):
    if not hasattr(sys, 'frozen'):
        path = os.path.dirname(__file__)
    else:
        path = os.path.dirname(sys.argv[0])
    filename = os.path.join(path, "translations/msg_%s.txt" % lang)
    out = open(filename,"w")
    for e in lines:
        out.write("%s=%s\n"%(e,translations[e]))
    out.close()
    

def L(x, p = None):
    if p is not None:
        r = translations.get(x, [])
        if len(r) > p:
            return r[p]
        else:
            return "?"+x+"?"
    else:
        return translations.get(x, "?"+x+"?")
